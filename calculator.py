import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(*args):
 if action_sign == 1:
  z = float(input("Введи число 3 "))
  logging.info(f"Додаю {x} i {y} і {z}\nРезультат")
  return x + y + z
 elif action_sign == 2:
  logging.info(f"Віднімаю {x} i {y}\nРезультат") 
  return x - y
 elif action_sign == 3:
  z = float(input("Введи число 3 "))   
  logging.info(f"Множу {x} i {y} і {z}\nРезультат")
  return x * y * z
 elif action_sign == 4:
  if y == 0:
   raise Exception("На 0 ділити не можна!!!")
  logging.info(f"Ділю {x} i {y}\nРезультат")
  return x / y
     
  
if __name__ == "__main__":
 action_sign = int(input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення "))
 if 1 < action_sign > 4:
  logging.error("Введено неправильний оператор")
  exit(1) 
 x = float(input("Введи число 1 "))
 y = float(input("Введи число 2 "))
 logging.info(calculator(x, action_sign, y))     