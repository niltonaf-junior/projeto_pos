from time import sleep
import pyautogui

pyautogui.PAUSE=1


def move(locate):
    x,y = pyautogui.center(locate)
    pyautogui.moveTo(x,y,duration=1)

def move_click(locate):
    move(locate)
    pyautogui.click()    

sleep(3)
lancamento = pyautogui.locateOnScreen('images/lancamento.png',confidence=0.8)
if lancamento == None:
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('g')
    sleep(1)
    pyautogui.write('lanca')
    sleep(1)
    pyautogui.press('enter') 

nu_vazio = pyautogui.locateOnScreen('images/nu.png',confidence=0.8)
while nu_vazio == None:
    sleep(0.5)
    nu_vazio = pyautogui.locateOnScreen('images/nu.png',confidence=0.8)

move_click(nu_vazio)

pyautogui.press('f8')
pyautogui.press('tab',presses=4)
sleep(1)
pyautogui.write('300')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.press('tab')
pyautogui.write('4')
pyautogui.press('tab')
pyautogui.write('9842')
pyautogui.press('tab')
pyautogui.write('1')
pyautogui.press('tab')
pyautogui.write('101')
pyautogui.press('tab')
pyautogui.write('194')
pyautogui.press('tab')
pyautogui.write('90001000')
pyautogui.press('tab')
pyautogui.write('1010504')
pyautogui.press('tab')
pyautogui.write('3020402')
pyautogui.press('tab',presses=7)
pyautogui.write('08032023')
pyautogui.press('tab')
pyautogui.write('08042023')
pyautogui.press('tab',presses=2) 