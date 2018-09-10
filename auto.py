# python3
# @author Xavier Collantes
# @date 09/09/2018

import pyautogui, time, arrow, os, random


pyautogui.PAUSE = 0.80
pyautogui.FAILSAFE = True


# MoveMouse will run until ctl+c is pressed or failsafe is triggered 
def moveMouse(min=10, max=25):	
	running()
	screenW = pyautogui.size()[0]
	screenH = pyautogui.size()[1]
	halfPos = (screenW // 2, screenH // 2)
	pyautogui.moveTo(halfPos)
	try:
		while True:		
			pyautogui.moveRel((10, 0))
			time.sleep(random.randrange(min, max))
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED.")

		
def pressKeySub(key='ctl', min=10, max=20):
	running()
	try:
		while True:
			pyautogui.press(key)
			time.sleep(random.randrange(min, max))
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED.")
	
	
# Switches between up to three windows by pressing `Alt + Tab` 
def switchWin(min=5, max=6):
	running()
	try:
		while True:
			pyautogui.keyDown('alt')
			
			for m in range(random.randint(1, 5)):
				pyautogui.press('tab')
			pyautogui.keyUp('alt')

			time.sleep(random.randrange(min, max))
	except KeyboardInterrupt as kb:
		pass


def writeEssay(key='win'):
	running()
	
	# Open text source 
	try:
		f = open('txt/smith.txt', 'r')
	except IOError as ioe:
		print("Source file not found: %s" %ioe)
		
	try:
		# Open MS Word 
		pyautogui.press('win')
		time.sleep(2)
		pyautogui.typewrite('Microsoft Word')
		time.sleep(2)
		pyautogui.press('enter')
		time.sleep(15)
		pyautogui.press('enter')
		
		# Expand MS Word window 
		pyautogui.hotkey('win', 'up')
		
		# Take text file into string 
		text = f.read()
		textSep = text.split(',')
		
		# Write Adam Smith's 1776 "The Wealth of Nations"
		for i in textSep:
			
			pyautogui.typewrite(i)
			time.sleep(random.randrange(20, 30))
			
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED.")
	
	f.close()
	
	
# Indicator print out program is running 
def running():
	print ("Running... ")
	print ("Press `CTL + C` on your keyboard to end this program.")
	
	
if __name__ == '__main__':
	try:
		print("Hello! Thank you for using this productivity app.")
		
		#moveMouse()
		#pressKeySub()
		#writeEssay()
		switchWin(1, 3)
		
		
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED. %s" %kb)