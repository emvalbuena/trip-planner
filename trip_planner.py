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
    class Leg:
        """A leg of the trip with distance and travel time."""

        name: str
        distance_km: float
        travel_time_hours: float

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
        legs: list[Leg] = field(default_factory=list)
        gas_price_per_liter: float = 1.5
        fuel_consumption_per_100km: float = 8.0
        price_sleeping: float = 0.0
        price_food: float = 0.0
        activities: list[str] = field(default_factory=list)
        booking_urls: list[str] = field(default_factory=list)
        id: str = field(default_factory=lambda: str(uuid.uuid4()))

        @property
        def total_distance_km(self) -> float:
            return sum(leg.distance_km for leg in self.legs)

        @property
        def total_travel_time_hours(self) -> float:
            return sum(leg.travel_time_hours for leg in self.legs)

        @property
        def fuel_cost(self) -> float:
            liters = (self.total_distance_km / 100) * self.fuel_consumption_per_100km
            return liters * self.gas_price_per_liter

        @property
        def total_price(self) -> float:
            return self.fuel_cost + self.price_sleeping + self.price_food

    return Leg, Price, Trip


@app.cell
def _(Leg, Path, Trip, asdict, json, re):
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
        # Store computed values in JSON for easy reading
        data["total_distance_km"] = trip.total_distance_km
        data["total_travel_time_hours"] = trip.total_travel_time_hours
        data["fuel_cost"] = trip.fuel_cost
        data["total_price"] = trip.total_price
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return filepath

    def load_trip(filepath: Path) -> Trip:
        """Load a trip from a JSON file."""
        with open(filepath) as f:
            data = json.load(f)
        # Remove computed fields
        data.pop("total_distance_km", None)
        data.pop("total_travel_time_hours", None)
        data.pop("fuel_cost", None)
        data.pop("total_price", None)

        # Handle legacy format (pre-legs)
        if "price" in data:
            # Old format: convert to new format
            old_price = data.pop("price")
            travel_time = data.pop("travel_time_hours", 0)
            # Create a single leg from old data
            legs = [Leg(name="Trip", distance_km=0, travel_time_hours=travel_time)]
            return Trip(
                legs=legs,
                gas_price_per_liter=1.5,
                fuel_consumption_per_100km=8.0,
                price_sleeping=old_price.get("sleeping", 0),
                price_food=old_price.get("food", 0),
                **data,
            )

        # New format: convert legs dicts to Leg objects
        legs_data = data.pop("legs", [])
        legs = [Leg(**leg) for leg in legs_data]
        return Trip(legs=legs, **data)

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
    mo.md("# 🧳 Trip Planner")
    return


@app.cell
def _(mo):
    # State for tracking which trip to edit and refresh trigger
    get_edit_id, set_edit_id = mo.state(None)
    get_refresh, set_refresh = mo.state(0)
    # State for managing legs
    get_legs, set_legs = mo.state([])
    return get_edit_id, get_legs, get_refresh, set_edit_id, set_legs, set_refresh


@app.cell
def _(find_trip_by_id, get_edit_id, set_legs):
    # Load trip being edited (if any)
    _edit_id = get_edit_id()
    editing_trip = find_trip_by_id(_edit_id) if _edit_id else None
    # Sync legs state when editing
    if editing_trip:
        set_legs(
            [
                {
                    "name": leg.name,
                    "distance_km": leg.distance_km,
                    "travel_time_hours": leg.travel_time_hours,
                }
                for leg in editing_trip.legs
            ]
        )
    return (editing_trip,)


@app.cell
def _(editing_trip, mo):
    # Form UI elements
    form_title = "✏️ Edit Trip" if editing_trip else "➕ Create New Trip"

    name_input = mo.ui.text(
        value=editing_trip.name if editing_trip else "",
        label="🏷️ Trip Name",
        full_width=True,
    )
    gas_price_slider = mo.ui.slider(
        value=editing_trip.gas_price_per_liter if editing_trip else 1.5,
        start=0.5,
        stop=3.0,
        step=0.1,
        label="⛽ Gas Price ($/L)",
        show_value=True,
    )
    fuel_consumption_input = mo.ui.number(
        value=editing_trip.fuel_consumption_per_100km if editing_trip else 8.0,
        start=3.0,
        stop=20.0,
        step=0.5,
        label="🚗 Fuel Consumption (L/100km)",
    )
    sleeping_input = mo.ui.number(
        value=editing_trip.price_sleeping if editing_trip else 0,
        start=0,
        step=10,
        label="🛏️ Sleeping ($)",
    )
    food_input = mo.ui.number(
        value=editing_trip.price_food if editing_trip else 0,
        start=0,
        step=10,
        label="🍔 Food ($)",
    )
    activities_input = mo.ui.text_area(
        value=", ".join(editing_trip.activities) if editing_trip else "",
        label="🎯 Activities (comma-separated)",
        full_width=True,
    )
    booking_urls_input = mo.ui.text_area(
        value="\n".join(editing_trip.booking_urls) if editing_trip else "",
        label="🔗 Booking URLs (one per line)",
        full_width=True,
    )
    save_button = mo.ui.run_button(label="💾 Save Trip")
    return (
        activities_input,
        booking_urls_input,
        food_input,
        form_title,
        fuel_consumption_input,
        gas_price_slider,
        name_input,
        save_button,
        sleeping_input,
    )


