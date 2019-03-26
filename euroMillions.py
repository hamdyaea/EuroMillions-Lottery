#!/usr/bin/python3

# developer : Hamdy Abou El Anein

# If you don't see the pictures install pillow with #pip3 install pillow

from easygui import *
import random
import sys



ticket = "./images/ticketfull1.gif"


def lottery():
    inputNum = 50
    outputNum = list(range(inputNum + 1))
    outputNum.remove(0)
    inputSta = 12
    outputSta = list(range(inputSta + 1))
    outputSta.remove(0)

    numbers = random.shuffle(outputNum)

    stars = random.shuffle(outputSta)

    top5 = outputNum[:5]
    top2 = outputSta[:2]

    top5.sort()
    top2.sort()



    lotChoice = ["Replay"]

    text = ("Numbers : " +str(top5[0])+str(",")+ str(top5[1])+str(",")\
           + str(top5[2])+str(",")+ str(top5[3])+str(",")+ str(top5[4])\
           +str(" \nStars : " +str(top2[0])+str(",")+str(top2[1])))

    replay = buttonbox(image=ticket,choices=lotChoice,title="List of numbers to play", msg=text)
    if replay == "Replay":
        lottery()
    else :
        sys.exit(0)

logoLoto = "./images/loto.gif"
msg = "Do you want to play ?"
choices = ["Yes","No"]

begining = buttonbox(msg,image=logoLoto,choices=choices)

if begining == "Yes":
    lottery()
else :
    sys.exit(0)




