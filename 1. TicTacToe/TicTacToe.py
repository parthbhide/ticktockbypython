from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Global Variables
activeplayer = 1
p1 = []
p2 = []
winner = -1

root=Tk()
root.title("Tic Tac Toe : Player 1")
root.resizable(False,False)
bu1 = ttk.Button(root,text = ' ')
bu1.grid(row=0,column=0,ipadx=45,ipady=45)
bu1.config(command= lambda: BuClicked(1))
bu2 = ttk.Button(root,text = ' ')
bu2.grid(row=0,column=1,ipadx=45,ipady=45)
bu2.config(command= lambda: BuClicked(2))
bu3 = ttk.Button(root,text = ' ')
bu3.grid(row=0,column=2,ipadx=45,ipady=45)
bu3.config(command= lambda: BuClicked(3))
bu4 = ttk.Button(root,text = ' ')
bu4.grid(row=1,column=0,ipadx=45,ipady=45)
bu4.config(command= lambda: BuClicked(4))
bu5 = ttk.Button(root,text = ' ')
bu5.grid(row=1,column=1,ipadx=45,ipady=45)
bu5.config(command= lambda: BuClicked(5))
bu6 = ttk.Button(root,text = ' ')
bu6.grid(row=1,column=2,ipadx=45,ipady=45)
bu6.config(command= lambda: BuClicked(6))
bu7 = ttk.Button(root,text = ' ')
bu7.grid(row=2,column=0,ipadx=45,ipady=45)
bu7.config(command= lambda: BuClicked(7))
bu8 = ttk.Button(root,text = ' ')
bu8.grid(row=2,column=1,ipadx=45,ipady=45)
bu8.config(command= lambda: BuClicked(8))
bu9 = ttk.Button(root,text = ' ')
bu9.grid(row=2,column=2,ipadx=45,ipady=45)
bu9.config(command= lambda: BuClicked(9))


#ID Function
def BuClicked(id):
    global activeplayer
    global p1
    global p2
    if(activeplayer==1):
        p1.append(id)
        SetLayout(id,'X')
        root.title("Tic Tac Toe : Player 2")
        print("P1 : {}".format(p1))
        activeplayer=2
    elif (activeplayer == 2):
        p2.append(id)
        SetLayout(id, 'O')
        root.title("Tic Tac Toe : Player 1")
        print("P2 : {}".format(p2))
        activeplayer = 1
    CheckWinner()

#Set Layout
def SetLayout(b_id,PlayerSymbol):
    if b_id ==1:
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])
    elif b_id==2:
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
    elif b_id==3:
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
    elif b_id==4:
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])
    elif b_id==5:
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])
    elif b_id==6:
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])
    elif b_id==7:
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
    elif b_id==8:
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])
    elif b_id==9:
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])

#Game Rules and checking winner
def CheckWinner():
    global winner
    global p1
    global p2
    if((1 in p1) and (2 in p1) and (3 in p1)):
        winner = 1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title="Game Over !",message="Player 1 Wins !!")
        RestartGame()
    elif winner ==2:
        messagebox.showinfo(title="Game Over !", message="Player 2 Wins !!")
        RestartGame()

#Restart Game
def RestartGame():
    global p1
    global p2
    global activeplayer
    global winner
    for b_id in p1:
        if b_id == 1:
            bu1.config(text=' ')
            bu1.state(['!disabled'])
        elif b_id == 2:
            bu2.config(text=' ')
            bu2.state(['!disabled'])
        elif b_id == 3:
            bu3.config(text=' ')
            bu3.state(['!disabled'])
        elif b_id == 4:
            bu4.config(text=' ')
            bu4.state(['!disabled'])
        elif b_id == 5:
            bu5.config(text=' ')
            bu5.state(['!disabled'])
        elif b_id == 6:
            bu6.config(text=' ')
            bu6.state(['!disabled'])
        elif b_id == 7:
            bu7.config(text=' ')
            bu7.state(['!disabled'])
        elif b_id == 8:
            bu8.config(text=' ')
            bu8.state(['!disabled'])
        elif b_id == 9:
            bu9.config(text=' ')
            bu9.state(['!disabled'])
    for b_id in p2:
        if b_id == 1:
            bu1.config(text=' ')
            bu1.state(['!disabled'])
        elif b_id == 2:
            bu2.config(text=' ')
            bu2.state(['!disabled'])
        elif b_id == 3:
            bu3.config(text=' ')
            bu3.state(['!disabled'])
        elif b_id == 4:
            bu4.config(text=' ')
            bu4.state(['!disabled'])
        elif b_id == 5:
            bu5.config(text=' ')
            bu5.state(['!disabled'])
        elif b_id == 6:
            bu6.config(text=' ')
            bu6.state(['!disabled'])
        elif b_id == 7:
            bu7.config(text=' ')
            bu7.state(['!disabled'])
        elif b_id == 8:
            bu8.config(text=' ')
            bu8.state(['!disabled'])
        elif b_id == 9:
            bu9.config(text=' ')
            bu9.state(['!disabled'])
    p1 = []
    p2 = []
    activeplayer = 1
    winner = -1
    root.title("Tic Tac Toe : Player 1")

root.mainloop()