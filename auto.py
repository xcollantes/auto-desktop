# python3
# @author Xavier Collantes
# @date 09/09/2018

import pyautogui, time, arrow

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = TRUE

def moveMouse():
	

	
def changeWin():


def pressKey():
	


def findImg():

if __name__ == '__main__':
	try:
		mouseMove()
		changeWin()
		pressKey()
		os.chdir('lib/')
		i = pyautogui.locateOnScreen('word.PNG')
		
		if i != None:
			pyautogui.click(pyautogui(center(i)))
		else:
			print("Image not found.")
		
		
	except KeyboardInterrupt as kb:
		print("PROGRAM HALTED. %s" %kb)