"""
🥬 Sabzi Mandi Shopping Cart - List Basics

Amma sabzi mandi gayi hain. Unka shopping cart (list) hai.
Items add karna, remove karna, check karna — sab list basic methods se.
Tu Amma ka digital thela bana!

Methods to explore: append(), pop(), insert(), index(), in, len(), +

Functions:

  1. add_to_cart(cart, item)
     - append() se item ko cart ke end mein add karo
     - Return: new cart length (len(cart) after adding)
     - Agar cart list nahi hai, return -1
     - Agar item empty string hai ya string nahi hai, return len(cart) without adding
     - Example: add_to_cart(["tamatar", "pyaaz"], "mirchi") => 3

  2. add_urgent_item(cart, item)
     - insert(0, item) se item ko cart ke BEGINNING mein add karo
     - Return: updated cart list
     - Agar cart not list, return []
     - Agar item valid string nahi hai, return cart unchanged
     - Example: add_urgent_item(["pyaaz", "mirchi"], "dhaniya") => ["dhaniya", "pyaaz", "mirchi"]

  3. remove_last_item(cart)
     - pop() se last sabzi remove karo
     - Return: the removed item
     - Agar cart not list ya empty hai, return None
     - Example: remove_last_item(["tamatar", "pyaaz", "mirchi"]) => "mirchi"

  4. is_in_cart(cart, item)
     - `in` operator se check karo ki item cart mein hai ya nahi
     - Agar cart not list, return False
     - Example: is_in_cart(["tamatar", "pyaaz"], "pyaaz") => True
     - Example: is_in_cart(["tamatar", "pyaaz"], "mirchi") => False

  5. merge_carts(cart1, cart2)
     - + operator se do carts ko combine karo
     - Return: new merged list
     - Agar koi bhi list nahi hai, usse empty list [] maan lo
     - Example: merge_carts(["tamatar"], ["mirchi", "adrak"]) => ["tamatar", "mirchi", "adrak"]

Examples:
  add_to_cart(["tamatar", "pyaaz"], "mirchi")        # => 3
  add_urgent_item(["pyaaz"], "dhaniya")              # => ["dhaniya", "pyaaz"]
  remove_last_item(["tamatar", "pyaaz", "mirchi"])   # => "mirchi"
"""


def add_to_cart(cart, item):
    # Your code here
    pass


def add_urgent_item(cart, item):
    # Your code here
    pass


def remove_last_item(cart):
    # Your code here
    pass


def is_in_cart(cart, item):
    # Your code here
    pass


def merge_carts(cart1, cart2):
    # Your code here
    pass
