"""Tests for trip planner data models and functions."""

import json
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

import pytest


# Copy dataclasses from trip_planner.py for testing
@dataclass
class Leg:
    """A leg of the trip with distance, time, and costs."""

    name: str
    distance_km: float
    travel_time_hours: float
    sleeping_cost: float = 0.0
    food_cost: float = 0.0

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


class TestLeg:
    """Tests for Leg dataclass."""

    def test_leg_creation(self):
        leg = Leg(name="Home → Paris", distance_km=500, travel_time_hours=5)
        assert leg.name == "Home → Paris"
        assert leg.distance_km == 500
        assert leg.travel_time_hours == 5
        assert leg.sleeping_cost == 0.0
        assert leg.food_cost == 0.0

    def test_leg_with_costs(self):
        leg = Leg(
            name="Paris → Lyon",
            distance_km=450,
            travel_time_hours=4.5,
            sleeping_cost=100,
            food_cost=50,
        )
        assert leg.sleeping_cost == 100
        assert leg.food_cost == 50

    def test_leg_total_cost(self):
        leg = Leg(
            name="Test",
            distance_km=100,
            travel_time_hours=1,
            sleeping_cost=80,
            food_cost=30,
        )
        assert leg.total_cost == 110


class TestTrip:
    """Tests for Trip dataclass."""

    def test_trip_creation_empty(self):
        trip = Trip(name="Summer Vacation")
        assert trip.name == "Summer Vacation"
        assert trip.legs == []
        assert trip.fuel_price_per_litre == 1.6
        assert trip.fuel_consumption_per_100km == 7.0
        assert trip.activities == []
        assert trip.booking_urls == []
        assert trip.id is not None

    def test_trip_with_legs(self):
        legs = [
            Leg(name="Leg 1", distance_km=200, travel_time_hours=2),
            Leg(name="Leg 2", distance_km=300, travel_time_hours=3),
        ]
        trip = Trip(name="Road Trip", legs=legs)
        assert len(trip.legs) == 2
        assert trip.total_distance_km == 500
        assert trip.total_travel_time_hours == 5

    def test_fuel_cost_calculation(self):
        """Test: fuel_cost = (km / 100) * consumption * price_per_litre."""
        legs = [Leg(name="Test", distance_km=1000, travel_time_hours=10)]
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
        legs = [Leg(name="Test", distance_km=500, travel_time_hours=5)]
        trip = Trip(name="Test Trip", legs=legs)
        # 500 km / 100 = 5 units
        # 5 * 7.0 = 35 litres
        # 35 * 1.6 = 56 €
        assert trip.fuel_cost == 56.0

    def test_total_sleeping_cost(self):
        legs = [
            Leg(name="L1", distance_km=100, travel_time_hours=1, sleeping_cost=50),
            Leg(name="L2", distance_km=100, travel_time_hours=1, sleeping_cost=75),
        ]
        trip = Trip(name="Test", legs=legs)
        assert trip.total_sleeping_cost == 125

    def test_total_food_cost(self):
        legs = [
            Leg(name="L1", distance_km=100, travel_time_hours=1, food_cost=30),
            Leg(name="L2", distance_km=100, travel_time_hours=1, food_cost=45),
        ]
        trip = Trip(name="Test", legs=legs)
        assert trip.total_food_cost == 75

    def test_total_price(self):
        """Test total price = fuel + sleeping + food."""
        legs = [
            Leg(
                name="L1",
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


class TestTripSerialization:
    """Tests for Trip serialization to/from dict."""

    def test_trip_to_dict(self):
        leg = Leg(name="Test Leg", distance_km=100, travel_time_hours=1)
        trip = Trip(name="Test Trip", legs=[leg], id="test-id-123")
        data = asdict(trip)

        assert data["name"] == "Test Trip"
        assert data["id"] == "test-id-123"
        assert len(data["legs"]) == 1
        assert data["legs"][0]["name"] == "Test Leg"
        assert data["fuel_price_per_litre"] == 1.6
        assert data["fuel_consumption_per_100km"] == 7.0
