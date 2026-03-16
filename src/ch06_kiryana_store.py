"""
🏪 Kiryana Store Bill - List Transform

Sharma ji ka kiryana store hai. Customers ka bill banana hai.
List transform methods use karke billing system banao.
Tu Sharma ji ka digital cashier bana!

Methods to explore: list comprehension, map(), filter(), sorted(),
  sum(), zip(), round()

Data format: item = {"name": "atta", "price": 50, "qty": 2, "category": "grocery"}

Functions:

  1. get_item_totals(items)
     - Har item ka total = price * qty calculate karo
     - Return: list of {"name": ..., "total": ...} dicts
     - List comprehension ya map() use karo
     - Agar items list nahi hai, return []
     - Example: get_item_totals([{"name": "atta", "price": 50, "qty": 2}])
               => [{"name": "atta", "total": 100}]

  2. get_expensive_items(items, threshold)
     - Sirf woh items return karo jinka price >= threshold hai
     - filter() ya list comprehension use karo
     - Agar items list nahi hai ya threshold number nahi hai, return []
     - Example: get_expensive_items([...], 100) => items where price >= 100

  3. calculate_total_bill(items)
     - Saare items ka grand total nikalo (price * qty)
     - sum() use karo
     - round() se 2 decimal places tak
     - Agar items list nahi hai ya empty hai, return 0.0
     - Example: calculate_total_bill([{"price": 50, "qty": 2}, {"price": 30, "qty": 3}]) => 190.0

  4. sort_by_price(items, ascending=True)
     - Items ko price ke hisaab se sort karo
     - sorted() use karo with key parameter
     - ascending=True means lowest price first
     - Agar items list nahi hai, return []
     - Example: sort_by_price([...]) => sorted list

  5. apply_tax(items, tax_percent)
     - Har item ke total pe tax lagao
     - Return: list of {"name": ..., "total_with_tax": ...} dicts
     - round() se 2 decimal places
     - Agar items list nahi hai ya tax_percent number nahi hai, return []
     - Example: apply_tax([{"name": "atta", "price": 50, "qty": 2}], 10)
               => [{"name": "atta", "total_with_tax": 110.0}]

Examples:
  get_item_totals([{"name": "atta", "price": 50, "qty": 2}])  # => [{"name": "atta", "total": 100}]
  calculate_total_bill([{"price": 50, "qty": 2}])              # => 100.0
  get_expensive_items(items, 100)                              # => filtered list
"""


def get_item_totals(items):
    # Your code here
    pass


def get_expensive_items(items, threshold):
    # Your code here
    pass


def calculate_total_bill(items):
    # Your code here
    pass


def sort_by_price(items, ascending=True):
    # Your code here
    pass


def apply_tax(items, tax_percent):
    # Your code here
    pass
