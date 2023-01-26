import random
import datetime

class Film:
     def __init__(self, name, year_graduate, genre, number_view):
      self.name = name
      self.year_graduate = year_graduate
      self.genre = genre
      self.number_view = number_view
     
     def __repr__(self):
        return repr((self.name, self.year_graduate, self.genre, self.number_view)) 
     
     def play(self):
      self.number_view += 1
           
     def show(self):
      print(f"{self.name}\t({self.year_graduate})\t{self.genre}\tПереглядів: {self.number_view}")
                   
     
class Serial(Film):
     def __init__(self, name, year_graduate, genre, number_series, number_season, number_view):
      Film.__init__(self, name = name, year_graduate = year_graduate, genre = genre, number_view = number_view)
      self.number_series = number_series
      self.number_season = number_season
            
     def __repr__(self):
        return repr((self.name, self.year_graduate, self.genre, self.number_series, self.number_season, self.number_view)) 
      
     def show(self):
      print(f"{self.name}\t({self.year_graduate})\t{self.genre}\tСерій: {self.number_series}\tСезонів: {self.number_season}\tПереглядів: {self.number_view}")
     
          
list_movies = [] 
film1 = Film("Титанік", 1997, "Драма", 234)
film2 = Film("Гладіатор", 2000, "Екшн", 197)
film3 = Film("Засуха", 2020, "Детектив", 54)
serial1 = Serial("Гра престолів", 2011, "Драма", 73, 8, 205)
serial2 = Serial("Цілком таємно", 1993, "Фантастика", 201, 11, 163)
serial3 = Serial("Венздей", 2022, "Фантастика", 8, 1, 147)
 
list_movies.append(film1)
list_movies.append(film2)
list_movies.append(film3)
list_movies.append(serial1)
list_movies.append(serial2)
list_movies.append(serial3)

def add_film():
 film = Film(name, year_graduate, genre, number_view)
 list_movies.append(film)
    
def add_serial():
 serial = Serial(name, year_graduate, genre, number_series, number_season, number_view)
 list_movies.append(serial) 
 
def search():
 name_search = input("Serial or film name for search")
 for movie in list_movies:
  if name_search == movie.name:
   movie.show()    
   
def generate_views():  
 random_list_movies = random.choice(list_movies)
 generate_number = [i for i in range(0, 101)]
 for j in range(random.choice(generate_number)):
  print(random_list_movies)
  
def generate_views_10():
 for i in range(10):
  generate_views()  
  
def top_titles():
 by_name = sorted(list_movies, key=lambda movie: movie.number_view) 
 print(by_name[-3:])
 
    
if __name__ == "__main__":
 print("ФІЛЬМОТЕКА")
 for movie in list_movies:
     movie.show()
 generate_views() 
 print(f"Найпопулярніші фільми та серіали дня {datetime.datetime.now()}")
 top_titles()
     
while True: 
 action = input("What would you like to do?")
 
 if action == "show":
  for movie in list_movies:
   movie.show()
      
 if action == "add film":
    name = input("Film name")
    year_graduate = int(input("Film year graduate"))
    genre = input("Film genre")
    number_view = int(input("Film number view"))
    add_film()
    for movie in list_movies:
     movie.show()
         
 if action == "add serial":
    name = input("Serial name")
    year_graduate = int(input("Serial year graduate"))
    genre = input("Serial genre")
    number_series = int(input("Serial number series"))
    number_season = int(input("Serial number season"))
    number_view = int(input("Serial number view"))
    add_serial()
    for movie in list_movies:
     movie.show()   
     
 if action == "play":
     name_play = input("Serial name for play")
     for movie in list_movies:
      if name_play == movie.name:
       number_season_play = int(input("Serial number season for play"))
       number_series_play = int(input("Serial number series for play"))
       print(f"{name_play} S0{number_season_play}E0{number_series_play}")
       movie.play()
            
 if action == "show films":
   for movie in list_movies:
     if isinstance(movie, Serial) == False:
      movie.show()
      
 if action == "show serials":
   for movie in list_movies:
     if isinstance(movie, Serial) == True:
      movie.show()
      
 if action == "search":
     search()   
     
 if action == "generate":
    generate_views()    
  
 if action == "generate 10":
    generate_views_10() 
    
 if action == "top":
    top_titles()    