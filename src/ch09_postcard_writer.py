"""
✉️ Indian Postcard Writer - String Advanced

Sunita apne dost ko postcard likh rahi hai. Postcard ko properly format karna hai —
sahi greeting, padding, alignment, aur content check.
String advanced methods use karke postcard system banao.

Methods to explore: f-strings, startswith(), endswith(), zfill(),
  ljust(), rjust(), center(), strip(), count()

Functions:

  1. format_postcard_address(name, city, pincode)
     - f-string use karke address format karo
     - pincode ko zfill(6) se 6 digits ka banao
     - Format: "To: {name}\\n    {city} - {pincode}"
     - Agar koi bhi string nahi hai, return ""
     - Example: format_postcard_address("Sunita", "Jaipur", "302001")
               => "To: Sunita\\n    Jaipur - 302001"

  2. add_postcard_border(message, width)
     - Message ko center mein rakhao aur dono taraf "-" se padding karo
     - message.center(width, "-") use karo
     - Agar message string nahi hai ya width positive integer nahi hai, return ""
     - Example: add_postcard_border("Namaste!", 20) => "------Namaste!------"

  3. is_valid_greeting(message)
     - Check karo ki message "Namaste" ya "Dear" se start hota hai
     - startswith() use karo with a tuple of prefixes
     - Agar message string nahi hai, return False
     - Example: is_valid_greeting("Namaste Sunita!") => True
     - Example: is_valid_greeting("Hey!") => False

  4. has_proper_closing(message)
     - Check karo ki message "Yours truly," ya "Aapka," ya "Shubhkamnao," se end hota hai
     - endswith() use karo
     - Agar message string nahi hai, return False
     - Example: has_proper_closing("...Aapka,") => True

  5. format_stamp_number(number)
     - Stamp number ko exactly 8 digits ka banao using zfill()
     - str() se pehle convert karo, phir zfill(8)
     - Agar number integer nahi hai ya negative hai, return ""
     - Example: format_stamp_number(12345) => "00012345"

  6. count_words(message)
     - Message mein words count karo
     - split() use karo (automatically handles multiple spaces)
     - Agar message string nahi hai ya empty/whitespace hai, return 0
     - Example: count_words("Jai Hind Vande Mataram") => 4

Examples:
  format_postcard_address("Sunita", "Jaipur", "302001")  # => "To: Sunita\\n    Jaipur - 302001"
  add_postcard_border("Namaste!", 20)                     # => "------Namaste!------"
  format_stamp_number(12345)                              # => "00012345"
"""


def format_postcard_address(name, city, pincode):
    # Your code here
    pass


def add_postcard_border(message, width):
    # Your code here
    pass


def is_valid_greeting(message):
    # Your code here
    pass


def has_proper_closing(message):
    # Your code here
    pass


def format_stamp_number(number):
    # Your code here
    pass


def count_words(message):
    # Your code here
    pass
