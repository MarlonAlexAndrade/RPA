import pyautogui as p
p.PAUSE=1
import time


p.hotkey('win', 'r')
# p.sleep(1)
p.typewrite('notepad')
# p.sleep(2)
p.press('enter')
#De preferencia usar sleep dessa forma quando nescessario pontualmente
# time.sleep(4)
p.typewrite('Ola !! Eu sou um Bot!', interval=0.02)
# p.sleep(2)
p.hotkey('ctrl', 'w')
# valor = p.getActiveWindow()
# valor.close()
p.press('right')
# p.sleep(2)
p.press('enter')

# p.moveTo(2933, 1060, duration=1)

# p.click(2933, 1060)

# p.sleep(2)
# print(p.position())
