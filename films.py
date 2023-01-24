class Film:
    def __init__(self, name, year_graduate, genre, number_view):
     self.name = name
     self.year_graduate = year_graduate
     self.genre = genre
     self.number_view = number_view
     
    def play(self):
     self.number_view += 1
     
    def show(self):
     print(f"{self.name} {self.year_graduate} {self.genre} {self.number_view}")
    
       
class Serial(Film):
    def __init__(self, name, year_graduate, genre, number_series, number_season, number_view):
     Film.__init__(self, name = name, year_graduate = year_graduate, genre = genre, number_view = number_view)
     self.number_series = number_series
     self.number_season = number_season
     
    def play(self):
     self.number_view += 1 
     
    def show(self):
     print(f"{self.name} {self.year_graduate} {self.genre} {self.number_series} {self.number_season} {self.number_view}")
     
film1 = Film("Титанік", 1997, "Драма", 234)
film2 = Film("Гладіатор", 2000, "Екшн", 197)
film3 = Film("Засуха", 2020, "Детектив", 54)
serial1 = Serial("Гра престолів", 2011, "Драма", 73, 8, 205)
serial2 = Serial("Цілком таємно", 1993, "Фантастика", 201, 11, 163)
serial3 = Serial("Венздей", 2022, "Фантастика", 8, 1, 147)
list_film = [film1, film2, film3] 
list_serial = [serial1, serial2, serial3]

def add_film():
 film = Film(name, year_graduate, genre, number_view)
 list_film.append(film)
    
def add_serial():
 serial = Serial(name, year_graduate, genre, number_series, number_season, number_view)
 list_serial.append(serial) 
 

while True:
 action = input("What would you like to do?")
 if action == "show":
  for film in list_film:
   film.show()
  for serial in list_serial:
   serial.show()
 if action == "add film":
    name = input("Film name")
    year_graduate = int(input("Film year graduate"))
    genre = input("Film genre")
    number_view = int(input("Film number view"))
    print(add_film())
    for film in list_film:
     film.show()
    for serial in list_serial:
     serial.show()
 if action == "add serial":
    name = input("Serial name")
    year_graduate = int(input("Serial year graduate"))
    genre = input("Serial genre")
    number_series = int(input("Serial number series"))
    number_season = int(input("Serial number season"))
    number_view = int(input("Serial number view"))
    print(add_serial())
    for film in list_film:
     film.show()
    for serial in list_serial:
     serial.show()    
 