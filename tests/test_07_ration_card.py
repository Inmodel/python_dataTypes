import pytest
from src.ch07_ration_card import (
    get_all_card_numbers,
    get_beneficiary_names,
    get_card_details,
    add_or_update_card,
    remove_card,
    count_by_category,
)

REGISTRY = {
    "RAJ001": {"name": "Ramesh", "members": 4, "category": "BPL"},
    "RAJ002": {"name": "Suresh", "members": 3, "category": "APL"},
    "RAJ003": {"name": "Anita", "members": 5, "category": "BPL"},
}


class TestGetAllCardNumbers:
    def test_returns_all_keys(self):
        result = get_all_card_numbers(REGISTRY)
        assert set(result) == {"RAJ001", "RAJ002", "RAJ003"}

    def test_empty_registry(self):
        assert get_all_card_numbers({}) == []

    def test_non_dict_returns_empty(self):
        assert get_all_card_numbers(None) == []
        assert get_all_card_numbers("not a dict") == []


class TestGetBeneficiaryNames:
    def test_returns_all_names(self):
        result = get_beneficiary_names(REGISTRY)
        assert set(result) == {"Ramesh", "Suresh", "Anita"}

    def test_empty_registry(self):
        assert get_beneficiary_names({}) == []

    def test_non_dict_returns_empty(self):
        assert get_beneficiary_names(None) == []


class TestGetCardDetails:
    def test_finds_card(self):
        result = get_card_details(REGISTRY, "RAJ001")
        assert result == {"name": "Ramesh", "members": 4, "category": "BPL"}

    def test_missing_card_returns_none(self):
        assert get_card_details(REGISTRY, "RAJ999") is None

    def test_non_dict_returns_none(self):
        assert get_card_details(None, "RAJ001") is None

    def test_non_string_card_number_returns_none(self):
        assert get_card_details(REGISTRY, 123) is None


class TestAddOrUpdateCard:
    def test_adds_new_card(self):
        reg = dict(REGISTRY)
        result = add_or_update_card(reg, "RAJ004", {"name": "Mohan", "members": 2, "category": "APL"})
        assert "RAJ004" in result

    def test_updates_existing_card(self):
        reg = dict(REGISTRY)
        new_details = {"name": "Ramesh", "members": 6, "category": "BPL"}
        result = add_or_update_card(reg, "RAJ001", new_details)
        assert result["RAJ001"]["members"] == 6

    def test_non_dict_registry_returns_empty(self):
        assert add_or_update_card(None, "RAJ001", {}) == {}

    def test_invalid_card_number_returns_unchanged(self):
        reg = dict(REGISTRY)
        result = add_or_update_card(reg, 123, {"name": "X"})
        assert result == reg


class TestRemoveCard:
    def test_removes_existing_card(self):
        reg = dict(REGISTRY)
        result = remove_card(reg, "RAJ001")
        assert result == {"name": "Ramesh", "members": 4, "category": "BPL"}
        assert "RAJ001" not in reg

    def test_missing_card_returns_none(self):
        reg = dict(REGISTRY)
        assert remove_card(reg, "RAJ999") is None

    def test_non_dict_returns_none(self):
        assert remove_card(None, "RAJ001") is None

    def test_non_string_card_number_returns_none(self):
        assert remove_card(REGISTRY, 123) is None


class TestCountByCategory:
    def test_counts_categories(self):
        result = count_by_category(REGISTRY)
        assert result == {"BPL": 2, "APL": 1}

    def test_empty_registry(self):
        assert count_by_category({}) == {}

    def test_non_dict_returns_empty(self):
        assert count_by_category(None) == {}
