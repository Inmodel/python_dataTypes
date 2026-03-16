"""
📋 Ration Card Registry - Dict Basics

Gram panchayat mein ration card registry hai. Officials ko records manage karne hain.
Dict methods use karke registry system banao.
Tu gram sevak ka digital assistant bana!

Methods to explore: .keys(), .values(), .items(), .get(), del, .update(), in

Data format: registry = {"RAJ001": {"name": "Ramesh", "members": 4, "category": "BPL"}}

Functions:

  1. get_all_card_numbers(registry)
     - Registry ke saare card numbers (keys) return karo as a list
     - list(registry.keys()) use karo
     - Agar registry dict nahi hai, return []
     - Example: get_all_card_numbers({"RAJ001": {...}}) => ["RAJ001"]

  2. get_beneficiary_names(registry)
     - Saare beneficiaries ke names return karo as a list
     - .values() se iterate karo
     - Agar registry dict nahi hai, return []
     - Example: get_beneficiary_names({"RAJ001": {"name": "Ramesh", ...}}) => ["Ramesh"]

  3. get_card_details(registry, card_number)
     - Ek specific card ka details return karo
     - .get() use karo (KeyError avoid karne ke liye)
     - Agar registry dict nahi hai ya card_number string nahi hai, return None
     - Agar card nahi mila, return None
     - Example: get_card_details(registry, "RAJ001") => {"name": "Ramesh", ...}

  4. add_or_update_card(registry, card_number, details)
     - Registry mein ek naya card add karo ya existing update karo
     - Return: updated registry
     - Agar registry dict nahi hai, return {}
     - Agar card_number string nahi hai ya details dict nahi hai, return registry unchanged
     - Example: add_or_update_card(registry, "RAJ002", {"name": "Suresh", "members": 3})

  5. remove_card(registry, card_number)
     - Registry se ek card remove karo using del
     - Return: the removed card details, ya None agar card nahi mila
     - Agar registry dict nahi hai ya card_number string nahi hai, return None
     - Example: remove_card(registry, "RAJ001") => {"name": "Ramesh", ...}

  6. count_by_category(registry)
     - Categories ke hisaab se cards count karo
     - Return: dict like {"BPL": 2, "APL": 3}
     - Agar registry dict nahi hai ya empty hai, return {}
     - Example: count_by_category({"RAJ001": {"category": "BPL"}, ...}) => {"BPL": 1}

Examples:
  get_all_card_numbers(registry)           # => ["RAJ001", "RAJ002"]
  get_card_details(registry, "RAJ001")     # => {"name": "Ramesh", ...}
  count_by_category(registry)              # => {"BPL": 2, "APL": 1}
"""


def get_all_card_numbers(registry):
    # Your code here
    pass


def get_beneficiary_names(registry):
    # Your code here
    pass


def get_card_details(registry, card_number):
    # Your code here
    pass


def add_or_update_card(registry, card_number, details):
    # Your code here
    pass


def remove_card(registry, card_number):
    # Your code here
    pass


def count_by_category(registry):
    # Your code here
    pass
