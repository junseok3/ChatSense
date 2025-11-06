# ChatSense Monorepo

팀원 모두가 VS Code에서 바로 작업할 수 있도록 구성된 스타터 레포지토리입니다.

## Tech Stack (기본 제안)
- **Backend (Python/FastAPI)**: 모델 로딩 및 API (`/predict`, `/health`)
- **ML**: 학습/실험 스크립트(추가 예정)
- **Frontend**: 웹/앱 클라이언트(추가 예정)
- **Dev Container**: 동일한 개발 환경 보장 (Codespaces/VS Code Dev Containers)

## 구조
```
.
├─ backend/            # FastAPI 서버 (모델 로딩/추론)
│  └─ app/
│     ├─ main.py
│     └─ model.py
├─ ml/                 # ML 학습/실험 코드
│  └─ README.md
├─ frontend/           # 프론트엔드(원하면 추후 scaffold)
│  └─ README.md
├─ .vscode/            # 워크스페이스 추천 설정/확장
├─ .devcontainer/      # 통일된 개발환경 (Docker 기반)
├─ .github/            # CI, PR/Issue 템플릿
├─ .env.example        # 환경변수 예시(토큰/경로 등)
├─ .editorconfig
├─ .gitattributes
├─ .gitignore
├─ CODEOWNERS
├─ LICENSE             # 필요 시 수정
└─ README.md
```

## 빠른 시작
1) **GitHub에 빈 Private 레포 생성** (예: `chatsense`).
2) 아래 명령으로 초기 push:
```bash
git init
git remote add origin <YOUR_GITHUB_REPO_URL>
git add .
git commit -m "chore: bootstrap ChatSense monorepo"
git branch -M main
git push -u origin main
```
3) **Collaborators** 초대 & **Branch Protection** 설정
   - Settings ▸ Collaborators 에 팀원 추가
   - Settings ▸ Branches ▸ *main* 보호: “Require PR”, “Require status checks (CI)” 활성화 추천

4) **Dev Container로 열기**
   - VS Code에서 "Reopen in Container" 실행 → 동일 환경 사용
   - Back-end 실행:
     ```bash
     cd backend
     uvicorn app.main:app --reload --port 8000
     ```
   - Health Check: http://localhost:8000/health

5) **환경변수 설정**
   - `.env` 파일을 루트나 서비스 폴더에 생성 (예시는 `.env.example` 참고)
   - 절대 *실제 키는 커밋 금지* (GitHub Actions Secrets 사용)

## 브랜치 전략(제안)
- 기본: `main` (보호), 개발통합: `dev` (선택), 기능: `feature/<slug>`
- 커밋: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:` 등 사용
- PR 규칙: 작은 단위, 설명/테스트 포함, 리뷰 1+

## CI
- `.github/workflows/ci.yml` 은 **pre-commit** 훅을 전체 파일에 실행하여 포맷/린트 확인

## 백엔드 로드맵(예시)
- [ ] `/predict`에서 텍스트 입력 받아 이모지 Top-K 반환
- [ ] 모델/가중치 로딩(로컬 `models/` 또는 Hugging Face Hub)
- [ ] 배포용 Dockerfile/Compose 추가 (추후)

## 폴더 별 README를 참고하세요.
