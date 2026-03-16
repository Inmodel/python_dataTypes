"""
🎨 Rangoli Border Maker - String Transform

Diwali aa rahi hai! Priya digital rangoli designs bana rahi hai terminal pe.
String transform methods use karke patterns banana hai.
Tu Priya ki madad kar!

Methods to explore: s * n (repeat), s[start:end] (slice), split(), join(), replace()

Functions:

  1. repeat_pattern(pattern, times)
     - pattern * times use karke pattern ko repeat karo
     - Agar pattern string nahi hai ya times positive integer nahi hai, return ""
     - Example: repeat_pattern("*-", 4) => "*-*-*-*-"

  2. extract_rangoli_center(design, start, end)
     - design[start:end] use karke rangoli ka center part nikalo
     - Agar design string nahi hai, return ""
     - Agar start/end integers nahi hain, return ""
     - Example: extract_rangoli_center("***LOTUS***", 3, 8) => "LOTUS"

  3. split_and_join_rangoli(color_string, old_sep, new_sep)
     - split(old_sep) se tod aur join(new_sep) se jod do
     - Separator change karna hai colors ke beech mein
     - Agar color_string string nahi hai, return ""
     - Example: split_and_join_rangoli("red,blue,green", ",", " | ") => "red | blue | green"

  4. replace_rangoli_color(design, old_color, new_color)
     - replace() use karke ek color ko doosre se replace karo (ALL occurrences)
     - Agar koi bhi param string nahi hai, return ""
     - Example: replace_rangoli_color("red-blue-red-green-red", "red", "pink")
               => "pink-blue-pink-green-pink"

  5. make_rangoli_border(char, length)
     - char ko repeat karke phir slice se exact length ka border banao
     - (char * length)[:length] pattern use karo
     - Agar char string nahi hai ya length positive integer nahi hai, return ""
     - Example: make_rangoli_border("*", 5) => "*****"
     - Example: make_rangoli_border("=-", 7) => "=-=-=-="

Examples:
  repeat_pattern("*-", 4)                    # => "*-*-*-*-"
  extract_rangoli_center("***LOTUS***", 3, 8) # => "LOTUS"
  split_and_join_rangoli("red,blue", ",", "-") # => "red-blue"
"""


def repeat_pattern(pattern, times):
    # Your code here
    pass


def extract_rangoli_center(design, start, end):
    # Your code here
    pass


def split_and_join_rangoli(color_string, old_sep, new_sep):
    # Your code here
    pass


def replace_rangoli_color(design, old_color, new_color):
    # Your code here
    pass


def make_rangoli_border(char, length):
    # Your code here
    pass
