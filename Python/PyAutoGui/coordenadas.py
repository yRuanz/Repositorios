import pyautogui as pag #importa o pyautogui e apelida ele de pag
import time #importa tempo

x, y = pag.position()
time.sleep(7)
print(f"x = {x} e y = {y}")