@app.cell
def _(get_legs, mo, set_legs):
    # Leg management UI
    leg_name_input = mo.ui.text(label="📍 Leg Name", placeholder="e.g., Home → Paris")
    leg_distance_input = mo.ui.number(
        value=0, start=0, step=10, label="📏 Distance (km)"
    )
    leg_time_input = mo.ui.number(value=0, start=0, step=0.5, label="⏱️ Time (hours)")

    def add_leg(_):
        if leg_name_input.value.strip():
            current = get_legs()
            set_legs(
                current
                + [
                    {
                        "name": leg_name_input.value.strip(),
                        "distance_km": leg_distance_input.value,
                        "travel_time_hours": leg_time_input.value,
                    }
                ]
            )

    add_leg_button = mo.ui.button(label="➕ Add Leg", on_click=add_leg)

    def clear_legs(_):
        set_legs([])

    clear_legs_button = mo.ui.button(
        label="🗑️ Clear All Legs", kind="warn", on_click=clear_legs
    )

    return (
        add_leg_button,
        clear_legs_button,
        leg_distance_input,
        leg_name_input,
        leg_time_input,
    )


@app.cell
def _(get_legs, mo, set_legs):
    # Display current legs with remove buttons
    current_legs = get_legs()

    def make_remove_handler(idx):
        def handler(_):
            legs = get_legs()
            set_legs(legs[:idx] + legs[idx + 1 :])

        return handler

    legs_display = []
    for i, leg in enumerate(current_legs):
        remove_btn = mo.ui.button(label="❌", on_click=make_remove_handler(i))
        legs_display.append(
            mo.hstack(
                [
                    mo.md(
                        f"**{leg['name']}**: {leg['distance_km']} km, {leg['travel_time_hours']}h"
                    ),
                    remove_btn,
                ],
                justify="space-between",
            )
        )

    total_km = sum(leg["distance_km"] for leg in current_legs)
    total_hours = sum(leg["travel_time_hours"] for leg in current_legs)

    legs_summary = (
        mo.md(f"**📊 Total:** {total_km} km, {total_hours}h")
        if current_legs
        else mo.md("*No legs added yet*")
    )
    return (
        current_legs,
        legs_display,
        legs_summary,
        make_remove_handler,
        total_hours,
        total_km,
    )


@app.cell
def _(
    activities_input,
    add_leg_button,
    booking_urls_input,
    clear_legs_button,
    food_input,
    form_title,
    fuel_consumption_input,
    gas_price_slider,
    leg_distance_input,
    leg_name_input,
    leg_time_input,
    legs_display,
    legs_summary,
    mo,
    name_input,
    save_button,
    sleeping_input,
):
    # Display form
    mo.vstack(
        [
            mo.md(f"## {form_title}"),
            name_input,
            mo.md("### 🛣️ Trip Legs"),
            mo.hstack(
                [leg_name_input, leg_distance_input, leg_time_input, add_leg_button],
                justify="start",
                gap=1,
            ),
            mo.vstack(legs_display, gap=0.25) if legs_display else mo.md(""),
            mo.hstack([legs_summary, clear_legs_button], justify="space-between")
            if legs_display
            else legs_summary,
            mo.md("### 💰 Costs"),
            mo.hstack(
                [gas_price_slider, fuel_consumption_input], justify="start", gap=2
            ),
            mo.hstack([sleeping_input, food_input], justify="start", gap=1),
            activities_input,
            booking_urls_input,
            save_button,
        ],
        gap=0.5,
    )
    return


