import turtle
import random
import time
pish = ''
dish = ''
fart = ''
pasa = turtle.Turtle()
eraser = turtle.Turtle()
eraser.color('white')
eraser.penup()
ws = turtle.Screen()
pasa.color('green')
pasa.penup()
pasa.setposition(300, 200)
pasa.pendown()
style=('Arial',40)
pasa.write('A', font=style, align='right')
pasa.penup()
pasa.color('red')
pasa.setposition(300,0)
pasa.pendown()
pasa.write('B', font=style, align='right')
pasa.penup()
pasa.color('blue')
pasa.setposition(300,-200)
pasa.pendown()
pasa.write('C', font=style, align='right')
pasa.color('black')
pasa.hideturtle()
huicho = turtle.Turtle()
huicho.penup()
huicho.setpos(-300,0)
huicho.pendown()
while True:
    stoinost=turtle.textinput('Choice','A,B or C')
    if stoinost!='A' and stoinost!='B' and stoinost!='C':
        continue
    if stoinost == pish:
        pasa.setpos(0,250)
        pasa.pendown()
        style =('Arial',20)
        pasa.write('Finder already knows the way to point A!', font=style, align='center')
        time.sleep(3)
        eraser.setpos(0,250)
        eraser.pendown()
        eraser.write('Finder already knows the way to point A!', font=style, align='center')
        style =('Arial',40)
        continue
    elif stoinost == dish:
        pasa.setpos(0,250)
        pasa.pendown()
        style =('Arial',20)
        pasa.write('Finder already knows the way to point B!', font=style, align='center')
        time.sleep(3)
        eraser.setpos(0,250)
        eraser.pendown()
        eraser.write('Finder already knows the way to point B!', font=style, align='center')
        style =('Arial',40)
        continue
    elif stoinost == fart:
        pasa.setpos(0,250)
        pasa.pendown()
        style =('Arial',20)
        pasa.write('Finder already knows the way to point C!', font=style, align='center')
        time.sleep(3)
        eraser.setpos(0,250)
        eraser.pendown()
        eraser.write('Finder already knows the way to point C!', font=style, align='center')
        style =('Arial',40)
        continue
    if stoinost == 'A':
        pish = stoinost
    elif stoinost == 'B':
        dish = stoinost
    elif stoinost == 'C':
        fart = stoinost
    a1=1
    a2=33
    b1=34
    b2=66
    c1=67
    c2=99
    counta = 0
    countb = 0
    countc = 0
    while True:
        trying = random.randint(1,99)
        if trying>=1 and trying<=a2:
            if stoinost=='A':
                huicho.color('green')
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                time.sleep(0.5)
                huicho.setpos(-300,200)
                time.sleep(0.5)
                huicho.setpos(300,200)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,250)
                pasa.pendown()
                pasa.write('Finder Guessed right!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,250)
                eraser.pendown()
                eraser.write('Finder Guessed right!', font=style, align='center')
                a2 +=2
                b1 +=2
                b2 +=1
                c1 +=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
                counta +=1
            else:
                huicho.color('green')
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                time.sleep(0.5)
                huicho.setpos(-300,200)
                time.sleep(0.5)
                huicho.setpos(300,200)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,-260)
                pasa.pendown()
                pasa.write('Finder Guessed wrong!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,-260)
                eraser.pendown()
                eraser.write('Finder Guessed wrong!', font=style, align='center')
                a2 -=2
                b1 -=2
                b2 -=1
                c1 -=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
        if trying>=b1 and trying<=b2:
            if stoinost=='B':
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                huicho.color('red')
                time.sleep(0.5)
                huicho.setpos(300,0)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,250)
                pasa.pendown()
                pasa.write('Finder Guessed right!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,250)
                eraser.pendown()
                eraser.write('Finder Guessed right!', font=style, align='center')
                b1 -=1
                b2 +=1
                a2 -=1
                c1 +=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
            else:
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                huicho.color('red')
                time.sleep(0.5)
                huicho.setpos(300,0)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,-260)
                pasa.pendown()
                pasa.write('Finder Guessed wrong!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,-260)
                eraser.pendown()
                eraser.write('Finder Guessed wrong!', font=style, align='center')
                b1 +=1
                b2+=1
                a2 +=1
                c1 -=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
        if trying>=c1 and trying<=99:
            if stoinost=='C':
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                huicho.color('blue')
                time.sleep(0.5)
                huicho.setpos(-300,-200)
                time.sleep(0.5)
                huicho.setpos(300,-200)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,250)
                pasa.pendown()
                pasa.write('Finder Guessed right!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,250)
                eraser.pendown()
                eraser.write('Finder Guessed right!', font=style, align='center')
                c1 -=2
                b2 -=2
                b1 -=1
                a2 -=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
            else:
                huicho.penup()
                huicho.setpos(-300,0)
                huicho.pendown()
                huicho.color('blue')
                time.sleep(0.5)
                huicho.setpos(-300,-200)
                time.sleep(0.5)
                huicho.setpos(300,-200)
                time.sleep(0.5)
                pasa.penup()
                pasa.setpos(0,-260)
                pasa.pendown()
                pasa.write('Finder Guessed wrong!', font=style, align='center')
                time.sleep(0.5)
                eraser.setpos(0,-260)
                eraser.pendown()
                eraser.write('Finder Guessed wrong!', font=style, align='center')
                c1 +=2
                b2 +=2
                b1+=1
                a2+=1
                if a2>99:
                    a2=99
                if b1<1:
                    b1=1
                if b2>99:
                    b2=99
                if c1<1:
                    c1=1
                if c2>99:
                    c2=99
        if a1==1 and a2==99:
            pasa.setpos(0,250)
            pasa.pendown()
            style =('Arial',20)
            pasa.write('Finder knows the path to point A!', font=style, align='center')
            time.sleep(3)
            eraser.setpos(0,250)
            eraser.pendown()
            eraser.write('Finder knows the path to point A!', font=style, align='center')
            style =('Arial',40)
            break
        elif b1==1 and b2==99:
            pasa.setpos(0,250)
            pasa.pendown()
            style =('Arial',20)
            pasa.write('Finder knows the path to point B!', font=style, align='center')
            time.sleep(3)
            eraser.setpos(0,250)
            eraser.pendown()
            eraser.write('Finder knows the path to point B!', font=style, align='center')
            style =('Arial',40)
            break
        elif c1==1 and c2==99:
            pasa.setpos(0,250)
            pasa.pendown()
            style =('Arial',20)
            pasa.write('Finder knows the path to point C!', font=style, align='center')
            time.sleep(3)
            eraser.setpos(0,250)
            eraser.pendown()
            eraser.write('Finder knows the path to point C!', font=style, align='center')
            style =('Arial',40)
            break
