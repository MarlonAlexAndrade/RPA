import pyautogui as p
from time import sleep 

p.PAUSE = 2
p.hotkey('win', 'r')
p.write('C:\RPA.pbix')
p.press('enter')
sleep(8)
p.click(713, 96)
sleep(4)
p.click(1893, 13)
p.click(972, 557)

# sleep(3)
# print(p.position())