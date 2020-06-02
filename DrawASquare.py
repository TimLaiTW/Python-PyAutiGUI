import pyautogui
# Open Safari browser - moveTo() + click()
pyautogui.click(x=833, y=1030, button='left')

# Enter url(autodraw.com) - typewrite()
pyautogui.typewrite('autodraw.com', interval=0.1)
pyautogui.press('enter')

# Draw the square - drag()
pyautogui.moveTo(x=958, y=310, duration=0.5)
distance = 80
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5, button='left')   # move right
        distance -= 10
        pyautogui.drag(0, distance, duration=0.5, button='left')   # move down
        pyautogui.drag(-distance, 0, duration=0.5, button='left')  # move left
        distance -= 10
        pyautogui.drag(0, -distance, duration=0.5, button='left')  # move up

# Point the square - click()
pyautogui.click(x=756, y=234, duration=0.2, button='left')
pyautogui.moveTo(x=948, y=302, duration=0.2)
pyautogui.dragTo(x=1078, y=409, duration=0.5, button='left')

# Move the square - press()
for i in range(5):
    pyautogui.press('right')

pyautogui.press('down', presses=3)
