import pyautogui
from time import sleep

pyautogui.press('winleft')
pyautogui.write('explorador de arquivos')
pyautogui.press('enter')
sleep(5)
pyautogui.moveTo(93,139)
pyautogui.doubleClick(93,139)
sleep(1)
pyautogui.moveTo(449,149)
pyautogui.doubleClick(449,149)
sleep(1)
pyautogui.moveTo(507,514)
pyautogui.click(507,514)

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.moveTo(600,50)
sleep(1)
pyautogui.click(600,50)

pyautogui.write('web.whatsapp.com')
pyautogui.press('enter')
pyautogui.moveTo(179,174)
sleep(7)
pyautogui.click(179,174)
pyautogui.write('grupo pra salvar coisas')
pyautogui.press('enter')

pyautogui.rightClick(646,809)
pyautogui.click(698,658)
sleep(1)
pyautogui.press('enter')


