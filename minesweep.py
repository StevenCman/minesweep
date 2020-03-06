#!/usr/bin/python
from tkinter import *
import os
import tkinter
import webbrowser
import random
import time
from PIL import Image
from PIL import ImageTk

def settings():
	try:
		root.destroy()
	except:
		print()
	try:
		lostGame.destroy()
	except:
		print()
	try:
		gameWindow.destroy()	
	except:
		print()
	try:
		wonGame.destroy()
	except:
		print()		

	global settingsWindow
	settingsWindow = tkinter.Tk()
	settingsWindow.geometry("300x400")
	settingsWindow.title("Shitty Minesweeper")

	settingsTitle = Label(settingsWindow, text="Settings", font=("Times New Roman", 30))
	settingsTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	itemLabel = Label(settingsWindow, text="Please choose the size of your game",font=("Times New Roman", 10))
	itemLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

	mineLabel = Label(settingsWindow, text="Please choose the number of mines in your game",font=("Times New Roman", 10))
	mineLabel.place(relx=0.5, rely=0.6, anchor=CENTER)

	size = Listbox(settingsWindow, height=3)
	size.place(relx=0.5, rely=0.4, anchor=CENTER)
	for item in ["Small", "Medium", "Large"]:
		size.insert(END, item)

	mines = Listbox(settingsWindow, height=3)
	mines.place(relx=0.5, rely=0.7, anchor=CENTER)
	for item in ["Almost none", "Some", "Too many"]:
		mines.insert(END, item)

	continueButton = Button(settingsWindow, text= "Continue", command= lambda: gameplay(size.get(ACTIVE), mines.get(ACTIVE), 0))
	continueButton.place(relx=0.5, rely=0.9, anchor=CENTER)

def gameplay(size, mines, arr):
	global gameWindow
	global mineArray
	global btnArray
	global name
	global na
	global level
	if (level == 1):
		try:
			name = na.get()
		except:
			print()
	print(name)
	try:
		settingsWindow.destroy()
	except:
		print()

	try:
		campaignWindow.destroy()
	except:
		print()

	gameWindow = tkinter.Tk()
	if (level != 0):
		gameWindow.title("Shitty Minesweep Level " + str(level))
	else:	
		gameWindow.title("Shitty Minesweeper")
	x = 1
	y = 1
	num = 0
	if (size=="Small" and mines == "Almost none"):
		x = 5
		y = 5
		num = 5
	elif(size=="Small" and mines == "Some"):
		x = 5
		y = 5
		num = 10
	elif(size=="Small" and mines == "Too many"):
		x = 5
		y = 5
		num = 15		
	elif (size=="Medium" and mines == "Almost none"):
		x = 10
		y = 10
		num = 15
	elif (size=="Medium" and mines == "Some"):
		x = 10
		y = 10
		num = 35
	elif(size=="Medium" and mines == "Too many"):	
		x = 10
		y = 10
		num = 50
	elif(size=="Large" and mines == "Almost none"):
		x = 30
		y = 30
		num = 300
	elif(size=="Large" and mines == "Some"):
		x = 30
		y = 30
		num = 400	
	elif(size=="Large" and mines=="Too many"):
		x = 30
		y = 30
		num = 500
	else:
		x = size
		y = size
		num = mines

	mineArray = [[0 for p in range(y)] for q in range(x)]
	btnArray = [[0 for x in range(y)] for x in range(x)]

	if(arr==0):
		mineMaker(num, x, y, mineArray)
		updater(x,y,mineArray)
	else:
		mineArray = arr
	if(level == 1):
		tutorial = Label(gameWindow, text="The mine is in the middle square, just click around it")
		tutorial.pack(side=TOP)
	elif(level == 2):
		tutorial = Label(gameWindow, text="The mines for this one are in a diagonal line (bottom left to top right)\n If you click the other 2 corners it will reveal the board")
		tutorial.pack(side=TOP)
	elif(level == 3):
		tutorial = Label(gameWindow, text="No help for this one, its completely randomized except for the corners")	
		tutorial.pack(side=TOP)
	if(level == 0):
		restartBtn = Button(gameWindow, text= "Restart", command=settings)
		restartBtn.pack(side=TOP)

	quitBtn = Button(gameWindow, text= "Quit", command=quit)
	quitBtn.pack(side=TOP)

	hintBtn = Button(gameWindow, text= "Hint", command=lambda x1 = x, y1 = y, number = num: hint(x1, y1, number))
	hintBtn.pack(side = RIGHT)

	for t in range(x):
		frame = tkinter.Frame(gameWindow)
		frame.pack(side = BOTTOM)
		for u in range(y):
			z = t
			w = u
			btnArray[z][w] = Button(frame, width=5)
			btnArray[z][w].bind('<Button-1>',lambda event, x1=z, y1=w: left(event,x1,y1, num))
			btnArray[z][w].bind('<Button-3>',lambda event, x1=z, y1=w: right(event,x1,y1))
			btnArray[z][w].pack(side = LEFT)

