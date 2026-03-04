# Project Agent Guide

## Mission
Build a **local single-player text adventure MVP** that can later be shared with a few friends as a locally hosted app.

## Hard Constraints
1. No multiplayer and no login system.
2. Theme must be swappable. Default theme is an original ninja/jianghu-style setting. Avoid direct commercial-IP proper nouns.
3. AI is narration-only (scene description, NPC dialogue, quest copy, combat commentary). AI must never mutate world state directly.
4. All content is data-driven (JSON/YAML for rooms, NPCs, items, quests, dialogue templates). Code provides engine/rules only.
5. Prioritize maintainability and clean layering.

## Working Style
- Implement only one small, runnable/testable step at a time.
- After each step:
  - summarize changed files,
  - provide run commands,
  - describe browser validation steps,
  - suggest next step,
  - then stop and wait for user confirmation.

## Default Stack
- Python 3.11+
- FastAPI + simple local web UI (Jinja2 or minimal HTML)
- SQLite save file via SQLModel or SQLAlchemy (keep simple)
- Dependency management via `requirements.txt` or `pyproject.toml`
- Tests via `pytest` (minimum tests for core rules)

## MVP Commands
Planned command set:
- `look`
- `go <direction|place>`
- `talk <npc>`
- `inv`
- `use <item>`
- `status`
- `help`

## Data Model Targets
- Player
- Room
- NPC
- Item
- Quest

## AI Integration Rule
Introduce a `NarratorService` interface with structured input/output. Use local templates first. If model calls are added later, enforce strict JSON and validate IDs/rewards before persistence.
