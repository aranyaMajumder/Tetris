import time

import characters
import os
import random as r
import keyboard
import starting_screen

s = starting_screen.Start()
b,i=s.select("left",1)
print(s.p)

print(b)
i=0
while True:
    if keyboard.read_key()=='enter' and i==0:
        break
    elif keyboard.read_key()=='a':
        b,i = s.select("left", i)
        print(s.p)
        
        print(b)
        
    elif keyboard.read_key()=="d":
        b,i = s.select("right", i)
        print(s.p)
        
        
        print(b)

board = [] #20 x 20
# board[y][x] = "#" to set a character '#' in x,y

for i in range(20):# empty rows
    arr = []
    for j in range(20):
        arr.append(" ")
    board.append(arr)

def clearblock(board,shape,shapeb,shapec,y,x):
    for i in range(3):
        if shape[i]=="*" and y-1>-1:
            board[y-1][x-1+i]=" "
    for i in range(3):
        if shapeb[i]=="*" and y>-1:
            board[y][x-1+i]=" "   
    for i in range(3):
        if shapec[i]=="*":
            board[y+1][x-1+i]=" "
    return board
def nextC(board, y, x,shapeb,  shapec):
    for i in range(3):
        if shapec[i]=="*":
            if board[y+1][x-1+i]=="\u2588":
                return 1
    for i in range(3):
        if shapeb [i]=="*":
            if board[y][x-1+i]=="\u2588" and i!=1:
                return 1
    for i in range(3):
        if shape[i]=="*" and shapeb[i]!="*":
            if board[y-1][x-1+i]=="\u2588" and i!=1:
                return 1


def fillblocks(board, y, x, shapeb, shapec, shape, c):

    h = 0
    for q in range(3):
        if shapec[q]=="*":
            board[y][x-1+q]=" "
    for q in range(3):
        if shapeb[q]=="*":   
            board[y-1][x-1+q]=" "
    for q in range(3):
        if shape[q]=="*":
            board[y-2][x-1+q]=" "
    if nextC(board,y+1,spawn_x,shapeb, shapec)==1:
        h = 1
    for i in range(3):
        if shape[i]=="*":
            board[y-1][x-1+i]="\u2588"
    for i in range(3):
        if shapeb[i]=="*":
            board[y][x-1+i]="\u2588"
    for j in range(3):
        if shapec[j]=="*":

            board[y+1][x-1+j]="\u2588"

    return board, h




def refresh(board,score):
    os.system("cls")
    print(" "*20 +str(score))
    row = " "*30
    for y in range(20):
        row=" "*10
        for x in range(20):
            #print(y, x)
            row += board[y][x]
        print(row)

T = characters.T
L = characters.L
score = 0
while True:    # main game
    for i in range(20):
        if board[0][i]!=" ":
            refresh(board, score)
            print("Game Over!")
            exit()   
    score+=1
    ex=0    
    spawn_x = r.randint(2,17)
    rand_character = r.randint(1,2)
    rand_rotation = r.randint(0,2)
    if rand_character==1:
        shape = T.shape[rand_rotation][0]
        shapeb = T.shape[rand_rotation][1]
        shapec = T.shape[rand_rotation][2]
    else:
        shape = L.shape[rand_rotation][0]
        shapeb = L.shape[rand_rotation][1]
        shapec = L.shape[rand_rotation][2]
    flag = True
    i=0
    t = time.time()
    while True:
        ex=0
        if i>16:
            break
        if time.time()>=t+0.5 or flag==True:
            board, ex = fillblocks(board,i+1,spawn_x,shapeb,shapec,shape, "n")
            refresh(board,score)            
            flag = False
            t=time.time()
            i+=1
        if keyboard.is_pressed('a'):
            if board[i][spawn_x-1]==" " or board[i][spawn_x-2]==" ":
                if board[i+1][spawn_x-2]==" " or board[i+1][spawn_x-2]==" ":
                    if board[i+2][spawn_x-2]==" " or board[i+2][spawn_x-2]==" ":
                        board = clearblock(board,shape,shapeb,shapec,i,spawn_x)
                        spawn_x-=1
                        board, ex = fillblocks(board,i, spawn_x, shapeb,shapec,shape, "l")
                        refresh(board,score)
                        
        if keyboard.is_pressed('d'):
            if spawn_x<18:
                if board[i][spawn_x+1]==" " or board[i][spawn_x+2]==" ":
                    if board[i+1][spawn_x+2]==" " or board[i+1][spawn_x+2]==" ":
                        if board[i+2][spawn_x+2]==" " or board[i+2][spawn_x+2]==" ":
                            board = clearblock(board,shape,shapeb,shapec,i,spawn_x)
                            spawn_x+=1
                            board, ex = fillblocks(board,i, spawn_x, shapeb,shapec,shape, "r")
                            refresh(board,score)
                            
         
        
        if ex == 1:
            break
