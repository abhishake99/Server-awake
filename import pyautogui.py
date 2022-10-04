import pyautogui
import time
import random
pyautogui.FAILSAFE = False

def delay(x):
    time.sleep(x)

def keystroke():
     pyautogui.press('volumedown')

def mclick(x_coord,y_coord,timer):
    pyautogui.moveTo(x_coord, y_coord, timer)
    pyautogui.click(x_coord,y_coord)

def tabs(i):
    with pyautogui.hold('alt'):
        for i in range(i):
             pyautogui.press("tab",interval=1)
        pyautogui.press("tab",interval=1)         
i = 1
kct=0
mct=0
mta=0
timenew=0
while i:
    delay(2) #keyboard
    ran=random.randint(0,20)
    for j in range(ran):
        keystroke()
        delay(2)
    kct+=ran    
    x_coord =  1366 #mouse
    y_coord =  768
    time_rand = 0
    delay(2)
    ran=random.randint(0,20)
    for k in range(ran):
        mclick(x_coord,y_coord,time_rand)
        delay(3)
    mct+=ran
    delay(2)  #tab
    ran=random.randint(0,6)
    tabs(ran)
    mta=ran
    print("keystrokes : ",kct,",click : ",mct," ,tab : ",mta)    
    kct=0
    mct=0
    mta=0
    i+= 1
    