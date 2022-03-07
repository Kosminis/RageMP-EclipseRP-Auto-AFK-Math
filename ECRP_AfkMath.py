sleepTime = 5 # Sleep time for how much it sleeps. E.g After an error

import re, time, os, cv2
import random
import pyperclip as pc
import pytesseract as pt
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Controller
from PIL import Image

#checks for tesseract.exe in known places
if os.path.exists('C:\\Program Files\\Tesseract-OCR\\tesseract.exe'):
    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
else:
    pt.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

os.system("title Auto Eclipse AFK Answering by Kosminis - v1.1")
while (True):
 os.system("cls")
 # take a screenshot of the monitor pixel selected.
 img=ImageGrab.grab(bbox=(30,255,750,325))
 d = img.getdata()
 # Change the color of img
 new_image = []
 for item in d:
 # change all white (also shades of whites)
     # pixels to green(ish) not sure if this is useful, but fuck it.
     if item[0] in list(range(200, 256)):
         new_image.append((200, 250, 200))
     else:
        new_image.append(item)
 # update image data
 img.putdata(new_image)
 # save new image
 img = img.point(lambda pixel: 0 if pixel<128 else 255)
 text = pt.image_to_string(img)
 print(f"TEXT IN STRING: {text}")

 # Function for automatic /afkmath writing
 def MainFunction():
     try:
         split_string = text.split("+", 1)
         substring = int(re.search(r'\d+', split_string[0]).group())
         substring1 = int(re.search(r'\d+', split_string[1]).group())
         print(f"SUB STRING: {substring}, {substring1}")
         print(f"NUMBERED: {substring + substring1}")
         Number = substring + substring1
         time.sleep(random.randint(3, 5) + (random.randint(1, 9) / 10))
         keyboard = Controller()
         keyboard.press('t')
         keyboard.release('t')
         pc.copy(f"/afkmath {Number}")
         keyboard.press(Key.ctrl)
         keyboard.press('v')
         keyboard.release('v')
         keyboard.release(Key.ctrl)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         print("Sleeping for 9 minutes!")
         time.sleep(540)
         os.system("cls")
     except:
         print("")

 #Detects if string contains "AFK SCRIPT", "+", "afkmath" in it.
 if text != None and "WEAZEL" in text:
     print(f"Found [WEAZEL] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "NEWS" in text:
     print(f"Found [NEWS] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "WEAZE" in text:
     print(f"Found [WEAZE] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "WEAZ" in text:
     print(f"Found [WEAZ] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "INFO" in text:
     print(f"Found [INFO] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "says" in text:
     print(f"Found [says] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "radio" in text:
     print(f"Found [radio] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "clipse" in text:
     print(f"Found [clipse] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
     time.sleep(sleepTime)
 elif text != None and "AFK Script" in text:
     print(f"Found [AFK Script]!")
     #checks for errors
     if text != None and "+" not in text:
         print(f"Can't find [+] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     elif text != None and "no longer" in text:
         print(f"Found [no longer] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     elif text != None and "considered" in text:
         print(f"Found [considered] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     else:
         MainFunction()
 elif text != None and "afkmath" in text:
     print(f"Found [afkmath]!")
     #checks for errors
     if text != None and "+" not in text:
         print(f"Can't find [+] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     elif text != None and "no longer" in text:
         print(f"Found [no longer] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     elif text != None and "considered" in text:
         print(f"Found [considered] IGNORING AND SLEEPING FOR {sleepTime} SECONDS!")
         time.sleep(sleepTime)
     else:
         MainFunction()
 else:
    print(f"Not found Sleeping for {sleepTime} secs!")
    time.sleep(sleepTime)

'''
v1.1:
Better random time for /afkmath.
calculation for how many times afkmath has been answered.
Automaticly looks in known places for tesseract.exe
Program doesn't save the screenshot that its taken.
Removed some useless code
Added more checks for text
'''
 


