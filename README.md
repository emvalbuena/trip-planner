# Trip Planner

> **Alpha version** - Work in progress, expect bugs and breaking changes.

A marimo notebook for planning and comparing road trips.

## Features

- **Multi-leg trips**: Add multiple legs with distance, travel time, sleeping and food costs
- **Fuel calculation**: Configurable fuel price (€/L) and consumption (L/100km)
- **Trip management**: Create, save, preview, edit, and delete trips
- **Cost breakdown**: See totals for fuel, sleeping, food, and overall trip cost
- **Activities & URLs**: Track planned activities and booking links

### Pending

- [ ] Trip comparison mode

## Quick Start

```bash
# Install dependencies
uv sync

# Run the notebook
uv run marimo edit trip_planner.py
```

## Development

```bash
# Run tests
uv run pytest

# Format code
uv run ruff format .

# Lint
uv run ruff check .
```

## Data

Trips are saved as JSON files in the `trips/` folder.