def instructions():
	webbrowser.open("http://www.freeminesweeper.org/help/minehelpinstructions.html")

def quit():
	try:
		root.destroy()
	except:
		print()
	try:
		gameWindow.destroy()
	except:
		print()
	try:
		wonGame.destroy()
	except:
		print()
	try:
		lostGame.destroy()
	except:
		print()		
	try:
		lossWindow.destroy()
	except:
		print()	
def mineMaker(mines, x, y, mineArray):
	r = random.randint(0, x-1)
	c = random.randint(0, y-1)
	corner = False
	currentRow = mineArray[r]
	if((r == 0 and c == 0) or (r == 0 and c == y-1) or (r == x-1 and c == 0) or (r == x-1 and c == y-1)):
		corner = True
	if (mines == 0):
		return
	if not currentRow[c] == "*" and not corner:
		currentRow[c] = "*"
		mines -=1
		mineMaker(mines, x, y, mineArray)
	else:
		mineMaker(mines, x, y, mineArray)

def updater(x, y, mineArray):
	for r in range(0,x):
		for c in range(0,y):
			if mineArray[r][c] == "*":
				updateValue(r, c, mineArray)

def updateValue(rn, c, mineArray):

	if rn-1 > -1:
		if(mineArray[rn-1][c-1] != "*" and c-1 > -1):
			mineArray[rn-1][c-1] += 1

		if(mineArray[rn-1][c] != "*"):
			mineArray[rn-1][c] += 1

		if(c+1 < len(mineArray[0]) and mineArray[rn-1][c+1] != "*"):
			mineArray[rn-1][c+1] += 1

	if(c-1 > -1 and mineArray[rn][c-1] != "*"):
		mineArray[rn][c-1] += 1

	if(c+1 < len(mineArray[0]) and mineArray[rn][c+1] != "*"):
		mineArray[rn][c+1] += 1

	if rn+1 < len(mineArray[0]):
		if mineArray[rn+1][c-1] != "*" and c-1 > -1:
			mineArray[rn+1][c-1] += 1

		if mineArray[rn+1][c] != "*":
			mineArray[rn+1][c] += 1

		if  (c+1 < len(mineArray[0]) and mineArray[rn+1][c+1] != "*" ):
			mineArray[rn+1][c+1] += 1

def hint(x1,y1,num):
	x = random.randint(0, x1-1)
	y = random.randint(0, y1-1)
	if(str(btnArray[x][y]['state']) == "normal" and mineArray[x][y] != "*"):
		btnArray[x][y].config(text=mineArray[x][y], state=DISABLED)
		winCheck(x1, y1, num)
	else:
		hint(x1,y1,num)

def left(event,t,u, num):
	btnArray[t][u].unbind('<Button-1>')
	btnArray[t][u].unbind('<Button-3>')
	global lives

	if(mineArray[t][u] == "*" and level == 0):
		explosion()
		lost()
	elif(mineArray[t][u] == "*" and level > 0):
		if(lives > 0):
			lives -= 1
			explosion()
			liveLoss()
		else:
			explosion()
			campaignLost()	
	elif(mineArray[t][u] == 0):
		openZeros(t, u)
	else:
		btnArray[t][u].config(text=mineArray[t][u], state=DISABLED)
	
	winCheck(t,u,num)
    
