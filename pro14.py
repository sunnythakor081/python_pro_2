import re

text = """
Hello, I am Dr. Mobile123. Please call me in case of an emergency. My phone number is
99405 33241. Otherwise, you can call my assistant at 8932732436. I am available at my
clinic from 9 to 1. For appointments, call the reception at (687) 324-3232.
"""

digits10 = r'\d{10}' 
digits55 = r'\d{5}\D\d{5}' 
digitsus = r'\(\d{3}\)\s?\d{3}\D\d{4}' 

regex = digits10 + '|' + digits55 + '|' + digitsus
mobiles = re.findall(regex, text)
print(mobiles)
