import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(*args):
 if action_sign == 1:
  z = float(input("Введи число 3 "))
  return(f"Додаю {x} i {y} і {z}\nРезультат {(x + y + z)}")
 elif action_sign == 2:
  return(f"Віднімаю {x} i {y}\nРезультат {(x - y)}") 
 elif action_sign == 3:
  z = float(input("Введи число 3 "))   
  return(f"Множу {x} i {y} і {z}\nРезультат {(x * y * z)}")
 elif action_sign == 4 and y != 0:
  return(f"Ділю {x} i {y}\nРезультат {(x / y)}")
 else:
  return("Введено неправильний оператор")
  
if __name__ == "__main__":
 action_sign = int(input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення "))
 x = float(input("Введи число 1 "))
 y = float(input("Введи число 2 "))
 print(calculator(x, action_sign, y))     