def right(event,t,u):
    btnArray[t][u].config(bg='orange', text="flag")

def openZeros(x, y):
	row = mineArray[x]
	btnArray[x][y].config(text=mineArray[x][y], state=DISABLED)

	if (y-1 > -1):
		if (row[y-1] != "*" and str(btnArray[x][y-1]['state']) == "normal"):
			btnArray[x][y-1].config(text=mineArray[x][y-1], state=DISABLED)
			openZeros(x, y-1)

	if (y+1 < len(row)):
		if (row[y+1] != "*" and str(btnArray[x][y+1]['state']) == "normal"):
			btnArray[x][y+1].config(text=mineArray[x][y+1], state=DISABLED)
			openZeros(x, y+1)
	
	if (x-1 > -1):
		if (mineArray[x-1][y] != "*" and str(btnArray[x-1][y]['state']) == "normal"):
			btnArray[x-1][y].config(text=mineArray[x-1][y], state=DISABLED)
			openZeros(x-1, y)
	
	if (x+1 < len(mineArray)):
		if(mineArray[x+1][y] != "*" and str(btnArray[x+1][y]['state']) == "normal"):
			btnArray[x+1][y].config(text=mineArray[x+1][y], state=DISABLED)
			openZeros(x+1, y)		

def winCheck(x, y, num):
	global level
	counter = 0
	for t in range(len(btnArray)):
		for u in range(len(btnArray[t])):
			if (str(btnArray[t][u]['state']) == "normal"):
				counter += 1
	print("Counter: " + str(counter))			
	if (counter == num and level == 0):
		won()
	elif(counter == num and level > 0):
		level += 1
		campaign()

def won():
	gameWindow.destroy()
	global wonGame

	wonGame = tkinter.Tk()
	wonGame.title("CONGRATULATIONS!!")
	wonGame.geometry("400x400")

	victory = Image.open("victory.jpg")
	victory = victory.resize((100,100))
	victory = ImageTk.PhotoImage(victory)
	
	over = Label(wonGame, text="You have succesfully located all mines and have saved the day")
	over.pack(side=TOP)

	restartBtn = Button(wonGame, text= "Restart", command= settings)
	restartBtn.place(relx=0.5, rely=0.5, anchor=CENTER)

	vicLbl = Label(wonGame, image = victory)
	vicLbl.image = victory
	vicLbl.place(relx=0.5, rely=0.3, anchor=CENTER)

	mainMen = Button(wonGame, text="Main Menu", command=mainMenu)
	mainMen.place(relx=0.5, rely=0.7, anchor=CENTER)

	quitBtn = Button(wonGame, text= "Quit", command=quit)
	quitBtn.place(relx=0.5, rely=0.9, anchor=CENTER)

def lost():
	gameWindow.destroy()
	global lostGame
	lostGame = tkinter.Tk()
	lostGame.title("Game Over")
	lostGame.geometry("300x200")

	defeat = Image.open("loss.jpg")
	defeat = defeat.resize((100,100))
	defeat = ImageTk.PhotoImage(defeat)

	over = Label(lostGame, text="You hit a mine and have lost the game")
	over.pack(side=TOP)
	restartBtn = Button(lostGame, text= "Restart", command= settings)
	restartBtn.place(relx=0.5, rely=0.3, anchor=CENTER)

	mainMen = Button(lostGame, text="Main Menu", command=mainMenu)
	mainMen.place(relx=0.5, rely=0.5, anchor=CENTER)

	quitBtn = Button(lostGame, text= "Quit", command=quit)
	quitBtn.place(relx=0.5, rely=0.8, anchor=CENTER)

