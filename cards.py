from faker import Faker
fake = Faker()

class CARD:
    def __init__(self, name, company, position, email):
     self.name = name
     self.company = company
     self.position = position
     self.email = email
   
class BaseContact(CARD):
    def __init__(self, name, phone_number, email):
       CARD.__init__(self, name = name, email = email, company = None, position = None)
       self.phone_number = phone_number
       
    @property
    def label_length(self):
     return len(self.name) - 1 
 
    def __str__(self):
     return f'{self.name} {self.phone_number} {self.label_length}'
    
    def contact(self):
     print(f"Я набираю {self.phone_number} і телефоную {self.name} {self.label_length}") 
       
class BusinessContact(CARD):
    def __init__(self, name, position, company, phone_number):
       CARD.__init__(self, name = name, position = position, company = company, email = None)
       self.phone_number = phone_number 
       
    @property
    def label_length(self):
     return len(self.name) - 1 
   
    def __str__(self):
     return f'{self.name} {self.position} {self.company} {self.phone_number} {self.label_length} ' 
       
    def contact_business(self):
     print(f"Я набираю {self.phone_number} і телефоную {self.position} {self.name} {self.label_length}") 


def add():
  card = BaseContact(fake.name(), fake.phone_number(), fake.email())
  card.contact()
 
def add_business():
  card = BusinessContact(fake.name(), fake.job(), fake.company(), fake.phone_number())
  card.contact_business()


def create_contacts():
 while True:
  card_type = input("What type of card would you like to print? base or business?")
  if card_type != "base" and card_type != "business":
     exit(1)
  number = int(input("How many card would you like to print?"))
  if number < 0 :
     exit(1)
  if card_type == "base":
   for i in range(number):
    add() 
  elif card_type == "business":
   for i in range(number):  
    add_business()
   
create_contacts()