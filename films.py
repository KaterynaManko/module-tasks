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
     
          
class Filmoteka():
 def __init__(self):
    self.list_movies = []
    
 def show_movie(self):
  for movie in  self.list_movies:
   movie.show()   
 
 def add_movie(self, movie):
  self.list_movies.append(movie)
  
 def search(self, name_search):
   for movie in  self.list_movies:
    if name_search == movie.name:
     movie.show()
     
 def play(self, name_play, number_season_play, number_series_play):
   for movie in  self.list_movies:
    if name_play == movie.name:
     print(f"{name_play} S0{number_season_play}E0{number_series_play}")
     movie.play()
     movie.show() 
     
 def show_films(self): 
  for movie in  self.list_movies:
   if isinstance(movie, Serial) == False:
      movie.show()
      
 def show_serials(self): 
  for movie in  self.list_movies:
   if isinstance(movie, Serial) == True:
      movie.show() 
      
 def generate_views(self):  
  random_list_movies = random.choice(self.list_movies)
  generate_number = [movie for movie in range(0, 101)]
  for j in range(random.choice(generate_number)):
   print(random_list_movies) 
   
 def top_titles(self):
  by_name = sorted(self.list_movies, key=lambda movie: movie.number_view) 
  print(by_name[-3:])
      
      
film1 = Film("Титанік", 1997, "Драма", 234)
film2 = Film("Гладіатор", 2000, "Екшн", 197)
film3 = Film("Засуха", 2020, "Детектив", 54)
serial1 = Serial("Гра престолів", 2011, "Драма", 73, 8, 205)
serial2 = Serial("Цілком таємно", 1993, "Фантастика", 201, 11, 163)
serial3 = Serial("Венздей", 2022, "Фантастика", 8, 1, 147)
 
list_movies = Filmoteka()
list_movies.add_movie(film1)
list_movies.add_movie(film2)
list_movies.add_movie(film3)
list_movies.add_movie(serial1)
list_movies.add_movie(serial2)
list_movies.add_movie(serial3)

if __name__ == "__main__":
 print("ФІЛЬМОТЕКА")
 list_movies.show_movie()
 list_movies.generate_views() 
 print(f"Найпопулярніші фільми та серіали дня {datetime.datetime.now()}")
 list_movies.top_titles()
  
while True: 
 action = input("What would you like to do?")
 
 if action == "show":
  list_movies.show_movie()
      
 if action == "add film":
    name = input("Film name")
    year_graduate = int(input("Film year graduate"))
    genre = input("Film genre")
    number_view = int(input("Film number view"))
    movie = Film(name, year_graduate, genre, number_view)
    list_movies.add_movie(movie)
    list_movies.show_movie()
    
 if action == "add serial":
    name = input("Serial name")
    year_graduate = int(input("Serial year graduate"))
    genre = input("Serial genre")
    number_series = int(input("Serial number series"))
    number_season = int(input("Serial number season"))
    number_view = int(input("Serial number view"))
    movie = Serial(name, year_graduate, genre, number_series, number_season, number_view)
    list_movies.add_movie(movie)
    list_movies.show_movie() 
    
 if action == "search":
    name_search = input("Serial or film name for search")
    list_movies.search(name_search)  
    
 if action == "play":
    name_play = input("Serial name for play")
    number_season_play = int(input("Serial number season for play"))
    number_series_play = int(input("Serial number series for play"))
    list_movies.play(name_play, number_season_play, number_series_play)
    
 if action == "show films":
    list_movies.show_films() 
    
 if action == "show serials":
    list_movies.show_serials() 
    
 if action == "generate":
    list_movies.generate_views() 
    
 if action == "generate 10":
    for i in range(10):
     list_movies.generate_views()
     
 if action == "top":
    list_movies.top_titles()