@app.cell
def _(
    Leg,
    Trip,
    activities_input,
    booking_urls_input,
    editing_trip,
    food_input,
    fuel_consumption_input,
    gas_price_slider,
    get_legs,
    get_refresh,
    mo,
    name_input,
    save_button,
    save_trip,
    set_edit_id,
    set_legs,
    set_refresh,
    sleeping_input,
    uuid,
):
    # Handle save
    mo.stop(not save_button.value)

    _name = name_input.value.strip()
    if not _name:
        mo.stop(True, mo.md("**❌ Error:** Please enter a trip name."))

    _legs_data = get_legs()
    if not _legs_data:
        mo.stop(True, mo.md("**❌ Error:** Please add at least one leg."))

    _legs = [
        Leg(
            name=leg["name"],
            distance_km=leg["distance_km"],
            travel_time_hours=leg["travel_time_hours"],
        )
        for leg in _legs_data
    ]
    _activities = [a.strip() for a in activities_input.value.split(",") if a.strip()]
    _urls = [u.strip() for u in booking_urls_input.value.split("\n") if u.strip()]

    _trip = Trip(
        name=_name,
        legs=_legs,
        gas_price_per_liter=gas_price_slider.value,
        fuel_consumption_per_100km=fuel_consumption_input.value,
        price_sleeping=sleeping_input.value,
        price_food=food_input.value,
        activities=_activities,
        booking_urls=_urls,
        id=editing_trip.id if editing_trip else str(uuid.uuid4()),
    )

    _path = save_trip(_trip)
    set_edit_id(None)
    set_legs([])
    set_refresh(get_refresh() + 1)

    mo.md(f"**✅ Saved:** {_trip.name} to `{_path}`")
    return


@app.cell
def _(editing_trip, mo, set_edit_id, set_legs):
    # Cancel button (only shown when editing)
    def cancel_edit(_):
        set_edit_id(None)
        set_legs([])

    cancel_button = mo.ui.button(
        label="❌ Cancel Edit",
        kind="warn",
        on_click=cancel_edit,
    )
    mo.md("") if not editing_trip else cancel_button
    return cancel_button, cancel_edit


@app.cell
def _(get_refresh, load_all_trips, mo):
    # Load trips (re-runs when refresh changes)
    _ = get_refresh()
    all_trips = load_all_trips()
    mo.md(
        f"---\n## 📋 Saved Trips ({len(all_trips)})"
        if all_trips
        else "---\n## 📋 Saved Trips\n\n*No trips saved yet.*"
    )
    return (all_trips,)


@app.cell
def _(
    all_trips,
    delete_trip_by_id,
    get_refresh,
    mo,
    set_edit_id,
    set_legs,
    set_refresh,
):
    # Trips table with actions
    def _make_edit_handler(trip):
        def handler(_):
            set_edit_id(trip.id)
            set_legs(
                [
                    {
                        "name": leg.name,
                        "distance_km": leg.distance_km,
                        "travel_time_hours": leg.travel_time_hours,
                    }
                    for leg in trip.legs
                ]
            )

        return handler

    def _make_delete_handler(tid):
        def handler(_):
            delete_trip_by_id(tid)
            set_refresh(get_refresh() + 1)

        return handler

    if all_trips:
        _rows = []
        for _trip in all_trips:
            _edit_btn = mo.ui.button(
                label="✏️",
                on_click=_make_edit_handler(_trip),
            )
            _del_btn = mo.ui.button(
                label="🗑️",
                kind="danger",
                on_click=_make_delete_handler(_trip.id),
            )
            _rows.append(
                {
                    "🏷️ Name": _trip.name,
                    "📏 Distance": f"{_trip.total_distance_km} km",
                    "⏱️ Time": f"{_trip.total_travel_time_hours}h",
                    "⛽ Fuel": f"${_trip.fuel_cost:.2f}",
                    "🛏️ Sleep": f"${_trip.price_sleeping:.2f}",
                    "🍔 Food": f"${_trip.price_food:.2f}",
                    "💰 Total": f"${_trip.total_price:.2f}",
                    "🎯 Activities": ", ".join(_trip.activities) or "-",
                    "🔗 URLs": len(_trip.booking_urls),
                    "Actions": mo.hstack([_edit_btn, _del_btn], gap=0.5),
                }
            )
        trips_table = mo.ui.table(_rows, selection=None)
        trips_table
    return (trips_table,)


@app.cell
def _(mo):
    mo.md("---\n## 📊 Comparison\n\n*Comparison features coming soon...*")
    return


if __name__ == "__main__":
    app.run()
