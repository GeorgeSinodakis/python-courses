import pyautogui
import time
import datetime
import os
import platform

zoom_path = "C:\\Users\\GEORGE\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

courses = [ {"name" : "ΠΡΟΗΓΜ.ΕΛΕΓΧ.ΗΛΕΚΤΡ.ΜΗΧ.-Θ",		"day" : "Mon", "time" : "09", "id" : "##########"},
			{"name" : "ΜΗ ΚΑΤΑΣΤΡ.ΕΛΕΓΧ-Θ",				"day" : "Mon", "time" : "12", "id" : "##########"},
			{"name" : "ΣΑΕΙΙΙ-ΕΠ-Θ",					"day" : "Tue", "time" : "17", "id" : "##########"},
			{"name" : "ΑΛΛΗΛ.ΑΝΘΡ.ΜΕ ΣΥΣΤ.ΜΗΧΑΤΡ.-Θ",	"day" : "Thu", "time" : "09", "id" : "##########"},
			{"name" : "ΕΥΦΥΗ ΣΥΣΤΗΜΑΤΑ-Θ",				"day" : "Fri", "time" : "11", "id" : "##########"} ]

while True:
	date = time.asctime(time.localtime(time.time()))
	for c in courses:
		if c.get("day") == date[0:3] and c.get("time") == date[11:13]:
			if platform.system() == 'Windows':
				os.startfile(zoom_path)
			else:
				os.system(zoom_path)
			while True:
			    try:
			    	pyautogui.moveTo(100, 200)
			    except:
			        continue
			    else:
		        	break
			while True:
			    try:
			        pyautogui.click("join_a_meeting.png")
			    except:
			        continue
			    else:
		        	break
			while True:
			    try:
			        pyautogui.click("enter_id.png")
			    except:
			        continue
			    else:
		        	break
			pyautogui.typewrite(c.get("id"))
			while True:
			    try:
			        pyautogui.click("join.png")
			    except:
			        continue
			    else:
		        	break
			time.sleep(60*70)
	time.sleep(0.1)
