import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import json
    import re
    import uuid
    from dataclasses import asdict, dataclass, field
    from pathlib import Path

    return Path, asdict, dataclass, field, json, re, uuid


@app.cell
def _(dataclass, field, uuid):
    @dataclass
    class Price:
        fuel: float = 0.0
        sleeping: float = 0.0
        food: float = 0.0

        @property
        def total(self) -> float:
            return self.fuel + self.sleeping + self.food

    @dataclass
    class Trip:
        name: str
        travel_time_hours: float
        price: Price
        activities: list[str] = field(default_factory=list)
        booking_urls: list[str] = field(default_factory=list)
        id: str = field(default_factory=lambda: str(uuid.uuid4()))

        @property
        def total_price(self) -> float:
            return self.price.total

    return Price, Trip


@app.cell
def _(Path, Price, Trip, asdict, json, re):
    TRIPS_FOLDER = Path("trips")

    def slugify(text: str) -> str:
        """Convert text to URL-friendly slug."""
        text = text.lower().strip()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[-\s]+", "-", text)
        return text

    def get_trip_filename(trip: Trip) -> str:
        """Generate filename from trip name and ID."""
        slug = slugify(trip.name)
        short_id = trip.id[:8]
        return f"{slug}_{short_id}.json"

    def save_trip(trip: Trip, folder: Path = TRIPS_FOLDER) -> Path:
        """Save a trip to a JSON file."""
        folder.mkdir(exist_ok=True)
        filepath = folder / get_trip_filename(trip)
        data = asdict(trip)
        data["total_price"] = trip.total_price
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return filepath

    def load_trip(filepath: Path) -> Trip:
        """Load a trip from a JSON file."""
        with open(filepath) as f:
            data = json.load(f)
        data.pop("total_price", None)
        price_data = data.pop("price")
        return Trip(price=Price(**price_data), **data)

    def load_all_trips(folder: Path = TRIPS_FOLDER) -> list[Trip]:
        """Load all trips from a folder."""
        if not folder.exists():
            return []
        trips = []
        for filepath in folder.glob("*.json"):
            try:
                trips.append(load_trip(filepath))
            except (json.JSONDecodeError, KeyError):
                continue
        return sorted(trips, key=lambda t: t.name.lower())

    def delete_trip_by_id(trip_id: str, folder: Path = TRIPS_FOLDER) -> bool:
        """Delete a trip by ID."""
        for filepath in folder.glob("*.json"):
            try:
                trip = load_trip(filepath)
                if trip.id == trip_id:
                    filepath.unlink()
                    return True
            except (json.JSONDecodeError, KeyError):
                continue
        return False

    def find_trip_by_id(trip_id: str, folder: Path = TRIPS_FOLDER) -> Trip | None:
        """Find a trip by its ID."""
        for trip in load_all_trips(folder):
            if trip.id == trip_id:
                return trip
        return None

    return (
        TRIPS_FOLDER,
        delete_trip_by_id,
        find_trip_by_id,
        get_trip_filename,
        load_all_trips,
        load_trip,
        save_trip,
        slugify,
    )


@app.cell
def _(mo):
    mo.md("# Trip Planner")
    return


@app.cell
def _(mo):
    # State for tracking which trip to edit and refresh trigger
    get_edit_id, set_edit_id = mo.state(None)
    get_refresh, set_refresh = mo.state(0)
    return get_edit_id, get_refresh, set_edit_id, set_refresh


@app.cell
def _(find_trip_by_id, get_edit_id):
    # Load trip being edited (if any)
    _edit_id = get_edit_id()
    editing_trip = find_trip_by_id(_edit_id) if _edit_id else None
    return (editing_trip,)


@app.cell
def _(editing_trip, mo):
    # Form UI elements
    form_title = "Edit Trip" if editing_trip else "Create New Trip"

    name_input = mo.ui.text(
        value=editing_trip.name if editing_trip else "",
        label="Trip Name",
        full_width=True,
    )
    travel_time_input = mo.ui.number(
        value=editing_trip.travel_time_hours if editing_trip else 0,
        start=0,
        stop=1000,
        step=0.5,
        label="Travel Time (hours)",
    )
    fuel_input = mo.ui.number(
        value=editing_trip.price.fuel if editing_trip else 0,
        start=0,
        step=10,
        label="Fuel ($)",
    )
    sleeping_input = mo.ui.number(
        value=editing_trip.price.sleeping if editing_trip else 0,
        start=0,
        step=10,
        label="Sleeping ($)",
    )
    food_input = mo.ui.number(
        value=editing_trip.price.food if editing_trip else 0,
        start=0,
        step=10,
        label="Food ($)",
    )
    activities_input = mo.ui.text_area(
        value=", ".join(editing_trip.activities) if editing_trip else "",
        label="Activities (comma-separated)",
        full_width=True,
    )
    booking_urls_input = mo.ui.text_area(
        value="\n".join(editing_trip.booking_urls) if editing_trip else "",
        label="Booking URLs (one per line)",
        full_width=True,
    )
    save_button = mo.ui.run_button(label="Save Trip")
    return (
        activities_input,
        booking_urls_input,
        food_input,
        form_title,
        fuel_input,
        name_input,
        save_button,
        sleeping_input,
        travel_time_input,
    )