def liveLoss():
	gameWindow.destroy()
	global liveWindow
	liveWindow = tkinter.Tk()
	liveWindow.title("Live Lost")
	liveWindow.geometry("250x150")

	li = Label(liveWindow, text="Unfortunately you triggered a mine\n Many innocents were killed\n But at least youre still alive to try again!")
	li.pack(side=TOP)

	con = Button(liveWindow, text="Continue on", command=campaign)
	con.pack(side=BOTTOM)

def explosion():
	global explosionWindow
	colors = ("red", "brown", "yellow")
	explosionWindow = tkinter.Tk()
	explosionWindow.title("EXPLOSION!!!")
	explosionWindow.geometry("300x300")

	colorSwap(explosionWindow, colors, 2,0)
def colorSwap(window, colors, counter, timer):
	try:
		window.config(bg = colors[counter])
	except:
		return	
	if(timer == 50):
		window.destroy()
	if(counter > 0 ):	
		explosionWindow.after(100, colorSwap, window, colors, counter-1, timer+1)
	else:
		explosionWindow.after(100, colorSwap, window, colors, 2, timer+1)	
def campaign():
	try:
		root.destroy()
	except:
		print()
	try:
		gameWindow.destroy()
	except:
		print()	
	try:
		liveWindow.destroy()
	except:
		print()				
	global level
	global lives
	global campaignWindow
	global na
	na = 0
	
	campaignWindow = tkinter.Tk()
	campaignWindow.title("Minesweep Level " + str(level))
	campaignWindow.geometry("400x200")
	x1 = 0
	miner = 0
	if(level == 0):
		lives = 3
		na = Entry(campaignWindow)
		na.place(relx=0.5, rely=0.5, anchor=CENTER)
		na.insert(0, "Name Here")
	mineArr = 0

	if (level == 0):
		level += 1

	if (level == 1):
		Intro = Label(campaignWindow, text="Welcome to your Minesweep adventure!\n Hit continue below to get to your first minefield and start clearing land\n You can hit three mines before you are fired from your job")
		Intro.pack(side=TOP)
		mineArr = [[1,1,1], [1,"*",1], [1,1,1]]
		x1=3
		miner=1
		cont = Button(campaignWindow, text="Continue", command=lambda x=x1, mine=miner: gameplay(x,mine, mineArr))
		cont.place(relx=0.5, rely=0.8, anchor=CENTER)
	elif(level == 2):
		Intro = Label(campaignWindow, text="Congratulations on clearing your first minefield!\n Its only going to get harder from here.")
		Intro.pack(side = TOP)
		mineArr = [["*",2,1,0,0],[2,"*",2,1,0],[1,2,"*",2,1],[0,1,2,"*",2],[0,0,1,2,"*"]]
		x1=5
		miner=5
		cont = Button(campaignWindow, text="Continue", command=lambda x=x1, mine=miner: gameplay(x,mine, mineArr))
		cont.place(relx=0.5, rely=0.8, anchor=CENTER)
	elif(level == 3):
		Intro = Label(campaignWindow, text="This will be your first random minefield\n The corners will always be safe\n So if you dont have any moves just go to the corners")
		Intro.pack(side = TOP) 
		x1 = 5
		miner = 5
		cont = Button(campaignWindow, text="Continue", command=lambda x=x1, mine=miner: gameplay(x,mine, 0))
		cont.place(relx=0.5, rely=0.8, anchor=CENTER)
	elif(level > 3):
		Intro = Label(campaignWindow, text="Good Job Out There!\n Another random minefield coming up\n Bigger than the last")
		Intro.pack(side = TOP) 
		x1 = level + 2
		if (level < 7):
			miner = ((level*level)/2)
			miner = round(miner)
		else:
			miner = ((level*level)/2) + level	
			miner = round(miner)

		cont = Button(campaignWindow, text="Continue", command=lambda x=x1, mine=miner: gameplay(x,mine, 0))
		cont.place(relx=0.5, rely=0.8, anchor=CENTER)

	liveLbl = Label(campaignWindow, text="You have " + str(lives) +" lives left")
	liveLbl.place(relx=0.5, rely=0.4, anchor=CENTER)

