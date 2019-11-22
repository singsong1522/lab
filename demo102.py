import pyautogui

print(pyautogui.size())
for i in range(10):
    pyautogui.moveTo(100+10*i, 100+10*1, duration=1)
    pyautogui.moveTo(200+10*i, 100+10*i, duration=1)
    pyautogui.moveTo(200+10*i, 200+10*i, duration=1)
    pyautogui.moveTo(100+10*i, 200+10*i, duration=1)



