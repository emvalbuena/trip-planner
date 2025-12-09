"""Tests for road trip planner data models and functions."""

import uuid
from dataclasses import asdict, dataclass, field


# Copy dataclasses from trip_planner.py for testing
@dataclass
class Leg:
    """A leg of the road trip with origin, destination, distance, time, and costs."""

    origin: str
    destination: str
    distance_km: float
    travel_time_hours: float
    sleeping_cost: float = 0.0
    food_cost: float = 0.0

    @property
    def driving_breaks(self) -> int:
        """Auto-calculate breaks: 1 break per 2 hours of driving."""
        return int(self.travel_time_hours // 2)

    @property
    def total_break_time_minutes(self) -> int:
        """Total break time: 10 minutes per break."""
        return self.driving_breaks * 10

    @property
    def total_cost(self) -> float:
        """Total cost for this leg (excluding fuel)."""
        return self.sleeping_cost + self.food_cost


@dataclass
class Trip:
    name: str
    legs: list[Leg] = field(default_factory=list)
    fuel_price_per_litre: float = 1.6
    fuel_consumption_per_100km: float = 7.0
    num_people: int = 1
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
    def total_driving_breaks(self) -> int:
        """Total number of driving breaks across all legs."""
        return sum(leg.driving_breaks for leg in self.legs)

    @property
    def total_break_time_minutes(self) -> int:
        """Total break time in minutes across all legs."""
        return sum(leg.total_break_time_minutes for leg in self.legs)

    @property
    def route_waypoints(self) -> list[str]:
        """Get ordered list of waypoints from all legs."""
        if not self.legs:
            return []
        waypoints = [self.legs[0].origin]
        for leg in self.legs:
            waypoints.append(leg.destination)
        return waypoints

    @property
    def fuel_cost(self) -> float:
        litres = (self.total_distance_km / 100) * self.fuel_consumption_per_100km
        return litres * self.fuel_price_per_litre

    @property
    def total_sleeping_cost(self) -> float:
        return sum(leg.sleeping_cost for leg in self.legs)

    @property
    def total_food_cost(self) -> float:
        return sum(leg.food_cost for leg in self.legs)

    @property
    def total_price(self) -> float:
        return self.fuel_cost + self.total_sleeping_cost + self.total_food_cost

    @property
    def cost_per_person(self) -> float:
        """Total cost divided by number of travelers."""
        return self.total_price / self.num_people


class TestLeg:
    """Tests for Leg dataclass."""

    def test_leg_creation(self):
        leg = Leg(
            origin="Home", destination="Paris", distance_km=500, travel_time_hours=5
        )
        assert leg.origin == "Home"
        assert leg.destination == "Paris"
        assert leg.distance_km == 500
        assert leg.travel_time_hours == 5
        assert leg.sleeping_cost == 0.0
        assert leg.food_cost == 0.0

    def test_leg_with_costs(self):
        leg = Leg(
            origin="Paris",
            destination="Lyon",
            distance_km=450,
            travel_time_hours=4.5,
            sleeping_cost=100,
            food_cost=50,
        )
        assert leg.sleeping_cost == 100
        assert leg.food_cost == 50

    def test_leg_total_cost(self):
        leg = Leg(
            origin="A",
            destination="B",
            distance_km=100,
            travel_time_hours=1,
            sleeping_cost=80,
            food_cost=30,
        )
        assert leg.total_cost == 110

    def test_leg_driving_breaks_calculation(self):
        """Test driving breaks: 1 break per 2 hours."""
        # 1 hour = 0 breaks
        leg1 = Leg(origin="A", destination="B", distance_km=100, travel_time_hours=1)
        assert leg1.driving_breaks == 0
        assert leg1.total_break_time_minutes == 0

        # 2 hours = 1 break
        leg2 = Leg(origin="A", destination="B", distance_km=200, travel_time_hours=2)
        assert leg2.driving_breaks == 1
        assert leg2.total_break_time_minutes == 10

        # 5 hours = 2 breaks
        leg3 = Leg(origin="A", destination="B", distance_km=500, travel_time_hours=5)
        assert leg3.driving_breaks == 2
        assert leg3.total_break_time_minutes == 20

        # 8 hours = 4 breaks
        leg4 = Leg(origin="A", destination="B", distance_km=800, travel_time_hours=8)
        assert leg4.driving_breaks == 4
        assert leg4.total_break_time_minutes == 40


class TestTrip:
    """Tests for Trip dataclass."""

    def test_trip_creation_empty(self):
        trip = Trip(name="Summer Vacation")
        assert trip.name == "Summer Vacation"
        assert trip.legs == []
        assert trip.fuel_price_per_litre == 1.6
        assert trip.fuel_consumption_per_100km == 7.0
        assert trip.num_people == 1
        assert trip.activities == []
        assert trip.booking_urls == []
        assert trip.id is not None

    def test_trip_with_legs(self):
        legs = [
            Leg(
                origin="Home", destination="Paris", distance_km=200, travel_time_hours=2
            ),
            Leg(
                origin="Paris", destination="Lyon", distance_km=300, travel_time_hours=3
            ),
        ]
        trip = Trip(name="Road Trip", legs=legs)
        assert len(trip.legs) == 2
        assert trip.total_distance_km == 500
        assert trip.total_travel_time_hours == 5

    def test_fuel_cost_calculation(self):
        """Test: fuel_cost = (km / 100) * consumption * price_per_litre."""
        legs = [
            Leg(origin="A", destination="B", distance_km=1000, travel_time_hours=10)
        ]
        trip = Trip(
            name="Test Trip",
            legs=legs,
            fuel_price_per_litre=1.5,
            fuel_consumption_per_100km=8.0,
        )
        # 1000 km / 100 = 10 units
        # 10 * 8.0 L/100km = 80 litres
        # 80 * 1.5 €/L = 120 €
        assert trip.fuel_cost == 120.0

    def test_fuel_cost_with_default_values(self):
        """Test fuel cost with default fuel price (1.6) and consumption (7.0)."""
        legs = [Leg(origin="A", destination="B", distance_km=500, travel_time_hours=5)]
        trip = Trip(name="Test Trip", legs=legs)
        # 500 km / 100 = 5 units
        # 5 * 7.0 = 35 litres
        # 35 * 1.6 = 56 €
        assert trip.fuel_cost == 56.0

    def test_total_sleeping_cost(self):
        legs = [
            Leg(
                origin="A",
                destination="B",
                distance_km=100,
                travel_time_hours=1,
                sleeping_cost=50,
            ),
            Leg(
                origin="B",
                destination="C",
                distance_km=100,
                travel_time_hours=1,
                sleeping_cost=75,
            ),
        ]
        trip = Trip(name="Test", legs=legs)
        assert trip.total_sleeping_cost == 125

    def test_total_food_cost(self):
        legs = [
            Leg(
                origin="A",
                destination="B",
                distance_km=100,
                travel_time_hours=1,
                food_cost=30,
            ),
            Leg(
                origin="B",
                destination="C",
                distance_km=100,
                travel_time_hours=1,
                food_cost=45,
            ),
        ]
        trip = Trip(name="Test", legs=legs)
        assert trip.total_food_cost == 75

    def test_total_price(self):
        """Test total price = fuel + sleeping + food."""
        legs = [
            Leg(
                origin="A",
                destination="B",
                distance_km=500,
                travel_time_hours=5,
                sleeping_cost=100,
                food_cost=50,
            ),
        ]
        trip = Trip(
            name="Test",
            legs=legs,
            fuel_price_per_litre=2.0,
            fuel_consumption_per_100km=10.0,
        )
        # Fuel: 500/100 * 10 * 2 = 100 €
        # Sleeping: 100 €
        # Food: 50 €
        # Total: 250 €
        assert trip.total_price == 250.0

    def test_trip_with_activities(self):
        trip = Trip(
            name="Adventure",
            activities=["Hiking", "Swimming", "Sightseeing"],
        )
        assert len(trip.activities) == 3
        assert "Hiking" in trip.activities

    def test_trip_with_booking_urls(self):
        trip = Trip(
            name="Booked Trip",
            booking_urls=["https://hotel.com", "https://flights.com"],
        )
        assert len(trip.booking_urls) == 2

    def test_empty_trip_calculations(self):
        """Test that empty trip has zero costs."""
        trip = Trip(name="Empty")
        assert trip.total_distance_km == 0
        assert trip.total_travel_time_hours == 0
        assert trip.fuel_cost == 0.0
        assert trip.total_sleeping_cost == 0
        assert trip.total_food_cost == 0
        assert trip.total_price == 0.0

    def test_total_driving_breaks(self):
        """Test total driving breaks across multiple legs."""
        legs = [
            Leg(
                origin="A", destination="B", distance_km=200, travel_time_hours=2
            ),  # 1 break
            Leg(
                origin="B", destination="C", distance_km=400, travel_time_hours=4
            ),  # 2 breaks
            Leg(
                origin="C", destination="D", distance_km=100, travel_time_hours=1
            ),  # 0 breaks
        ]
        trip = Trip(name="Test", legs=legs)
        assert trip.total_driving_breaks == 3
        assert trip.total_break_time_minutes == 30

    def test_route_waypoints(self):
        """Test route waypoints extraction."""
        legs = [
            Leg(
                origin="Paris",
                destination="Lyon",
                distance_km=450,
                travel_time_hours=4.5,
            ),
            Leg(
                origin="Lyon", destination="Nice", distance_km=300, travel_time_hours=3
            ),
            Leg(
                origin="Nice",
                destination="Barcelona",
                distance_km=500,
                travel_time_hours=5,
            ),
        ]
        trip = Trip(name="France to Spain", legs=legs)
        assert trip.route_waypoints == ["Paris", "Lyon", "Nice", "Barcelona"]

    def test_route_waypoints_empty(self):
        """Test route waypoints with no legs."""
        trip = Trip(name="Empty")
        assert trip.route_waypoints == []

    def test_num_people_default(self):
        """Test default number of people is 1."""
        trip = Trip(name="Solo Trip")
        assert trip.num_people == 1

    def test_cost_per_person_single(self):
        """Test cost per person with single traveler."""
        legs = [
            Leg(
                origin="A",
                destination="B",
                distance_km=500,
                travel_time_hours=5,
                sleeping_cost=100,
                food_cost=50,
            ),
        ]
        trip = Trip(
            name="Test",
            legs=legs,
            fuel_price_per_litre=2.0,
            fuel_consumption_per_100km=10.0,
            num_people=1,
        )
        # Total: 250 € / 1 person = 250 €
        assert trip.cost_per_person == 250.0

    def test_cost_per_person_multiple(self):
        """Test cost per person with multiple travelers."""
        legs = [
            Leg(
                origin="A",
                destination="B",
                distance_km=500,
                travel_time_hours=5,
                sleeping_cost=100,
                food_cost=50,
            ),
        ]
        trip = Trip(
            name="Test",
            legs=legs,
            fuel_price_per_litre=2.0,
            fuel_consumption_per_100km=10.0,
            num_people=5,
        )
        # Total: 250 € / 5 people = 50 €
        assert trip.cost_per_person == 50.0


class TestTripSerialization:
    """Tests for Trip serialization to/from dict."""

    def test_trip_to_dict(self):
        leg = Leg(
            origin="Home", destination="Paris", distance_km=100, travel_time_hours=1
        )
        trip = Trip(name="Test Trip", legs=[leg], id="test-id-123")
        data = asdict(trip)

        assert data["name"] == "Test Trip"
        assert data["id"] == "test-id-123"
        assert data["num_people"] == 1
        assert len(data["legs"]) == 1
        assert data["legs"][0]["origin"] == "Home"
        assert data["legs"][0]["destination"] == "Paris"
        assert data["fuel_price_per_litre"] == 1.6
        assert data["fuel_consumption_per_100km"] == 7.0
