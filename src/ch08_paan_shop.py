"""
🌿 Paan Shop Menu - Dict Transform

Munnabhai ka paan shop hai. Menu manage karna hai — naye items add karna,
prices update karna, special offers banana.
Dict transform methods use karke menu system banao.

Methods to explore: dict comprehension, .update(), .copy(), {**d1, **d2} merge,
  .items(), {k: v for k, v in ...}

Data format: menu = {"sada paan": 10, "meetha paan": 20, "banarasi paan": 50}

Functions:

  1. apply_price_hike(menu, percent)
     - Har item ki price pe percent wala hike lagao
     - Dict comprehension use karo: {k: round(v * (1 + percent/100), 2) for ...}
     - Agar menu dict nahi hai ya percent number nahi hai, return {}
     - Agar percent negative hai, return {}
     - Example: apply_price_hike({"sada": 10}, 10) => {"sada": 11.0}

  2. filter_menu_by_price(menu, max_price)
     - Sirf woh items rakhao jinka price <= max_price hai
     - Dict comprehension use karo
     - Agar menu dict nahi hai ya max_price number nahi hai, return {}
     - Example: filter_menu_by_price({"sada": 10, "banarasi": 50}, 20) => {"sada": 10}

  3. merge_menus(base_menu, special_menu)
     - Do menus ko merge karo. special_menu ke items override karein base_menu ko
     - {**base_menu, **special_menu} ya | operator use karo
     - Agar koi bhi dict nahi hai, usse {} maan lo
     - Return: merged dict
     - Example: merge_menus({"sada": 10}, {"banarasi": 50}) => {"sada": 10, "banarasi": 50}

  4. get_menu_copy(menu)
     - Menu ki ek shallow copy return karo using .copy()
     - Agar menu dict nahi hai, return {}
     - Example: get_menu_copy({"sada": 10}) => {"sada": 10}  (new object)

  5. invert_menu(menu)
     - Menu ko invert karo: prices as keys, names as values
     - Dict comprehension use karo: {v: k for k, v in menu.items()}
     - Agar menu dict nahi hai, return {}
     - Note: Agar same price ke multiple items hain, last one hi rahega
     - Example: invert_menu({"sada paan": 10, "meetha paan": 20}) => {10: "sada paan", 20: "meetha paan"}

Examples:
  apply_price_hike({"sada": 10, "meetha": 20}, 10)  # => {"sada": 11.0, "meetha": 22.0}
  filter_menu_by_price({"sada": 10, "banarasi": 50}, 20)  # => {"sada": 10}
  merge_menus({"sada": 10}, {"banarasi": 50, "sada": 15})  # => {"sada": 15, "banarasi": 50}
"""


def apply_price_hike(menu, percent):
    # Your code here
    pass


def filter_menu_by_price(menu, max_price):
    # Your code here
    pass


def merge_menus(base_menu, special_menu):
    # Your code here
    pass


def get_menu_copy(menu):
    # Your code here
    pass


def invert_menu(menu):
    # Your code here
    pass
