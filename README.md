ChatSense Monorepo

A starter repository configured so the whole team can work in VS Code right away.

Tech Stack (proposed)

Backend (Python/FastAPI): Model loading and APIs (/predict, /health)

ML: Training/experiment scripts (to be added)

Frontend: Web/app client (to be added)

Dev Container: Consistent development environment (Codespaces / VS Code Dev Containers)

Structure

.
├─ backend/            # FastAPI server (model loading/inference)
│  └─ app/
│     ├─ main.py
│     └─ model.py
├─ ml/                 # ML training/experiment code
│  └─ README.md
├─ frontend/           # Frontend (scaffold later if needed)
│  └─ README.md
├─ .vscode/            # Recommended workspace settings/extensions
├─ .devcontainer/      # Unified dev environment (Docker-based)
├─ .github/            # CI, PR/Issue templates
├─ .env.example        # Example env vars (tokens/paths, etc.)
├─ .editorconfig
├─ .gitattributes
├─ .gitignore
├─ CODEOWNERS
├─ LICENSE             # Update as needed
└─ README.md
Quick Start

Create an empty private repo on GitHub (e.g., chatsense).

Initial push:

git init
git remote add origin <YOUR_GITHUB_REPO_URL>
git add .
git commit -m "chore: bootstrap ChatSense monorepo"
git branch -M main
git push -u origin main


Invite collaborators & set branch protection

Settings ▸ Collaborators → add teammates

Settings ▸ Branches → protect main: enable “Require PR” and “Require status checks (CI)” (recommended)

Open in Dev Container

In VS Code, run “Reopen in Container” to use the same environment

Run the backend:

cd backend
uvicorn app.main:app --reload --port 8000


Health check: http://localhost:8000/health

Environment Variables

Create a .env file at the repo root or inside each service (see .env.example)

Do not commit real secrets (store them in GitHub Actions Secrets)

Branching Strategy (suggested)

Base: main (protected), Integration: dev (optional), Features: feature/<slug>

Commit prefixes: feat:, fix:, chore:, docs:, refactor:, etc.

PR rules: small, well-described, with tests when possible; at least 1 review

CI

.github/workflows/ci.yml runs pre-commit hooks across the repo to check formatting/linting.

Backend Roadmap (example)

 /predict accepts text and returns Top-K emojis

 Load model/weights (local models/ or Hugging Face Hub)

 Add Dockerfile/Compose for deployment (later)

See the README in each folder for details
