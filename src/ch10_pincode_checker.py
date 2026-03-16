"""
📮 Pincode Type Checker - Type Checking

India Post ka system hai. Pincodes aur data validate karna hai.
Type checking methods use karke sahi data ensure karo.

Methods to explore: isinstance(), type(), int, str, float, bool, list, dict,
  type(x).__name__, int.bit_length() nahi — sirf isinstance use karo!

Functions:

  1. check_pincode_type(pincode)
     - Pincode ka type batao as a string
     - Return: "int", "str", "float", "bool", "list", "dict", or "unknown"
     - isinstance() use karo (bool check MUST come before int — bool is subclass of int!)
     - Example: check_pincode_type(110001) => "int"
     - Example: check_pincode_type("110001") => "str"
     - Example: check_pincode_type(True) => "bool"

  2. is_valid_pincode(pincode)
     - Valid pincode: int hai, 100000 aur 999999 ke beech hai
     - isinstance(pincode, int) use karo (bool accept mat karo — isinstance(pincode, bool) check karo)
     - Return: True ya False
     - Example: is_valid_pincode(110001) => True
     - Example: is_valid_pincode("110001") => False
     - Example: is_valid_pincode(True) => False  (bool nahi chalega)

  3. is_valid_name(name)
     - Valid name: non-empty string
     - isinstance() use karo
     - Return: True ya False
     - Example: is_valid_name("Ramesh") => True
     - Example: is_valid_name("") => False
     - Example: is_valid_name(123) => False

  4. is_valid_address(address)
     - Valid address: dict hai aur required keys hain: "street", "city", "pincode"
     - isinstance() + `in` operator use karo
     - Return: True ya False
     - Example: is_valid_address({"street": "MG Road", "city": "Delhi", "pincode": 110001}) => True
     - Example: is_valid_address({"street": "MG Road"}) => False  (city aur pincode missing)

  5. normalize_pincode(pincode)
     - Agar pincode string hai aur valid digits hain, int mein convert karo
     - Agar already int hai (aur bool nahi), return as-is
     - Agar conversion nahi ho sakti, return None
     - isinstance() + int() + try/except use karo
     - Example: normalize_pincode("110001") => 110001
     - Example: normalize_pincode(110001) => 110001
     - Example: normalize_pincode("abcdef") => None
     - Example: normalize_pincode(True) => None

Examples:
  check_pincode_type(110001)    # => "int"
  check_pincode_type("110001")  # => "str"
  is_valid_pincode(110001)      # => True
  normalize_pincode("302001")   # => 302001
"""


def check_pincode_type(pincode):
    # Your code here
    pass


def is_valid_pincode(pincode):
    # Your code here
    pass


def is_valid_name(name):
    # Your code here
    pass


def is_valid_address(address):
    # Your code here
    pass


def normalize_pincode(pincode):
    # Your code here
    pass
