from tkinter import *
import random

# https://pypi.org/project/tkmacosx/
# pip3 install tkmacosx
from tkmacosx import Button

currRow = []
listRows = []
hintRow = []
listHintRows = []
solution = []

numAttempts = 10

colors = ['red', 'cyan', 'purple', 'orange', 'yellow', 'green']


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


def RandSolution():
    global solution
    for i in range(4):
        solution.append(colors[random.randint(0, len(colors) - 1)])

# ==================================================================================================================================

def DrawRow(thisRow, row = 0, col = 0):
    global currRow
    global listRows
    global hintRow
    global listHintRows

    offset = 20
    size = 20
    spacing = 25

    # draw the current row

    for color in thisRow:
        canvas1.create_oval(spacing * col + offset,
                            spacing * row + offset,
                            spacing * col + size + offset,
                            spacing * row + size + offset, fill=color)
        col += 1
    pass


# ==================================================================================================================================

def DrawBoard():
    global currRow
    global listRows
    global hintRow
    global listHintRows

    # draw the rows of colors
    for i in range(len(listRows)):
        DrawRow(listRows[i], i)
        DrawRow(listHintRows[i], i, 6)


    # draw the solution... just for testing.
    DrawRow(solution, 12)

    #DrawRow(emptyRow, len(listRows)+1)

    pass

# ==================================================================================================================================

def AddColor(c):
    global currRow
    global listRows
    global hintRow
    global listHintRows

    if len(currRow) < 4:
        currRow.append(c)
    DrawRow(currRow, len(listRows))

    print(currRow)

    #DrawBoard()

    pass

# ==================================================================================================================================

def Delete():
    global currRow
    global listRows
    global hintRow
    global listHintRows


    #del listRows[-1]
    currRow.clear()
    DrawRow(emptyRow, len(listRows))

    #DrawBoard()
    pass

# ==================================================================================================================================

def Reset():
    global currRow
    global listRows
    global hintRow
    global listHintRows

    currRow.clear()

    DrawBoard()
    pass

# ==================================================================================================================================

def Check():
    global currRow
    global listRows
    global hintRow
    global listHintRows

    if len(currRow) == 4:
        listRows.append(currRow.copy())
        tempSol = []
        tempRow = []
        for i in range(4):
            if currRow[i] == solution[i]:
                hintRow.append('black')
            else:
                tempRow.append(currRow[i])
                tempSol.append(solution[i])
        for i in range(len(tempRow)):
            if tempRow[i] in tempSol:
                hintRow.append('pink')
                tempSol.remove(tempRow[i])
                tempRow[i] = ''

        listHintRows.append(hintRow.copy())

        print(hintRow)
        print(listHintRows)

        DrawBoard()

        if (len(hintRow)==4 and not 'pink' in hintRow):
            print("you win")
            pass
        elif (len(listRows) > numAttempts):
            print('you lose')
            pass
        else:
            DrawRow(emptyRow, len(listRows))
            currRow.clear()
            hintRow.clear()

    pass


# ==================================================================================================================================
# ==================================================================================================================================
# ==================================================================================================================================


root = Tk()
root.title("MasterMind")
root.configure(background='white')

frame1 = Frame(root, bg='sky blue', bd=10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width=400, height=400)
canvas1.pack()

frame2 = Frame(root)

c1 = Button(frame2, text=colors[0], borderless=1, bg=colors[0], command=lambda: AddColor(colors[0]))
c1.pack(side=LEFT)

c2 = Button(frame2, text=colors[1], borderless=1, bg=colors[1], command=lambda: AddColor(colors[1]))
c2.pack(side=LEFT)

c3 = Button(frame2, text=colors[2], borderless=1, bg=colors[2], command=lambda: AddColor(colors[2]))
c3.pack(side=LEFT)

c4 = Button(frame2, text=colors[3], borderless=1, bg=colors[3], command=lambda: AddColor(colors[3]))
c4.pack(side=LEFT)

c5 = Button(frame2, text=colors[4], borderless=1, bg=colors[4], command=lambda: AddColor(colors[4]))
c5.pack(side=LEFT)

c6 = Button(frame2, text=colors[5], borderless=1, bg=colors[5], command=lambda: AddColor(colors[5]))
c6.pack(side=LEFT)


b3 = Button(frame2, text="Reset", command=Reset)
b3.pack(side=RIGHT)

b1 = Button(frame2, text="Delete", command=Delete)
b1.pack(side=RIGHT)

b2 = Button(frame2, text="Check", command=Check)
b2.pack(side=RIGHT)

frame2.pack(side=BOTTOM)


RandSolution()

DrawRow(solution, 12)

emptyRow = ['white', 'white', 'white', 'white']

DrawRow(emptyRow, len(listRows))


# ==================================================================================================================================

mainloop()
