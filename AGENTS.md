# AGENTS.md

## Workflow
- Always commit after making changes
- Always run tests after making changes: `uv run pytest`

## Build/Test Commands
- Install deps: `uv sync`
- Run marimo notebook: `uv run marimo edit <notebook.py>`
- Run single test: `uv run pytest path/to/test.py::test_function -v`
- Run all tests: `uv run pytest`
- Type check: `uv run pyright`
- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`

## Code Style
- Python 3.13+ required
- Use type hints for all function signatures
- Imports: stdlib, blank line, third-party, blank line, local
- Naming: snake_case for functions/variables, PascalCase for classes
- Use `ruff` for linting and formatting (line length 88)
- Prefer explicit over implicit; avoid bare `except:`

## Marimo Notebooks
- Import as `import marimo as mo`
- Use `@app.cell` decorator for cells
- Layout: `mo.hstack()`, `mo.vstack()`, `mo.tabs()` for arranging elements
- UI elements return values via `.value` attribute
- Access UI values in separate cells from where they're defined
