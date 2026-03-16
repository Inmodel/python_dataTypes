"""
📦 Dak Ghar Parcel Service - JSON & Conversion

Dak Ghar ka parcel tracking system hai. Data ko JSON mein store karna hai
aur ek format se doosre mein convert karna hai.
JSON aur type conversion methods use karke parcel system banao.

Methods to explore: json.loads(), json.dumps(), str(), int(), float(),
  list(), dict(), json.JSONDecodeError

import json  # zaroor karo!

Functions:

  1. parse_parcel_json(json_string)
     - JSON string ko Python dict mein convert karo using json.loads()
     - Agar json_string string nahi hai ya invalid JSON hai, return None
     - json.JSONDecodeError catch karo
     - Example: parse_parcel_json('{"id": "PKT001", "weight": 2.5}')
               => {"id": "PKT001", "weight": 2.5}

  2. serialize_parcel(parcel)
     - Python dict ko JSON string mein convert karo using json.dumps()
     - Agar parcel dict nahi hai, return ""
     - Example: serialize_parcel({"id": "PKT001", "weight": 2.5})
               => '{"id": "PKT001", "weight": 2.5}'

  3. convert_weight(weight_str)
     - Weight string (like "2.5") ko float mein convert karo
     - Agar conversion fail ho, return None
     - Example: convert_weight("2.5") => 2.5
     - Example: convert_weight("heavy") => None

  4. get_tracking_ids(parcels)
     - List of parcel dicts se tracking IDs list banao
     - list comprehension use karo
     - Agar parcels list nahi hai, return []
     - Har parcel se "id" field lo; agar nahi hai toh skip karo
     - Example: get_tracking_ids([{"id": "PKT001"}, {"id": "PKT002"}]) => ["PKT001", "PKT002"]

  5. build_parcel_summary(parcel)
     - Dict se human-readable summary string banao using str() and f-strings
     - Format: "Parcel {id}: {weight}kg from {sender} to {receiver}"
     - Required keys: "id", "weight", "sender", "receiver"
     - Agar parcel dict nahi hai ya keys missing hain, return ""
     - Example: build_parcel_summary({"id": "PKT001", "weight": 2.5, "sender": "Ramesh", "receiver": "Suresh"})
               => "Parcel PKT001: 2.5kg from Ramesh to Suresh"

Examples:
  parse_parcel_json('{"id": "PKT001"}')  # => {"id": "PKT001"}
  serialize_parcel({"id": "PKT001"})     # => '{"id": "PKT001"}'
  convert_weight("2.5")                  # => 2.5
"""
import json


def parse_parcel_json(json_string):
    # Your code here
    pass


def serialize_parcel(parcel):
    # Your code here
    pass


def convert_weight(weight_str):
    # Your code here
    pass


def get_tracking_ids(parcels):
    # Your code here
    pass


def build_parcel_summary(parcel):
    # Your code here
    pass
