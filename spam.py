import pyautogui, time

spam_text="TEST SPAM"
for_in range(50):
    pyautogui.typewrite(spam_text)
    pyautogui.press("enter")