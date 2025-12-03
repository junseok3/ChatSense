# backend/app/model.py
from typing import List, Dict
import torch, json, numpy as np
from transformers import CLIPModel, CLIPProcessor

class EmojiModel:
    def __init__(self, base="backend/indexes"):  
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.clip_name = "openai/clip-vit-base-patch32"
        self.model = CLIPModel.from_pretrained(self.clip_name).to(self.device).eval()
        self.processor = CLIPProcessor.from_pretrained(self.clip_name)

        def load_one(kind):
            emb = torch.load(f"{base}/{kind}_embeddings.pt", map_location=self.device) 
            with open(f"{base}/{kind}_meta.json", "r", encoding="utf-8") as f:
                meta = json.load(f)  

            for m in meta:
                filename = m["path"].split("/")[-1]
                m["url"] = f"/assets/{kind}/{filename}"
            return emb, meta

        self.emoji_emb, self.emoji_meta = load_one("emoji")
        self.meme_emb,  self.meme_meta  = load_one("meme")
        self.gif_emb,   self.gif_meta   = load_one("gif")

      
        def l2norm(x): return x / (x.norm(dim=-1, keepdim=True) + 1e-8)
        self.emoji_emb = l2norm(self.emoji_emb)
        self.meme_emb  = l2norm(self.meme_emb)
        self.gif_emb   = l2norm(self.gif_emb)

    def _text_embed(self, text: str) -> torch.Tensor:
       
        inputs = self.processor(text=[text], return_tensors="pt", padding=True).to(self.device)
        with torch.no_grad():
            t = self.model.get_text_features(**inputs)  
            t = t / (t.norm(dim=-1, keepdim=True) + 1e-8)
        return t

    def _top1(self, t: torch.Tensor, bank: torch.Tensor, meta: List[Dict]) -> Dict:
        
        sims = (bank @ t.squeeze(0).T).float()      
        idx = int(torch.argmax(sims).item())
        score = float(sims[idx].clamp(min=-1.0, max=1.0).item())
        out = dict(meta[idx])                        
        out["score"] = round((score + 1) / 2, 4)      
        return out

    def predict(self, text: str) -> List[Dict]:
        t = self._text_embed(text)
        emoji = self._top1(t, self.emoji_emb, self.emoji_meta)
        meme  = self._top1(t, self.meme_emb,  self.meme_meta)
        gif   = self._top1(t, self.gif_emb,   self.gif_meta)
     
        return [
            {"type": "emoji", **emoji},
            {"type": "meme",  **meme},
            {"type": "gif",   **gif},
        ]
