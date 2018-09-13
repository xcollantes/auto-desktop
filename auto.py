# python3
# @author Xavier Collantes
# @date 09/09/2018

import pyautogui, time, arrow, os, random, subprocess


pyautogui.PAUSE = 0.80
pyautogui.FAILSAFE = True


# MoveMouse will run until ctl+c is pressed or failsafe is triggered 
def moveMouse(min=10, max=25):	
	running()
	pix = 10
	screenW = pyautogui.size()[0]
	screenH = pyautogui.size()[1]
	halfPos = (screenW // 2, screenH // 2)
	pyautogui.moveTo(halfPos)
	try:
		while True:
			dir = random.randint(0, 2)
			if dir >= 1:
				pyautogui.moveRel((pix, 0))
			else:
				pyautogui.moveRel((0, pix))
			
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
def switchWin(min=30, max=50):
	running()
	try:
		# Remove cmd window from the switch back and forth 
		pyautogui.hotkey('alt', 'tab')
		pyautogui.keyDown('altleft')  # I'm not about the AltRight 
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.keyUp('altleft')
		
		while True:
			pyautogui.hotkey('alt', 'tab')
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
		pyautogui.typewrite('Word')  # I hope the first option is MS Word 
		time.sleep(2)
		pyautogui.press('enter')
		time.sleep(15)
		pyautogui.press('enter')
		
		# Expand MS Word window 
		pyautogui.hotkey('win', 'up')
		
		# Take text file into string 
		text = f.read()
		textSep = text.split(',')
		
		# Header for your fake-ass essay 
		pyautogui.typewrite(arrow.utcnow('local'))
		pyautogui.press('enter')
		
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
	
	
# Print out the options in Command Line and returns chosen program 
def options():
	print("Enter a program number and press ENTER:")
	print("")
	print("Program    |   Description                                         |   Program Number")
	print("-------------------------------------------------------------------------------------")
	print("Mouse      :  Moves mouse a few pixels every 10 to 25 seconds      |   1")
	print("")
	print("Crazy Ctl  :  Randomly presses `Ctl` every 10 to 20 seconds        |   2")
	print("")
	print("Switch     :  Switch back and forth every between two open windows |   3")
	print("")
	print("Ghostwriter:  a) Search for Microsoft Word on your computer        |   4")
	print("              b) Then write Adam Smith's 1776 'Wealth of Nations'     ")
	print("")
	userInput = input("Please choose a number corresponding to a program: ")
	
	if userInput in {"1", "2", "3", "4"}:
		return userInput
	else:
		options()

		
# Instructions after the program is terminated 
def cleanEnd():
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")
		
		
def hideEvidence():
	os.system("exit")

	
if __name__ == '__main__':
	try:
		print("Hello! Thank you for using this productivity app.")
		print("")
		
		choice = options()
		if choice == '1':  # Mouse
			moveMouse()
		elif choice == '2':  # Crazy Ctl
			pressKeySub()
		elif choice == '3':  # Switch
			switchWin()
		elif choice == '4':  # Ghostwriter
			writeEssay()
		else:
			options()
		
	except KeyboardInterrupt as kb:
		cleanEnd()
		hideEvidence()