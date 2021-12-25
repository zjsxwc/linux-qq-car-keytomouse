from pynput.keyboard import Key, Listener
import pyautogui


isJdown = False

def on_press(key):
    global isJdown
    print('{0} pressed'.format(key))
    thek = str(key)
    if thek == "'0'":
        pyautogui.moveTo(925,582)
        pyautogui.click()
    if thek == "Key.space" and (not isJdown):
        pyautogui.moveTo(1062,670)
        pyautogui.mouseDown()
        isJdown = True
    if thek == "'-'":
        pyautogui.moveTo(1035,507)
        pyautogui.click()
    if thek == "'='":
        pyautogui.moveTo(1145,513)
        pyautogui.click()

    #if hasattr(key, 'vk'):
    #    print('vk:  ', key.vk)
    #print(thek == "'o'")
    #print(thek == "Key.ctrl")

def on_release(key):
    global isJdown
    print('{0} release'.format(key))
    thek = str(key)
    if thek == "Key.space":
        pyautogui.mouseUp()
        isJdown = False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
