# ChatSense
<img width="1154" height="759" alt="image" src="https://github.com/user-attachments/assets/5043639f-f778-481a-b310-f4dd691a1357" />

A monorepo for deploying a multimodal recommendation system (emoji/GIF/meme) with a unified backend workflow.

## Project Summary

ChatSense uses multimodal embeddings to map user chat input to relevant reactions/content.
Training and experiment iteration were completed in Google Colab, and this repository focuses on backend integration and serving.

## Current Scope of This Repo

-  FastAPI backend scaffold (`/health`, inference integration path)
-  Monorepo structure for backend / ml / frontend collaboration
-  Dev Container for reproducible team development
-  Integration of trained artifacts/weights into inference workflow
-  Colab notebooks are not fully mirrored here yet (this repo is deployment/integration-first)

## What was completed in Colab

- Multimodal embedding experiments and iteration
- Retrieval quality checks across target content types
- Model/weight selection for backend integration

> Note: This repository contains the deployment-oriented structure and integration path.
> Some experiment notebooks remain in Colab and may be migrated later.

## Repository Structure

.
├─ backend/            # FastAPI server (model loading/inference)
│  └─ app/
│     ├─ main.py
│     └─ model.py
├─ ml/                 # ML artifacts / migration area for training scripts
│  └─ README.md
├─ frontend/           # Frontend scaffold
│  └─ README.md
├─ .vscode/
├─ .devcontainer/
├─ .github/
├─ .env.example
└─ README.md

## Quick Start

```bash
cd backend
uvicorn app.main:app --reload --port 8000
