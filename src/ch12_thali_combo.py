"""
🍽️ Thali Combo Platter - Mixed Methods Capstone

Grand Indian Thali restaurant mein combo platter system banana hai.
String, Number, List, aur Dict — sab methods mila ke ek complete
thali banao. Yeh capstone challenge hai — sab kuch combine karo!

Data format:
  thali = {
      "name": "Rajasthani Thali",
      "items": ["dal baati", "churma", "papad"],
      "price": 250,
      "is_veg": True
  }

Functions:

  1. create_thali_description(thali)
     - f-string, join(), upper(), round() use karo
     - Format: "{NAME} (Veg/Non-Veg) - Items: {items joined} - Rs.{price:.2f}"
     - name ko UPPERCASE karo, price 2 decimal places
     - is_veg True => "Veg", False => "Non-Veg"
     - Required fields: name (str), items (list), price (number), is_veg (bool)
     - Agar thali dict nahi hai ya required fields missing hain, return ""
     - Example: create_thali_description({"name":"Rajasthani Thali","items":["dal","churma"],"price":250,"is_veg":True})
               => "RAJASTHANI THALI (Veg) - Items: dal, churma - Rs.250.00"

  2. get_thali_stats(thalis)
     - List of thali dicts ka stats nikalo
     - Veg/Non-veg count (list comprehension + len)
     - Average price (sum + len)
     - min/max price
     - Saare names
     - Return: {"total_thalis": int, "veg_count": int, "non_veg_count": int,
                "avg_price": str (2 decimal), "cheapest": number, "costliest": number, "names": list}
     - Agar thalis list nahi hai ya empty hai, return None

  3. search_thali_menu(thalis, query)
     - List comprehension + lower() + in se search karo (case-insensitive)
     - Thali match karti hai agar name ya koi bhi item query include kare
     - Agar thalis list nahi hai ya query string nahi hai, return []
     - Example: search_thali_menu(thalis, "dal") => thalis with "dal" in name or items

  4. generate_thali_receipt(customer_name, thalis)
     - f-strings + list comprehension + join() + sum() se receipt banao
     - Format:
         "THALI RECEIPT\\n---\\nCustomer: {NAME}\\n{line items}\\n---\\nTotal: Rs.{total:.2f}\\nItems: {count}"
     - Line item format: "- {thali name} x Rs.{price}"
     - customer_name UPPERCASE karo
     - Agar customer_name string nahi hai ya thalis list nahi hai/empty hai, return ""

Examples:
  create_thali_description({"name":"Rajasthani","items":["dal"],"price":250,"is_veg":True})
  # => "RAJASTHANI (Veg) - Items: dal - Rs.250.00"
"""


def create_thali_description(thali):
    # Your code here
    pass


def get_thali_stats(thalis):
    # Your code here
    pass


def search_thali_menu(thalis, query):
    # Your code here
    pass


def generate_thali_receipt(customer_name, thalis):
    # Your code here
    pass