@app.cell
def _(
    activities_input,
    booking_urls_input,
    food_input,
    form_title,
    fuel_input,
    mo,
    name_input,
    save_button,
    sleeping_input,
    travel_time_input,
):
    # Display form
    mo.vstack(
        [
            mo.md(f"## {form_title}"),
            name_input,
            travel_time_input,
            mo.md("### Price Breakdown"),
            mo.hstack([fuel_input, sleeping_input, food_input], justify="start", gap=1),
            activities_input,
            booking_urls_input,
            save_button,
        ],
        gap=0.5,
    )
    return


@app.cell
def _(
    Price,
    Trip,
    activities_input,
    booking_urls_input,
    editing_trip,
    food_input,
    fuel_input,
    get_refresh,
    mo,
    name_input,
    save_button,
    save_trip,
    set_edit_id,
    set_refresh,
    sleeping_input,
    travel_time_input,
    uuid,
):
    # Handle save
    mo.stop(not save_button.value)

    _name = name_input.value.strip()
    if not _name:
        mo.stop(True, mo.md("**Error:** Please enter a trip name."))

    _activities = [a.strip() for a in activities_input.value.split(",") if a.strip()]
    _urls = [u.strip() for u in booking_urls_input.value.split("\n") if u.strip()]

    _trip = Trip(
        name=_name,
        travel_time_hours=travel_time_input.value,
        price=Price(
            fuel=fuel_input.value,
            sleeping=sleeping_input.value,
            food=food_input.value,
        ),
        activities=_activities,
        booking_urls=_urls,
        id=editing_trip.id if editing_trip else str(uuid.uuid4()),
    )

    _path = save_trip(_trip)
    set_edit_id(None)
    set_refresh(get_refresh() + 1)

    mo.md(f"**Saved:** {_trip.name} to `{_path}`")
    return


@app.cell
def _(editing_trip, mo, set_edit_id):
    # Cancel button (only shown when editing)
    cancel_button = mo.ui.button(
        label="Cancel Edit",
        kind="warn",
        on_click=lambda _: set_edit_id(None),
    )
    mo.md("") if not editing_trip else cancel_button
    return (cancel_button,)


@app.cell
def _(get_refresh, load_all_trips, mo):
    # Load trips (re-runs when refresh changes)
    _ = get_refresh()
    all_trips = load_all_trips()
    mo.md(
        f"---\n## Saved Trips ({len(all_trips)} trips)"
        if all_trips
        else "---\n## Saved Trips\n\n*No trips saved yet.*"
    )
    return (all_trips,)


@app.cell
def _(
    all_trips,
    delete_trip_by_id,
    get_refresh,
    mo,
    set_edit_id,
    set_refresh,
):
    # Trips table with actions
    def _make_edit_handler(tid):
        return lambda _: set_edit_id(tid)

    def _make_delete_handler(tid):
        def handler(_):
            delete_trip_by_id(tid)
            set_refresh(get_refresh() + 1)

        return handler

    if all_trips:
        _rows = []
        for _trip in all_trips:
            _edit_btn = mo.ui.button(
                label="Edit",
                on_click=_make_edit_handler(_trip.id),
            )
            _del_btn = mo.ui.button(
                label="Delete",
                kind="danger",
                on_click=_make_delete_handler(_trip.id),
            )
            _rows.append(
                {
                    "Name": _trip.name,
                    "Travel (h)": _trip.travel_time_hours,
                    "Fuel ($)": _trip.price.fuel,
                    "Sleep ($)": _trip.price.sleeping,
                    "Food ($)": _trip.price.food,
                    "Total ($)": _trip.total_price,
                    "Activities": ", ".join(_trip.activities) or "-",
                    "URLs": len(_trip.booking_urls),
                    "Actions": mo.hstack([_edit_btn, _del_btn], gap=0.5),
                }
            )
        trips_table = mo.ui.table(_rows, selection=None)
        trips_table
    return (trips_table,)


@app.cell
def _(mo):
    mo.md("---\n## Comparison\n\n*Comparison features coming soon...*")
    return


if __name__ == "__main__":
    app.run()
