import sys
import logging
logging.basicConfig(level=logging.DEBUG)

items = {"Name": ["хліб", "булка ", "пончик", "шоколад"],
  "Quantity": [50, 24, 12, 15], "Unit": ["шт", "шт", "шт", "шт"], "Unit Price (PLN)": [3.25, 0.33, 1.99, 3.99]}
def get_items():
  keys = items.keys()
  print("\t".join(keys))
  values = items.values()
  
action = input("What would you like to do?")
if action == "exit":
 logging.info("Exiting...Bye!")
if action == "show":
 get_items()