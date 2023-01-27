from faker import Faker
fake = Faker()

from random import randint

class Card:
    def __init__(self, name, company, position, email):
     self.name = name
     self.company = company
     self.position = position
     self.email = email
     
    @property 
    def label_length(self):
     return len(self.name) - 1
   
class BaseContact(Card):
    def __init__(self, name, phone_number, email):
       Card.__init__(self, name = name, email = email, company = None, position = None)
       self.phone_number = phone_number
       
    def __str__(self):
     return f'{self.name} {self.phone_number} {self.label_length}'
    
    def contact(self):
     print(f"Я набираю {self.phone_number} і телефоную {self.name} {self.label_length}") 
       
class BusinessContact(Card):
    def __init__(self, name, position, company, job_phone_number):
       Card.__init__(self, name = name, position = position, company = company, email = None)
       self.job_phone_number = job_phone_number 
       
    def __str__(self):
     return f'{self.name} {self.position} {self.company} {self.job_phone_number} {self.label_length} ' 
       
    def contact(self):
     print(f"Я набираю {self.job_phone_number} і телефоную {self.position} {self.name} {self.label_length}") 


def add():
  card = BaseContact(fake.name(), fake.phone_number(), fake.email())
  card.contact()
 
def add_business():
  card = BusinessContact(fake.name(), fake.job(), fake.company(), fake.phone_number())
  card.contact()


def create_contacts():
 while True: 
  number = int(input("How many card would you like to print?"))
  for j in range(randint(1, number)):  
   add()
  for i in range(number - j - 1):
   add_business()
      
create_contacts()