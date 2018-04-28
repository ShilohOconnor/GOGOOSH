from turtle import *
import random

setup(500, 500)
Screen()
title("GOGOOSH")
boolman = False
colors  = ["orange","dark orange","orange red","red","dark red", "black", "gray68"]
linewidth = input("what line thickness, 1-50?")
howlong = input("how long do you want this to iterate, 1-2000?")
move = Turtle()

#showturtle()

print(move.pos())
randlist = list()

move.width(linewidth)
def automatemyturtleleft():
    color = random.choice(colors)
    move.left(random.randint(1,45))
    move.forward(random.randint(1,69))
    move.color(color)
def automatemyturtleright():
    color = random.choice(colors)
    move.right(random.randint(1,45))
    move.forward(random.randint(1,69))
    move.color(color)
for x in range(int(howlong)):
  randlist.append(random.randint(1,99))
for x in range(int(howlong)):
    if 100 > randlist[x]> 80:
            automatemyturtleleft()
    elif 80 > randlist[x] > 60:
            automatemyturtleright()
    elif 60 > randlist[x] > 40:
            automatemyturtleleft()
    elif 40 > randlist[x] > 20:
            automatemyturtleright()
            if move.xcor()or move.ycor()>100:
                move.penup()
                move.goto(random.randint(-200,200),random.randint(-200,200))
                move.pendown()
    elif randlist[x] ==1:
        if boolman == False:
            print('TIME FOR A COLOR SWAP')
            colors  = ["deep sky blue", "dodger blue", "blue", "royal blue", "medium blue"]
            boolman = True
        elif boolman -- True:
            colors  = ["white","orange","dark orange","orange red","red","dark red", "black", "white", "gray68"]
            print('TIME FOR A COLOR SWAP, BACK TO THE OG')
            boolman = False



#print(randlist)
print(move.pos())
listen()
mainloop()
