import pyautogui
import time
print("Press Ctrl-C to quit!")
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        
        # Add RGB of the pixel to the output
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        colorStr = ' RGB: ' + str(pixelColor[0:3]).rjust(3)
        positionStr += colorStr
        
        print(positionStr, end='')
        time.sleep(0.5)
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('Interrupted')

print('Done.')
