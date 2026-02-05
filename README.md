# MOSS

MOSS 是一个面向个人的 AI 主助理项目，强调**长期记忆、主动沟通、成长教练**和**可扩展能力**。

## 仓库结构

```
backend/   # FastAPI 后端
frontend/  # Vite + React 前端
docs/      # 需求与设计文档
```

## 快速启动（开发）

### 后端
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 前端
```bash
cd frontend
npm install
npm run dev
```
