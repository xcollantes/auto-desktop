# python3
# @author Xavier Collantes
# @date 09/09/2018

import pyautogui, time, arrow, os, random


pyautogui.PAUSE = 0.80
pyautogui.FAILSAFE = True


# MoveMouse will run until ctl+c is pressed or failsafe is triggered 
def moveMouse():	
	running()
	screenW = pyautogui.size()[0]
	screenH = pyautogui.size()[1]
	halfPos = (screenW // 2, screenH // 2)
	pyautogui.moveTo(halfPos)
	try:
		while True:		
			pyautogui.moveRel((10, 0))
			time.sleep(random.randrange(10, 25))
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED.")

		
def pressKeySub(key='ctl'):
	running()
	try:
		while True:
			pyautogui.press(key)
			time.sleep(random.randrange(10, 20))
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED.")
	

# Indicator print out program is running 
def running():
	print ("Running... ")
	print ("Press `CTL + C` on your keyboard to end this program.")
	
	
if __name__ == '__main__':
	try:
		os.chdir('img/')
		print("Hello! Thank you for using this productivity app.")
		
		#moveMouse()
		pressKeySub()
		
		
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED. %s" %kb)