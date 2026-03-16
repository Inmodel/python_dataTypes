import pytest
from src.ch12_thali_combo import (
    create_thali_description,
    get_thali_stats,
    search_thali_menu,
    generate_thali_receipt,
)

THALIS = [
    {"name": "Rajasthani Thali", "items": ["dal baati", "churma", "papad"], "price": 250, "is_veg": True},
    {"name": "Punjabi Thali", "items": ["dal makhani", "naan", "lassi"], "price": 350, "is_veg": True},
    {"name": "Hyderabadi Thali", "items": ["biryani", "raita", "haleem"], "price": 400, "is_veg": False},
]


class TestCreateThaliDescription:
    def test_basic_veg_thali(self):
        thali = {"name": "Rajasthani Thali", "items": ["dal", "churma"], "price": 250, "is_veg": True}
        result = create_thali_description(thali)
        assert result == "RAJASTHANI THALI (Veg) - Items: dal, churma - Rs.250.00"

    def test_non_veg_thali(self):
        thali = {"name": "Hyderabadi Thali", "items": ["biryani"], "price": 400, "is_veg": False}
        result = create_thali_description(thali)
        assert "Non-Veg" in result

    def test_name_is_uppercase(self):
        thali = {"name": "simple thali", "items": ["dal"], "price": 100, "is_veg": True}
        result = create_thali_description(thali)
        assert "SIMPLE THALI" in result

    def test_price_has_2_decimals(self):
        thali = {"name": "Thali", "items": ["dal"], "price": 150, "is_veg": True}
        result = create_thali_description(thali)
        assert "150.00" in result

    def test_non_dict_returns_empty(self):
        assert create_thali_description(None) == ""
        assert create_thali_description("not a dict") == ""

    def test_missing_required_fields_returns_empty(self):
        assert create_thali_description({"name": "Thali"}) == ""


class TestGetThaliStats:
    def test_basic_stats(self):
        result = get_thali_stats(THALIS)
        assert result["total_thalis"] == 3
        assert result["veg_count"] == 2
        assert result["non_veg_count"] == 1
        assert result["cheapest"] == 250
        assert result["costliest"] == 400
        assert set(result["names"]) == {"Rajasthani Thali", "Punjabi Thali", "Hyderabadi Thali"}

    def test_avg_price_as_string(self):
        result = get_thali_stats(THALIS)
        assert isinstance(result["avg_price"], str)
        assert result["avg_price"] == "333.33"

    def test_non_list_returns_none(self):
        assert get_thali_stats(None) is None
        assert get_thali_stats("not a list") is None

    def test_empty_list_returns_none(self):
        assert get_thali_stats([]) is None


class TestSearchThaliMenu:
    def test_search_in_name(self):
        result = search_thali_menu(THALIS, "rajasthani")
        assert len(result) == 1
        assert result[0]["name"] == "Rajasthani Thali"

    def test_search_in_items(self):
        result = search_thali_menu(THALIS, "dal")
        names = [t["name"] for t in result]
        assert "Rajasthani Thali" in names
        assert "Punjabi Thali" in names

    def test_case_insensitive(self):
        result = search_thali_menu(THALIS, "BIRYANI")
        assert len(result) == 1

    def test_no_match_returns_empty(self):
        assert search_thali_menu(THALIS, "pizza") == []

    def test_non_list_returns_empty(self):
        assert search_thali_menu(None, "dal") == []

    def test_non_string_query_returns_empty(self):
        assert search_thali_menu(THALIS, 123) == []


class TestGenerateThaliReceipt:
    def test_basic_receipt(self):
        result = generate_thali_receipt("Rohan", [THALIS[0]])
        assert "ROHAN" in result
        assert "THALI RECEIPT" in result
        assert "Rajasthani Thali" in result
        assert "250" in result

    def test_total_in_receipt(self):
        result = generate_thali_receipt("Priya", [THALIS[0], THALIS[1]])
        assert "600.00" in result
        assert "Items: 2" in result

    def test_customer_name_uppercase(self):
        result = generate_thali_receipt("sunita", [THALIS[0]])
        assert "SUNITA" in result

    def test_non_string_customer_returns_empty(self):
        assert generate_thali_receipt(None, THALIS) == ""
        assert generate_thali_receipt(123, THALIS) == ""

    def test_non_list_thalis_returns_empty(self):
        assert generate_thali_receipt("Rohan", None) == ""

    def test_empty_thalis_returns_empty(self):
        assert generate_thali_receipt("Rohan", []) == ""
