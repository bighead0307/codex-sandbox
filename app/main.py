from __future__ import annotations

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Text World MVP")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    logs = [
        "欢迎来到本地文字世界 MVP。",
        "输入 help 查看可用命令（后续步骤实现）。",
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"logs": logs, "last_command": ""},
    )


@app.post("/command", response_class=HTMLResponse)
def submit_command(request: Request, command: str = Form(...)) -> HTMLResponse:
    cleaned = command.strip()
    logs = [
        "欢迎来到本地文字世界 MVP。",
        f"> {cleaned or '(空命令)'}",
        "Step 0: 命令引擎尚未接入；下一步将实现 look/go。",
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"logs": logs, "last_command": cleaned},
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
