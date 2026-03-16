"""
🛺 Auto Rickshaw Fare Calculator - Number & Math

Raju rickshaw wala hai. Passengers ka fare calculate karna hai.
Number aur math functions use karke sahi fare nikalo.
Tu Raju ka digital meter bana!

Methods to explore: int(), float(), round(), abs(), math.ceil(),
  max(), min()

import math  # zaroor karo!

Functions:

  1. parse_distance(distance_str)
     - string ko float mein convert karo using float()
     - Agar conversion fail ho (ValueError), return -1.0
     - Example: parse_distance("12.5") => 12.5
     - Example: parse_distance("abcd") => -1.0

  2. calculate_fare(distance, rate_per_km)
     - distance * rate_per_km calculate karo
     - math.ceil() se upar round karo (rickshaw wala always rounds up!)
     - Agar distance ya rate_per_km number nahi hai, return -1
     - Agar distance ya rate_per_km negative hai, return -1
     - Example: calculate_fare(3.2, 10) => 32  (math.ceil(32.0))
     - Example: calculate_fare(3.5, 10) => 35

  3. apply_discount(fare, discount_percent)
     - fare pe discount_percent wala discount lagao
     - discounted = fare - (fare * discount_percent / 100)
     - round() se 2 decimal places tak karo
     - Agar fare ya discount_percent number nahi hai, return -1
     - Agar discount_percent 0 se 100 ke beech nahi hai, return -1
     - Example: apply_discount(100, 10) => 90.0

  4. get_fare_range(fares)
     - list of fares mein se min aur max nikalo
     - Return: {"min": ..., "max": ...}
     - Agar fares list nahi hai ya empty hai, return None
     - Example: get_fare_range([50, 30, 80, 20]) => {"min": 20, "max": 80}

  5. get_absolute_difference(fare1, fare2)
     - do fares ka absolute difference nikalo using abs()
     - Agar koi bhi number nahi hai, return -1
     - Example: get_absolute_difference(80, 50) => 30
     - Example: get_absolute_difference(50, 80) => 30

Examples:
  parse_distance("12.5")               # => 12.5
  calculate_fare(3.2, 10)              # => 32
  get_fare_range([50, 30, 80])         # => {"min": 30, "max": 80}
"""
import math


def parse_distance(distance_str):
    # Your code here
    pass


def calculate_fare(distance, rate_per_km):
    # Your code here
    pass


def apply_discount(fare, discount_percent):
    # Your code here
    pass


def get_fare_range(fares):
    # Your code here
    pass


def get_absolute_difference(fare1, fare2):
    # Your code here
    pass
