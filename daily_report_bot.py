# prepare daily status report from copying the data from chrome and 
# paste it into the excel file

import pyautogui
import time
import datetime
import re
import pyperclip
import pyscreeze

pyautogui.FAILSAFE=True
pyautogui.PAUSE=1

print("opening the chrome browser")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('chrome')
pyautogui.press('enter')
time.sleep(1)
print("chrome browser opened")


print("opening the daily status report page")
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.typewrite('https://in.tradingview.com/symbols/NASDAQ-GOOG/')
pyautogui.press('enter')
time.sleep(3)
print("daily status report page opened")


print("copying the data from the daily status report page")
time.sleep(5)
pyautogui.dragTo(500, 500, duration=3)
time.sleep(5)
pyautogui.doubleClick(500, 500)  
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(3)
print("data copied from the daily status report page")

# get current date and time
now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# get copied data from clipboard
copied_data = pyperclip.paste()

# create final string
final_text = f"Date&Time :{formatted_time} \n Stock name: Google \n value:{copied_data}"

# copy final text back to clipboard
pyperclip.copy(final_text)

print("opening the excel file")
pyautogui.hotkey('win', 'r')   
time.sleep(1) 
pyautogui.typewrite('excel')
pyautogui.press('enter')
print("excel file opened")
time.sleep(1)

#now in excel file, oday's date & time, the fetched data, and your own short comment

print("pasting the data into the excel file")
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
print("data pasted into the excel file")

#saving the filename in current date in the YYYY-MM-DD format.
file_name = now.strftime("%Y-%m-%d") + ".xlsx"
print("saving the excel file")
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite(file_name)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
print("excel file saved")

#taking screenshot of the excel file and saving it in the current directory 
# with the name "daily_report.png"
print("taking screenshot of the excel file")
time.sleep(1)
screenshot=pyautogui.screenshot()
screenshot.save("daily_report.png")
print("screenshot Saved")

