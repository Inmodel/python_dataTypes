import pytest
from src.ch05_train_coach import (
    find_passenger,
    get_coach_passengers,
    has_any_ticketless,
    all_have_tickets,
    get_seats_in_coach,
)

PASSENGERS = [
    {"name": "Rohan", "coach": "S3", "seat": 42, "has_ticket": True},
    {"name": "Priya", "coach": "S3", "seat": 15, "has_ticket": True},
    {"name": "Suresh", "coach": "B2", "seat": 7, "has_ticket": False},
    {"name": "Anita", "coach": "B2", "seat": 22, "has_ticket": True},
]


class TestFindPassenger:
    def test_finds_by_name(self):
        result = find_passenger(PASSENGERS, "Rohan")
        assert result is not None
        assert result["name"] == "Rohan"

    def test_case_insensitive(self):
        result = find_passenger(PASSENGERS, "rohan")
        assert result is not None
        assert result["name"] == "Rohan"

    def test_not_found_returns_none(self):
        assert find_passenger(PASSENGERS, "Ramesh") is None

    def test_non_list_returns_none(self):
        assert find_passenger(None, "Rohan") is None
        assert find_passenger("not a list", "Rohan") is None

    def test_non_string_name_returns_none(self):
        assert find_passenger(PASSENGERS, 123) is None


class TestGetCoachPassengers:
    def test_gets_passengers_in_coach(self):
        result = get_coach_passengers(PASSENGERS, "S3")
        assert len(result) == 2
        assert all(p["coach"] == "S3" for p in result)

    def test_no_passengers_in_coach(self):
        result = get_coach_passengers(PASSENGERS, "A1")
        assert result == []

    def test_non_list_returns_empty(self):
        assert get_coach_passengers(None, "S3") == []
        assert get_coach_passengers("not a list", "S3") == []

    def test_non_string_coach_returns_empty(self):
        assert get_coach_passengers(PASSENGERS, 123) == []


class TestHasAnyTicketless:
    def test_has_ticketless_passenger(self):
        assert has_any_ticketless(PASSENGERS) is True

    def test_all_have_tickets(self):
        ticketed = [p for p in PASSENGERS if p["has_ticket"]]
        assert has_any_ticketless(ticketed) is False

    def test_non_list_returns_false(self):
        assert has_any_ticketless(None) is False
        assert has_any_ticketless("not a list") is False

    def test_empty_list_returns_false(self):
        assert has_any_ticketless([]) is False


class TestAllHaveTickets:
    def test_all_have_tickets(self):
        ticketed = [p for p in PASSENGERS if p["has_ticket"]]
        assert all_have_tickets(ticketed) is True

    def test_some_missing_tickets(self):
        assert all_have_tickets(PASSENGERS) is False

    def test_non_list_returns_false(self):
        assert all_have_tickets(None) is False

    def test_empty_list_returns_false(self):
        assert all_have_tickets([]) is False


class TestGetSeatsInCoach:
    def test_gets_sorted_seats(self):
        result = get_seats_in_coach(PASSENGERS, "S3")
        assert result == [15, 42]

    def test_empty_coach(self):
        assert get_seats_in_coach(PASSENGERS, "A1") == []

    def test_non_list_returns_empty(self):
        assert get_seats_in_coach(None, "S3") == []

    def test_non_string_coach_returns_empty(self):
        assert get_seats_in_coach(PASSENGERS, 123) == []
