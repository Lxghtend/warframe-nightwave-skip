import keyboard
import pyautogui
import time
# sorry this is unreadable
def your_function():
    # Replace this with the function you want to run
    print("Key pressed! Running your function.")
    keyboard.send('esc')
    nightwave = pyautogui.locateCenterOnScreen('nightwave.png', confidence=0.7)
    while nightwave is None:
        time.sleep(0.1)
        nightwave = pyautogui.locateCenterOnScreen('nightwave.png', confidence=0.7)
    pyautogui.moveTo(nightwave)
    for i in range(3):
        time.sleep(0.1)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp
    thing = pyautogui.locateCenterOnScreen('thing.png', confidence=0.7)
    while thing is None:
        time.sleep(0.1)
        thing = pyautogui.locateCenterOnScreen('thing.png', confidence=0.7)
    keyboard.send('esc')

# Define the key you want to listen for
target_key = '0'  # You can change this to the key combination you want
# PUT THE KEY U WANT TO BIND IT TO HERE
# EX. ctrl+shift+a
# EX. a

# Register the hotkey and specify the function to run
keyboard.add_hotkey(target_key, your_function)

try:
    # Keep the script running
    keyboard.wait()
except KeyboardInterrupt:
    # Handle KeyboardInterrupt (e.g., when you manually stop the script)
    pass
finally:
    # Unregister the hotkey when the script is interrupted
    keyboard.unhook_all()
