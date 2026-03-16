"""
🚂 Train Coach Finder - List Search

Rohan ka train ticket hai. Use apna coach, seat, aur co-passengers dhundhne hain.
List search methods use karke passengers ki jankaari nikalo.
Tu Rohan ka digital TTE bana! (without black money 😄)

Methods to explore: next() with filter(), list comprehension,
  any(), all(), [x for x in lst if condition]

Data format: passenger = {"name": "Rohan", "coach": "S3", "seat": 42, "has_ticket": True}

Functions:

  1. find_passenger(passengers, name)
     - passengers list mein se name wala passenger dhundho (case-insensitive)
     - Return: first matching passenger dict, ya None agar nahi mila
     - Agar passengers list nahi hai ya name string nahi hai, return None
     - Example: find_passenger([{...}], "rohan") => {"name": "Rohan", ...}

  2. get_coach_passengers(passengers, coach)
     - Ek specific coach ke saare passengers filter karo
     - Return: list of matching passengers
     - Agar passengers list nahi hai ya coach string nahi hai, return []
     - Example: get_coach_passengers([...], "S3") => [{...}, {...}]

  3. has_any_ticketless(passengers)
     - Check karo ki koi bhi passenger ticketless hai (has_ticket == False)
     - any() use karo
     - Agar passengers list nahi hai ya empty hai, return False
     - Example: has_any_ticketless([{..., "has_ticket": False}, ...]) => True

  4. all_have_tickets(passengers)
     - Check karo ki saare passengers ke paas valid ticket hai
     - all() use karo
     - Agar passengers list nahi hai ya empty hai, return False
     - Example: all_have_tickets([{..., "has_ticket": True}, ...]) => True

  5. get_seats_in_coach(passengers, coach)
     - Ek coach ke saare seat numbers nikalo as a sorted list
     - List comprehension use karo + sorted()
     - Agar passengers list nahi hai ya coach string nahi hai, return []
     - Example: get_seats_in_coach([{..., "coach": "S3", "seat": 42}, ...], "S3") => [42]

Examples:
  find_passenger(passengers, "Rohan")          # => {"name": "Rohan", ...}
  get_coach_passengers(passengers, "S3")       # => [{...}, {...}]
  has_any_ticketless(passengers)               # => True/False
"""


def find_passenger(passengers, name):
    # Your code here
    pass


def get_coach_passengers(passengers, coach):
    # Your code here
    pass


def has_any_ticketless(passengers):
    # Your code here
    pass


def all_have_tickets(passengers):
    # Your code here
    pass


def get_seats_in_coach(passengers, coach):
    # Your code here
    pass
