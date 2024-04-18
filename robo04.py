import pyautogui as p
from time import sleep

p.PAUSE = 1
p.doubleClick(x=48, y=224)

p.hotkey('win', 'up')

p.write('www.udemy.com')
p.press('enter')

local_pesq = p.locateOnScreen('Imagens/Teste02.png', confidence=0.9, minSearchTime=3)
local_pesquisa = p.center(local_pesq)
x_pesquisa, y_pesquisa = local_pesquisa
p.moveTo(x_pesquisa, y_pesquisa)
p.click(x_pesquisa, y_pesquisa)
p.write('Charles Lima')
p.press('enter')

sleep(2)
p.screenshot('Cursos.png')

local_clo = p.locateOnScreen('Imagens/Close.PNG', confidence=0.9, minSearchTime=3)
local_close = p.center(local_clo)
x_close, y_close = local_close
p.moveTo(x_close, y_close)
p.click(x_close, y_close)