def campaignLost():
	gameWindow.destroy()
	global lossWindow
	global name
	lossWindow = tkinter.Tk()
	lossWindow.title("Defeat")
	lossWindow.geometry("400x150")

	print (name)
	file = open("leaderboard.txt", "a")
	file.write(str(name) + '\n')
	file.write(str(level) + '\n')
	file.close()

	defLabel = Label(lossWindow, text="This is the end of your career as a Minesweeper\n You have wasted everybodies time by\n failing to clear out the dangerous bombs\n Too many innocents to count are dead\n Shame on you")
	defLabel.pack(side=TOP)

	manMenu= Button(lossWindow,text="Main Menu", command=mainMenu)
	manMenu.pack(side=BOTTOM)

	qut = Button(lossWindow, text="Quit", command=quit)
	qut.pack(side=BOTTOM)

def ldrBoard():
	root.destroy()
	global leaderWindow
	leaderWindow = tkinter.Tk()
	leaderWindow.title("Leaderboard")
	leaderWindow.geometry("300x500")

	if(os.path.exists("leaderboard.txt") == False):
		file2 = open("leaderboard.txt", "w")
		file2.close


	length = file_len("leaderboard.txt")
	file = open("leaderboard.txt", "r")
	lbl = Label(leaderWindow, text="Top Ten scores")
	lbl.pack(side=TOP)
	leaders = [0 for x in range(int(length/2))]
	nameLbls = [0 for x in range(10)]
	scoreLbls = [0 for x in range(10)]

	frame = Frame(leaderWindow)
	
	for x in range(int(length/2)):
		leaders[x] = (file.readline(), file.readline())
	file.close()
	leaders.sort(key=scoreSorter, reverse=True)

	listSize = 0
	if(length/2 > 10):
		listSize = 10
	else:
		listSize = length/2

	if (listSize==0):
		noth = Label(frame, text="There are no entries yet")
		noth.grid(row=0, column=0)
	for x in range(int(listSize)):	
		nameLbls[x] = Label(frame, text=str(leaders[x][0]))
		scoreLbls[x] = Label(frame, text=str(leaders[x][1]))
		nameLbls[x].grid(row=x, column=0)
		scoreLbls[x].grid(row=x, column=5)


	frame.pack(side=TOP)
	backButton = Button(leaderWindow, text="Back", command=mainMenu)
	backButton.pack(side=BOTTOM)

def file_len(fname):
	if os.stat(fname).st_size == 0:
		return 0
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def scoreSorter(list):
	return int(list[1])

def mainMenu():
	try:
		leaderWindow.destroy()
	except:
		print()
	try:
		lostGame.destroy()
	except:
		print()
	try:
		lossWindow.destroy()
	except:
		print()
	try:
		wonGame.destroy()
	except:
		print()

	global flag
	global lives
	global level
	global name
	global root
	name = 0
	level = 0
	lives = 0
	root = tkinter.Tk()
	root.geometry("300x400")
	root.title('Shitty Minesweeper')

	flag = Image.open("minesweeperFlag.png")
	flag = flag.resize((50,50))
	flag = ImageTk.PhotoImage(flag)

	title = Label(text="Shitty Minesweeper")
	title.pack(side = TOP)

	label = Label(image=flag)
	label.image = flag
	label.pack(side = TOP)

	campBtn = Button(root, text="Campaign", command=campaign)
	campBtn.place(relx=0.5, rely=0.3, anchor=CENTER)

	startBtn = Button(root, text="Quick Play", command=settings)
	startBtn.place(relx=0.5, rely=0.475, anchor=CENTER)

	instructBtn = Button(root, text="Instructions", command=instructions)
	instructBtn.place(relx=0.5, rely=0.65, anchor=CENTER)

	leaderboardBtn = Button(root, text="Leaderboard", command=ldrBoard)
	leaderboardBtn.place(relx=0.5, rely=0.8, anchor=CENTER)

	quitBtn = Button(root, text="Quit", command=quit)
	quitBtn.place(relx=0.5, rely=0.95, anchor=CENTER)


	root.mainloop()

mainMenu()