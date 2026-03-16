"""
☕ Chai Tapri Order System - String Basics

Guddu ki chai tapri hai college ke bahar. Customers order dete hain,
aur Guddu ko string methods use karke orders handle karne hain.
Tu Guddu ka helper hai — basic string methods seekh aur orders process kar!

Methods to explore: len(), strip(), upper(), lower(), in, s[0], s[-1]

Functions:

  1. get_chai_order_length(order)
     - Pehle strip() se extra spaces hatao, phir len() se count karo
     - Agar order string nahi hai, return -1
     - Example: get_chai_order_length("  masala chai  ") => 11

  2. shout_chai_order(order)
     - Guddu apne helper ko UPPERCASE mein order shout karta hai
     - Pehle strip() karo, phir upper()
     - Agar order string nahi hai ya strip ke baad empty hai, return ""
     - Example: shout_chai_order("masala chai") => "MASALA CHAI"

  3. whisper_chai_order(order)
     - Jab koi secretly order karta hai, lowercase mein likho
     - Pehle strip() karo, phir lower()
     - Agar order string nahi hai ya strip ke baad empty hai, return ""
     - Example: whisper_chai_order("ADRAK CHAI") => "adrak chai"

  4. has_special_ingredient(order, ingredient)
     - Check karo ki order mein koi special ingredient hai ya nahi
     - Dono ko lower() karo, phir `in` operator use karo
     - Agar koi bhi string nahi hai, return False
     - Example: has_special_ingredient("Elaichi Masala Chai", "elaichi") => True

  5. get_first_and_last_char(order)
     - order[0] se pehla character aur order[-1] se aakhri character nikalo
     - Pehle strip() karo
     - Return: {"first": ..., "last": ...}
     - Agar order string nahi hai ya strip ke baad empty hai, return None
     - Example: get_first_and_last_char("masala chai") => {"first": "m", "last": "i"}

Examples:
  get_chai_order_length("  masala chai  ")  # => 11
  shout_chai_order("masala chai")           # => "MASALA CHAI"
  has_special_ingredient("Elaichi Chai", "elaichi")  # => True
"""


def get_chai_order_length(order):
    # Your code here
    pass


def shout_chai_order(order):
    # Your code here
    pass


def whisper_chai_order(order):
    # Your code here
    pass


def has_special_ingredient(order, ingredient):
    # Your code here
    pass


def get_first_and_last_char(order):
    # Your code here
    pass
