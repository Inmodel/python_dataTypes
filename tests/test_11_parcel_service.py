import pytest
import json
from src.ch11_parcel_service import (
    parse_parcel_json,
    serialize_parcel,
    convert_weight,
    get_tracking_ids,
    build_parcel_summary,
)

PARCEL = {"id": "PKT001", "weight": 2.5, "sender": "Ramesh", "receiver": "Suresh"}
PARCELS = [
    {"id": "PKT001", "weight": 2.5},
    {"id": "PKT002", "weight": 1.0},
    {"weight": 3.0},  # No id — should be skipped
]


class TestParseParcelJson:
    def test_valid_json(self):
        result = parse_parcel_json('{"id": "PKT001", "weight": 2.5}')
        assert result == {"id": "PKT001", "weight": 2.5}

    def test_invalid_json_returns_none(self):
        assert parse_parcel_json("{invalid json}") is None
        assert parse_parcel_json("not json at all") is None

    def test_non_string_returns_none(self):
        assert parse_parcel_json(None) is None
        assert parse_parcel_json(123) is None


class TestSerializeParcel:
    def test_serializes_dict(self):
        result = serialize_parcel({"id": "PKT001"})
        assert json.loads(result) == {"id": "PKT001"}

    def test_non_dict_returns_empty(self):
        assert serialize_parcel(None) == ""
        assert serialize_parcel("not a dict") == ""
        assert serialize_parcel([1, 2]) == ""


class TestConvertWeight:
    def test_valid_float_string(self):
        assert convert_weight("2.5") == 2.5

    def test_integer_string(self):
        assert convert_weight("10") == 10.0

    def test_invalid_string_returns_none(self):
        assert convert_weight("heavy") is None
        assert convert_weight("2.5kg") is None

    def test_non_string_returns_none(self):
        assert convert_weight(None) is None
        assert convert_weight(2.5) is None


class TestGetTrackingIds:
    def test_gets_all_ids(self):
        result = get_tracking_ids([{"id": "PKT001"}, {"id": "PKT002"}])
        assert result == ["PKT001", "PKT002"]

    def test_skips_parcels_without_id(self):
        result = get_tracking_ids(PARCELS)
        assert result == ["PKT001", "PKT002"]

    def test_non_list_returns_empty(self):
        assert get_tracking_ids(None) == []
        assert get_tracking_ids("not a list") == []

    def test_empty_list(self):
        assert get_tracking_ids([]) == []


class TestBuildParcelSummary:
    def test_basic_summary(self):
        result = build_parcel_summary(PARCEL)
        assert result == "Parcel PKT001: 2.5kg from Ramesh to Suresh"

    def test_missing_key_returns_empty(self):
        assert build_parcel_summary({"id": "PKT001", "weight": 2.5}) == ""

    def test_non_dict_returns_empty(self):
        assert build_parcel_summary(None) == ""
        assert build_parcel_summary("not a dict") == ""
