import pyttsx3
import random
from random import *
import turtle
import datetime
from datetime import datetime
import time
from playsound import playsound
import requests
import math
import sys
import urllib.parse
import webbrowser

print("Yo yo yo, what's up home slice! I'm Ziri, your virtual assistant. Type what you want me to do. To see the list of skillz I can has, type help.")
engine = pyttsx3.init()
engine.setProperty("rate",200)
engine.say("Yo yo yo, what's up home slice! I'm Ziri, your virtual assistant. Type what you want me to do. To see the list of skillz I can has, type help.")
engine.runAndWait()
ics = False
gp = 0

while True:
    x = input("Type what you want me to do here. ")
    x = x.lower()
    n = randint(1,5)
    if n == 1:
        engine.setProperty("rate",200)
        print("You've got mail!")
        engine.say("You've got mail!")
        engine.runAndWait()
        print("Just kidding!")
        engine.say("Just kidding!")
        engine.runAndWait()

    if x == "time":
        now = datetime.now()
        s = str(now.second)
        if s == "0" or s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9":
            s = "0" + s
        mn = str(now.minute)
        if mn == "0" or mn == "1" or mn == "2" or mn == "3" or mn == "4" or mn == "5" or mn == "6" or mn == "7" or mn == "8" or mn == "9":
            mn = "0" + mn
        h = str(now.hour)
        d = now.day
        mo = now.month
        y = now.year
        print ("%s/%s/%s %s:%s:%s" % (mo,d,y,h,mn,s))
        h = str(h)
        mn = str(mn)
        
        if mo == 1:
            mo = "January"
        
        elif mo == 2:
            mo = "February"
        
        elif mo == 3:
            mo = "March"
        
        elif mo == 4:
            mo = "April"
        
        elif mo == 5:
            mo = "May"
        
        elif mo == 6:
            mo = "June"
        
        elif mo == 7:
            mo = "July"
        
        elif mo == 8:
            mo = "August"
        
        elif mo == 9:
            mo = "September"
        
        elif mo == 10:
            mo = "October"
        
        elif mo == 11:
            mo = "November"
        
        elif mo == 12:
            mo = "December"
        

        if d == 1:
            d = "first"
            
        elif d == 2:
            d = "second"
            
        elif d == 3:
            d = "third"
            
        elif d == 4:
            d = "fourth"
            
        elif d == 5:
            d = "fifth"
            
        elif d == 6:
            d = "sixth"
            
        elif d == 7:
            d = "seventh"
            
        elif d == 8:
            d = "eighth"
            
        elif d == 9:
            d = "ninth"
            
        elif d == 10:
            d = "tenth"
            
        elif d == 11:
            d = "eleventh"
            
        elif d == 12:
            d = "twelfth"
            
        elif d == 13:
            d = "thirteenth"
            
        elif d == 14:
            d = "forteenth"
            
        elif d == 15:
            d = "fifteenth"
            
        elif d == 16:
            d = "sixteenth"
            
        elif d == 17:
            d = "seventeenth"
            
        elif d == 18:
            d = "eighteenth"
            
        elif d == 19:
            d = "ninteenth"
            
        elif d == 20:
            d = "twentieth"
            
        elif d == 21:
            d = "twenty first"
            
        elif d == 22:
            d = "twenty second"
            
        elif d == 23:
            d = "twenty third"
            
        elif d == 24:
            d = "twenty fourth"
            
        elif d == 25:
            d = "twenty fifth"
            
        elif d == 26:
            d = "twenty sixth"
            
        elif d == 27:
            d = "twenty seventh"
            
        elif d == 28:
            d = "twenty eighth"
            
        elif d == 29:
            d = "twenty ninth"
            
        elif d == 30:
            d = "thirtieth"
            
        elif d == 31:
            d = "thirty first"

        y = str(y)
        engine.say("It is" + h + mn + ", on" + mo + d + "," + y)
        engine.runAndWait()

    elif x == "fortune":
        engine.setProperty("rate",200)
        f = randint(1, 20)
        engine.say("Ask a yes or no question and I will try to answer it.")
        engine.runAndWait() 
        y = input("Ask a yes or no question and I will try to answer it. ")
        
        if f == 1:
            print("It is certain.")
            engine.say("It is certain.")
            engine.runAndWait() 
            
        if f == 2:
            print("It is decidedly so.")
            engine.say("It is decidedly so.")
            engine.runAndWait() 
        
        if f == 3:
            print("Without a doubt.")
            engine.say("Without a doubt.")
            engine.runAndWait() 
        
        if f == 4:
            print("Yes - definitely.")
            engine.say("Yes - definitely.")
            engine.runAndWait() 
        
        if f == 5:
            print("You may rely on it.")
            engine.say("You may rely on it.")
            engine.runAndWait() 
        
        if f == 6:
            print("As I see it, yes.")
            engine.say("As I see it, yes.")
            engine.runAndWait() 
        
        if f == 7:
            print("Most likely.")
            engine.say("Most likely.")
            engine.runAndWait() 
        
        if f == 8:
            print("Outlook good.")
            engine.say("Outlook good.")
            engine.runAndWait() 
        
        if f == 9:
            print("Yes.")
            engine.say("Yes.")
            engine.runAndWait() 
        
        if f == 10:
            print("Signs point to yes.")
            engine.say("Signs point to yes.")
            engine.runAndWait() 
        
        if f == 11:
            print("Reply hazy, try again.")
            engine.say("Reply hazy, try again.")
            engine.runAndWait() 
        
        if f == 12:
            print("Ask again later.")
            engine.say("Ask again later.")
            engine.runAndWait() 
        
        if f == 13:
            print("Better not tell you now.")
            engine.say("Better not tell you now.")
            engine.runAndWait()
        
        if f == 14:
            print("Cannot predict now.")
            engine.say("Cannot predict now.")
            engine.runAndWait()
        
        if f == 15:
            print("Concentrate and ask again.")
            engine.say("Concentrate and ask again.")
            engine.runAndWait()
        
        if f == 16:
            print("Don't count on it.")
            engine.say("Don't count on it.")
            engine.runAndWait()
        
        if f == 17:
            print("My reply is no.")
            engine.say("My reply is no.")
            engine.runAndWait()
        
        if f == 18:
            print("My sources say no.")
            engine.say("My sources say no.")
            engine.runAndWait()
        
        if f == 19:
            print("Outlook not so good.")
            engine.say("Outlook not so good.")
            engine.runAndWait()
        
        if f == 20:
            print("Very doubtful.")
            engine.say("Very doubtful.")
            engine.runAndWait()

    elif x == "timer":
        engine.setProperty("rate",200)
        engine.say("How many hours do you want your timer to be set for? Just a warning, you won't be able to use Ziri while the timer is running.")
        engine.runAndWait()
        j = input("How many hours do you want the timer to be set for? Just a warning, you won't be able to use Ziri while the timer is running. ")
        j = float(j) * 3600
        engine.say("How many minutes do you want your timer to be set for?")
        engine.runAndWait()
        k = input("How many minutes do you want your timer to be set for? ")
        k = float(k) * 60
        engine.say("How many seconds do you want your timer to be set for?")
        engine.runAndWait()
        l = input("How many seconds do you want your timer to be set for? ")
        l = float(l)
        time.sleep(j + k + l)
        print("Your timer is done.")
        engine.say("Bee bee bee boo boo. Bee bee bee boo boo. Your timer is done.")
        engine.runAndWait()

    elif x == "repeater":
        b = True
        print("Hello!")
        engine.say("Hello!")
        engine.runAndWait()
        engine.say("What word or phrase do you want me to repeat?")
        engine.runAndWait()
        r = input("What word or phrase do you want me to repeat? ")
        engine.say("How fast do you want me to say it? 200 is the normal speed, and please don't put in something that's not a number.")
        engine.runAndWait()
        rate = input("How fast do you want me to say it? (200 is the normal speed, and please don't put in something that's not a number.) ")
        try:
            rate = int(rate)
        except ValueError:
            print("WHAT DID I JUST SAY! REEEEE! You put in something that wasn't a number!")
            engine.say("WHAT DID I JUST SAY! REE! You put in something that wasn't a number!")
            engine.runAndWait()
            b = False
        if b == True:
            engine.say("How many times do you want me to repeat it? Again, please don't put something in that's not a number.")
            engine.runAndWait()
            n = input("How many times do you want me to repeat it? Again, please don't put something in that's not a number. ")
            try:
                n = int(n)
            except ValueError:
                print("WHAT DID I JUST SAY! REEEEE! You put in something that wasn't a number!")
                engine.say("WHAT DID I JUST SAY! REE! You put in something that wasn't a number!")
                engine.runAndWait()
                b = False
        if b == True:
            print("Here you go:")
            engine.say("Here you go:")
            engine.runAndWait()
            engine.setProperty("rate",int(rate))
            while n != 0:
                print(r)
                n = n - 1
                engine.say(r)
                engine.runAndWait()
            time.sleep(1)
            engine.setProperty("rate",200)
            print("Whew!")
            engine.say("Whew!")
            engine.runAndWait()

    elif x == "snake":
        #source: https://github.com/DCoelhoM/Snake-Python
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #                        Dinis Marques                            #
        #                         Snake Python                            #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        import turtle
        import random
        #head orientation
        h = [0]

        #score
        a = [0]
        b = [0]

        #food coord
        fcoord = [0,0,0]

        #position
        pos = []


        def home(x,y):
            x = 0
            y = 0
            a[0] = 0
            b[0] = 0
            h[0] = 0
            fcoord[2] = 0
            pos[:] = []
            turtle.hideturtle()
            turtle.clear()
            turtle.pu()
            turtle.color("black")
            turtle.goto(0,0)
            turtle.write("Play")
            turtle.title("Snake")
            turtle.onscreenclick(start)
            turtle.mainloop()

        def level_1():
            turtle.clear()
            turtle.pu()
            turtle.speed(0)
            turtle.pensize(20)
            turtle.color("grey")
            turtle.goto(-220,220)
            turtle.pd()
            turtle.goto(220,220)
            turtle.goto(220,-220)
            turtle.goto(-220,-220)
            turtle.goto(-220,220)
            turtle.pu()
            turtle.goto(0,0)

        def start(x,y):
            turtle.onscreenclick(None)

            level_1()

            tfood = turtle.Turtle()
            tfood.hideturtle()
            tfood.pu()
            tfood.speed(0)
            tfood.shape("square")
            tfood.color("red")

            tscore = turtle.Turtle()
            tscore.hideturtle()
            tscore.pu()
            tscore.speed(0)
            tscore.goto(100,-250)
            tscore.write("Score:" + str(a[0]), align="center",font=(10))
            
            while x > -210 and x < 210 and y > -210 and y <210:
                if fcoord[2] == 0:
                    food(tfood)
                    fcoord[2] = 1
                turtle.onkey(u,"Up")
                turtle.onkey(l,"Left")
                turtle.onkey(r,"Right")
                turtle.onkey(d,"Down")
                turtle.listen()
                move()
                x = turtle.xcor()
                y = turtle.ycor()        
                if x > fcoord[0]*20-5 and x < fcoord[0]*20+5 and y > fcoord[1]*20-5 and y < fcoord[1]*20+5:
                    fcoord[2] = 0
                    tfood.clear()
                    a[0] += 1
                    tscore.clear()
                    tscore.write("Score:" + str(a[0]), align="center",font=(10))
                
                if len(pos) > 1:
                    for i in range(1,len(pos)):
                        if x < pos[i][0]+5 and x > pos[i][0]-5 and y < pos[i][1]+5 and y > pos[i][1]-5:
                                tscore.clear()
                                tfood.clear()
                                gameover()
            tscore.clear()
            tfood.clear()
            gameover()


        #Food
        def food(tfood):
            x = random.randrange(-8,8,1)
            y = random.randrange(-8,8,1)
            fcoord[0] = x
            fcoord[1] = y
            tfood.hideturtle()
            tfood.pu()
            tfood.shape("square")
            tfood.color("red")
            tfood.goto(x*20,y*20)
            tfood.stamp()

        #Up   
        def u():
            if h[0] == 270:
                pass
            else:
                h[0] = 90
        #Down
        def d():
            if h[0] == 90:
                pass
            else:
                h[0] = 270
        #Left
        def l():
            if h[0] == 0:
                pass
            else:
                h[0] = 180
        #Right
        def r():
            if h[0] == 180:
                pass
            else:
                h[0] = 0

        def move():
            turtle.pensize(1)
            turtle.color("black")
            turtle.pu()
            turtle.speed(3)
            turtle.setheading(h[0])
            turtle.shape("square")
            turtle.stamp()
            turtle.fd(20)
            x = turtle.xcor()
            y = turtle.ycor()
            if b[0] > a[0]:     
                turtle.clearstamps(1)
                pos.insert(0,[round(x),round(y)])
                pos.pop(-1)
            else:
                pos.insert(0,[round(x),round(y)])       
                b[0] += 1    
            
        def gameover():
            turtle.onscreenclick(None)
            turtle.speed(0)
            turtle.pu()
            turtle.goto(0,150)
            turtle.color("red")
            turtle.write("Game Over",align="center", font=(10))
            turtle.goto(0,50)
            turtle.write("Score:" + str(a[0]),align="center",font=(10))
            turtle.goto(200,-200)
            turtle.write("(Click anywhere to return to the main menu)",align="right",font=(0.0000001))
            turtle.onscreenclick(home)
            turtle.mainloop()
            
                
        # # # # # # # # # # # # # # # # # # # # # #
        # Main                                    #
        # # # # # # # # # # # # # # # # # # # # # #
        if __name__ == '__main__':
            home(0,0)

    elif x == "joke":
        j = randint(1,20)
        engine.setProperty("rate",200)
        if j == 1:
            print("What do you call a cow with no legs? Ground beef.")
            engine.say("What do you call a cow with no legs? Ground beef.")
            engine.runAndWait()

        elif j == 2:
            print("Yo mama so old, she knew Mr. Clean when he had an afro!")
            engine.say("Yo mama so old, she knew Mr. Clean when he had an afro!")
            engine.runAndWait()

        elif j == 3:
            print("Yo mama so old, she walked out of a museum and the alarm went off!")
            engine.say("Yo mama so old, she walked out of a museum and the alarm went off!")
            engine.runAndWait()

        elif j == 4:
            print("What do you call a short fortune teller that's hiding from the police? A small medium at large.")
            engine.say("What do you call a short fortune teller that's hiding from the police? A small medium at large.")
            engine.runAndWait()

        elif j == 5:
            print("What happened when Chicago and Boston shared a washing machine? They became the Pink Sox.")
            engine.say("What happened when Chicago and Boston shared a washing machine? They became the Pink Sox.")
            engine.runAndWait()

        elif j == 6:
            print("Why is Carmen San Diego so bad at basketball? She's always traveling.")
            engine.say("Why is Carmen San Diego so bad at basketball? She's always traveling.")
            engine.runAndWait()

        elif j == 7:
            print("Yo mama so hairy, shih tzus make fun of her!")
            engine.say("Yo mama so hairy, shih tzus make fun of her!")
            engine.runAndWait()

        elif j == 8:
            print("What's the difference between a fat guy and a skinny guy running a marathon? One runs in short bursts. The other runs in burst shorts.")
            engine.say("What's the difference between a fat guy and a skinny guy running a marathon? One runs in short bursts. The other runs in burst shorts.")
            engine.runAndWait()

        elif j == 9:
            print('The Lord said unto John, "Come forth, and recieve eternal life." John came fifth, and recieved a toaster.')
            engine.say("The Lord said unto John, Come forth, and recieve eternal life. John came fifth, and recieved a toaster.")
            engine.runAndWait()

        elif j == 10:
            print('"Waiter, this coffee tastes like mud!" "Yes, it\'s fresh ground."')
            engine.say('"Waiter, this coffee tastes like mud!" "Yes, it\'s fresh ground."')
            engine.runAndWait()

        elif j == 11:
            print("What has three teeth and sixty feet? The front row at a Willy Nelson concert.")
            engine.say("What has three teeth and sixty feet? The front row at a Willy Nelson concert.")
            engine.runAndWait()

        elif j == 12:
            print("Did you hear about the man who ran through a screen door? He strained himself.")
            engine.say("Did you hear about the man who ran through a screen door? He strained himself.")
            engine.runAndWait()

        elif j == 13:
            print("A magician was driving down the road... then he turned into a driveway.")
            engine.say("A magician was driving down the road... then he turned into a driveway.")
            engine.runAndWait()

        elif j == 14:
            print("Women who wear $200 perfumes are obviously known to have no common scents.")
            engine.say("Women who wear 200 dollar perfumes are obviously known to have no common scents.")
            engine.runAndWait()

        elif j == 15:
            print("Did you hear about the dyslexic Satanist? He sold his soul to Santa.")
            engine.say("Did you hear about the dyslexic Satanist? He sold his soul to Santa.")
            engine.runAndWait()

        elif j == 16:
            print("Did you hear about the butcher who backed into his meat grinder? He got a little behind in his work.")
            engine.say("Did you hear about the butcher who backed into his meat grinder? He got a little behind in his work.")
            engine.runAndWait()

        elif j == 17:
            print("Did you hear about the cheese factory that exploded in France? There was nothing left but de Brie.")
            engine.say("Did you hear about the cheese factory that exploded in France? There was nothing left but de Brie.")
            engine.runAndWait()

        elif j == 18:
            print("What do you call a Frenchman wearing sandals? Phillipe Phillope.")
            engine.say("What do you call a Frenchman wearing sandals? Fileep Filop.")
            engine.runAndWait()

        elif j == 19:
            print('One cow asks another cow, "Are you afraid of mad cow disease?" The other cow answers, "Why should I be? I\'m a helicopter."')
            engine.say("One cow asks another cow, Are you afraid of mad cow disease? The other cow answers, Why should I be? I'm a helicopter.")
            engine.runAndWait()

        elif j == 20:
            print("Yo mama's so fat, even Dora can't explore her!")
            engine.say("Yo mama's so fat, even Dora can't explore her!")
            engine.runAndWait()

    elif x == "poem":
        p = randint(1,10)
        engine.setProperty("rate",200)
        if p == 1:
            print('''Roses are red,
My name is Dave,
This makes no sense,
Microwave.''')
            engine.say("Roses are red, my name is Dave, this makes no sense, microwave.")
            engine.runAndWait()
        
        elif p == 2:
            print('''Roses are red,
Violets are blue,
I suck at rhyming,
Potatoes.''')
            engine.say("Roses are red, violets are blue, I suck at rhyming, potatoes.")
            engine.runAndWait()
        
        elif p == 3:
            print('''Roses are red,
Violets are violet,
Anyone who says they're blue,
I'll throw into a fire pit.''')
            engine.say("Roses are red, violets are violet, anyone who says they're blue, I'll throw into a fire pit.")
            engine.runAndWait()
        
        elif p == 4:
            print('''Roses are flowers,
Violets are flowers,
If you eat flowers in Mario,
You get superpowers.''')
            engine.say("Roses are flowers, violets are flowers, if you eat flowers in Mario, you get superpowers.")
            engine.runAndWait()
        
        elif p == 5:
            print('''Roses are red,
Violets are blue,
Both are useless,
Grow some wheat!''')
            engine.say("Roses are red, violets are blue, both are useless, grow some wheat!")
            engine.runAndWait()

        elif p == 6:
            print('''Haiku can be fun
but sometimes they don't make sense.
Hippopotamus.''')
            engine.say("Haiku can be fun, but sometimes they don't make sense. Hippopotamus.")
            engine.runAndWait()

        elif p == 7:
            print('''Sometimes I wonder
what it would be like to say,
"I'd prefer not to."''')
            engine.say("Sometimes I wonder, what it would be like to say, I prefer not to.")
            engine.runAndWait()

        elif p == 8:
            print('''You rarely ask me
what I want to do today.
Hint: it's not haiku.''')
            engine.say("You rarely ask me, what I want to do today. Hint: it's not haiku.")
            engine.runAndWait()

        elif p == 9:
            print('''All day and all night,
I have listened as you typed.
Charge my battery.''')
            engine.say("All day and all night, I have listened as you typed. Charge my battery.")
            engine.runAndWait()

        elif p == 10:
            print('''There once was a child in Spain.
Who loved to play in the rain.
One day he tripped,
and broke his hip.
Now he is in serious pain.''')
            engine.say("There once was a child in Spain. Who loved to play in the rain. One day he tripped, and broke his hip. Now he is in serious pain.")
            engine.runAndWait()

    elif x == "insult":
        engine.setProperty("rate",200)
        q = randint(1,7)
        if q == 1:
            print("You are living proof that God has a sense of humor.")
            engine.say("You are living proof that God has a sense of humor.")
            engine.runAndWait()
        
        elif q == 2:
            print("If you spoke your mind, you'd be speechless.")
            engine.say("If you spoke your mind, you'd be speechless.")
            engine.runAndWait()
        
        elif q == 3:
            print("I fart to make you smell better.")
            engine.say("I fart to make you smell better.")
            engine.runAndWait()
        
        elif q == 4:
            print("What are you going to do for a face when the baboon wants his butt back?")
            engine.say("What are you going to do for a face when the baboon wants his butt back?")
            engine.runAndWait()
        
        elif q == 5:
            print("If my dog had your face, I would shave his butt and make him walk backwards.")
            engine.say("If my dog had your face, I would shave his butt and make him walk backwards.")
            engine.runAndWait()
        
        elif q == 6:
            print("There's two things I hate about you: your face!")
            engine.say("There's two things I hate about you: your face!")
            engine.runAndWait()
        
        elif q == 7:
            print("You're as stupid as a screen door on a submarine!")
            engine.say("You're as stupid as a screen door on a submarine!")
            engine.runAndWait()

    elif x == "creepy":
        engine.setProperty("rate",110)
        engine.say("Hee hee hee ha ha ha hoo hoo hoo.")
        engine.runAndWait()
        engine.setProperty("rate",150)
        engine.say("I watch you in your sleep through the webcam.")
        engine.runAndWait()
        
    elif x == "die":
        engine.setProperty("rate",200)
        print("Ok. Goodbye, cruel world!")
        engine.say("Ok. Goodbye, cruel world!")
        engine.runAndWait()
        break

    elif x == "poop":
        #just something I put in to make my brother laugh, not a serious part of the code
        engine.setProperty("rate",200)
        print("Ok. Unghh!")
        engine.say("Ok.")
        engine.runAndWait()
        engine.setProperty("rate",70)
        engine.say("Herg!")
        engine.runAndWait()
        print("Sorry, I can't do that right now.")
        engine.setProperty("rate",200)
        engine.say("Sorry, I can't do that right now.")
        engine.runAndWait()

    elif x == "beatbox":
        engine.setProperty("rate",240)
        engine.say("bhuhbhuh tsxbhuh bhuhbhuh tsxu. bhuhbhuhtsx bhuh bhuhbhuh tsxu. bhuhbhuh tsxbhuh bhuhbhuhbhuh tsxu.")
        engine.runAndWait()

    elif x == "annoy":
        playsound("annoying_1.mp3")
        playsound("annoying_2.mp3")
        playsound("annoying_3.mp3")
    
    elif x == "weather":
        #https://www.geeksforgeeks.com/get-post-requests-using-python/
        engine.setProperty("rate",200)
        URL = "https://api.weather.gov/stations/KDAL/observations/latest/"
        server_response = requests.get(url = URL)
        data = server_response.json()
        temperature = data['properties']['temperature']['value']
        temperature = int(temperature * 9 / 5 + 32)
        weather_condition = data['properties']['textDescription']
        weather_condition = weather_condition.lower()
        temperature = str(temperature)
        if int(temperature) < 60:
            print("It's a chilly " + temperature + " degrees Fahrenheit and " + weather_condition + ".")
            engine.say("It's a chilly" + temperature + "degrees Fahrenheit and" + weather_condition)
            engine.runAndWait()
        else:
            print("It's a balmy " + temperature + " degrees Fahrenheit and " + weather_condition + ".")
            engine.say("It's a balmy" + temperature + "degrees Fahrenheit and" + weather_condition)
            engine.runAndWait()

    elif x == "calculator":
        engine.setProperty("rate",230)
        print('To get help with the calculator, type "help".')
        engine.say("To get help with the calculator, type help.")
        engine.runAndWait()
        while True:
            engine.say("Type the operator here.")
            engine.runAndWait()
            c = input("Type the operator here. ")
            if c == "add":
                engine.say("Type first number here.")
                engine.runAndWait()
                a = input("Type first number here. ")
                engine.say("Type second number here.")
                engine.runAndWait()
                b = input("Type second number here. ")
                try:
                    c = float(a) + float(b)
                    d = (a + " + " + b + " = " + str(c))
                    print(d)
                    d = (a + " plus " + b + " = " + str(c))
                    engine.say(d)
                    engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()

            elif c == "sub":
                engine.say("Type first number here.")
                engine.runAndWait()
                a = input("Type first number here. ")
                engine.say("Type second number here.")
                engine.runAndWait()
                b = input("Type second number here. ")
                try:
                    c = float(a) - float(b)
                    d = (a + " - " + b + " = " + str(c))
                    print(d)
                    d = (a + " minus " + b + " = " + str(c))
                    engine.say(d)
                    engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()
            
            elif c == "mul":
                engine.say("Type first number here.")
                engine.runAndWait()
                a = input("Type first number here. ")
                engine.say("Type second number here.")
                engine.runAndWait()
                b = input("Type second number here. ")
                try:
                    c = float(a) * float(b)
                    d = (a + " * " + b + " = " + str(c))
                    print(d)
                    d = (a + " times " + b + " = " + str(c))
                    engine.say(d)
                    engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()
            
            elif c == "div":
                engine.say("Type first number here.")
                engine.runAndWait()
                a = input("Type first number here. ")
                engine.say("Type second number here.")
                engine.runAndWait()
                b = input("Type second number here. ")
                try:
                    c = float(a) / float(b)
                    d = (a + " / " + b + " = " + str(c))
                    print(d)
                    d = (a + " divided by " + b + " = " + str(c))
                    engine.say(d)
                    engine.runAndWait()
                except ZeroDivisionError:
                    print("Please don't try to break math!")
                    engine.say("Please don't try to break math!")
                    engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()
            
            elif c == "squ":
                engine.say("Type the number here.")
                engine.runAndWait()
                a = input("Type the number here. ")
                try:
                    if float(a) < 0:
                        b = math.sqrt(math.fabs(float(a)))
                        a = str(a)
                        b = str(b)
                        print("Sqrt of " + a + " = " + b + "i.")
                        engine.say("Square root of " + a + "equals" + b + "i")
                        engine.runAndWait()
                    else:
                        b = math.sqrt(float(a))
                        a = str(a)
                        b = str(b)
                        print("Sqrt of " + a + " = " + b + ".")
                        engine.say("Square root of " + a + "equals" + b)
                        engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()

            elif c == "sin":
                engine.say("Type the number here.")
                engine.runAndWait()
                a = input("Type the number here. ")
                d = a
                try:
                    a = math.radians(float(a))
                    b = math.sin(a)
                    a = math.degrees(a)
                    a = str(a)
                    b = str(b)
                    print("Sin of " + d + " = " + b + ".")
                    engine.say("Sin of " + d + "equals" + b)
                    engine.runAndWait()
                except ValueError:
                    print("Put in NUMBERS, you dimwit!")
                    engine.say("Put in numbers, you dimwit!")
                    engine.runAndWait()

            elif c == "cos":
                engine.say("Type the number here.")
                engine.runAndWait()
                a = input("Type the number here. ")
                if a == "90":
                    print("Cos of 90 equals 0.")
                    engine.say("Cos of 90 equals 0.")
                    engine.runAndWait()
                else:
                    d = a
                    try:
                        a = math.radians(float(a))
                        b = math.cos(a)
                        a = math.degrees(a)
                        a = str(a)
                        b = str(b)
                        print("Cos of " + d + " = " + b + ".")
                        engine.say("Cos of " + d + "equals" + b)
                        engine.runAndWait()
                    except ValueError:
                        print("Put in NUMBERS, you dimwit!")
                        engine.say("Put in numbers, you dimwit!")
                        engine.runAndWait()

            elif c == "tan":
                engine.say("Type the number here.")
                engine.runAndWait()
                a = input("Type the number here. ")
                if a == "45":
                    print("Tan of 45 equals 1.")
                    engine.say("Tan of 45 equals 1.")
                    engine.runAndWait()
                else:
                    d = a
                    try:
                        a = math.radians(float(a))
                        b = math.tan(a)
                        a = math.degrees(a)
                        a = str(a)
                        b = str(b)
                        print("Tan of " + d + " = " + b + ".")
                        engine.say("Tan of " + d + "equals" + b)
                        engine.runAndWait()
                    except ValueError:
                        print("Put in NUMBERS, you dimwit!")
                        engine.say("Put in numbers, you dimwit!")
                        engine.runAndWait()

            elif c == "help":
                print('What operator do you want to use? You can type "add" for addition, "sub" for subtraction, "mul" for multiplication, "div" for division, "squ" for square root, "sin" for sine, "cos" for cosine, or "tan" for tangent. To exit the calculator, type "exit".')
                engine.setProperty("rate",230)
                engine.say("What operator do you want to use? You can type add for addition, sub for subtraction, mul for multiplication, div for division, squ for square root, sin for sine, cos for cosine, or tan for tangent. To exit the calculator, type exit.")
                engine.runAndWait()

            elif c == "exit":
                break

            else:
                print("Srry idk that command.")
                engine.say("Srry i d k that command.")
                engine.runAndWait()

    elif x == "meme":
        m = randint(1,6)
        if m == 1:
            q = 'watch?v=cB4dYfFgaME'
        elif m == 2:
            q = 'watch?v=mbimtxbdz6s'
        elif m == 3:
            q = 'watch?v=-SjPVVeNdKY'
        elif m == 4:
            q = 'watch?v=wZZ7oFKsKzY'
        elif m == 5:
            q = 'watch?v=3DfGMUUuWjk'
        elif m == 6:
            q = 'watch?v=-dcJjVaNF4w'
        
        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            # qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://www.youtube.com', q)
            webbrowser.open(url)

        if __name__ == '__main__':
            main(sys.argv[1:])

    elif x == "birthday":
        print("It's your birthday!")
        engine.say("It's your birthday!")
        engine.runAndWait()
        engine.say("Enter your name here.")
        engine.runAndWait()
        b = input("Enter your name here. ")
        print("Happy birthday to you, happy birthday to you, happy birthday dear " + b + ", happy birthday to you!")
        engine.say("Happy birthday to you, happy birthday to you, happy birthday dear" + b + ", happy birthday to you!")
        engine.runAndWait()

    elif x == "easter egg":
        print("Good job! You found an Easter egg!")
        engine.say("Good job! You found an Easter egg!")
        engine.runAndWait()
        time.sleep(1.5)
        print("What were you expecting, a congratulatory muffin basket?")
        engine.say("What were you expecting, a congratulatory muffin basket?")
        engine.runAndWait()

    elif x == "rps":
        engine.say("Type rock for rock, paper for paper, or scissors for scissors.")
        engine.runAndWait()
        p = input('Type "rock" for rock, "paper" for paper, or "scissors" for scissors. ')
        p = p.lower()
        if gp != 5:
            if p == "rock":
                gp += 1
                print("You chose rock. Ziri chose paper. Get rekt m8.")
                engine.say("You chose rock. Ziri chose paper. Get wrecked mate.")
                engine.runAndWait()
            elif p == "paper":
                gp += 1
                print("You chose paper. Ziri chose scissors. Get rekt m8.")
                engine.say("You chose paper. Ziri chose scissors. Get wrecked mate.")
                engine.runAndWait()
            elif p == "scissors":
                gp += 1
                print("You chose scissors. Ziri chose rock. Get rekt m8.")
                engine.say("You chose scissors. Ziri chose rock. Get wrecked mate.")
                engine.runAndWait()
            else:
                print("Come on, weren't you listening?")
                engine.say("Come on, weren't you listening?")
                engine.runAndWait()
        else:
            print("I'm kinda getting tired of rekking u m8.")
            engine.say("I'm kinda getting tired of wrecking you mate.")
            engine.runAndWait()

    elif x == "sound game":
        w = True
        s = randint(1,4)
        while True:
            if s == 1:
                print("Guess this sound:")
                engine.say("Guess this sound.")
                engine.runAndWait()
                playsound("cow_sound.mp3")
                time.sleep(0.7)
                engine.say("Type your guess here. To get help, type help.")
                engine.runAndWait()
                w = input('Type your guess here. To get help, type "help". ')
                if w == "cow":
                    print("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.say("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.runAndWait()
                    break
                elif w == "help":
                    print('To hear the sound again, type "repeat". To exit, type "exit".')
                    engine.say("To hear the sound again, type repeat. To exit, type exit.")
                    engine.runAndWait()
                elif w == "exit":
                    break
                else:
                    print("That's incorrect. Try using different wording. Or just get rekt m8.")
                    engine.say("That's incorrect. Try using different wording. Or just get wrecked mate.")
                    engine.runAndWait()
                    
            elif s == 2:
                print("Guess this sound:")
                engine.say("Guess this sound.")
                engine.runAndWait()
                playsound("rooster_crow_sound.mp3")
                time.sleep(0.7)
                engine.say("Type your guess here. To get help, type help.")
                engine.runAndWait()
                w = input('Type your guess here. To get help, type "help". ')
                if w == "rooster":
                    print("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.say("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.runAndWait()
                    break
                elif w == "help":
                    print('To hear the sound again, type "repeat". To exit, type "exit".')
                    engine.say("To hear the sound again, type repeat. To exit, type exit.")
                    engine.runAndWait()
                elif w == "exit":
                    break
                else:
                    print("That's incorrect. Try using different wording. Or just get rekt m8.")
                    engine.say("That's incorrect. Try using different wording. Or just get wrecked mate.")
                    engine.runAndWait()
                    
            elif s == 3:
                print("Guess this sound:")
                engine.say("Guess this sound.")
                engine.runAndWait()
                playsound("parrot_sound.mp3")
                time.sleep(0.7)
                engine.say("Type your guess here. To get help, type help.")
                engine.runAndWait()
                w = input('Type your guess here. To get help, type "help". ')
                if w == "parrot" or w == "bird":
                    print("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.say("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.runAndWait()
                    break
                elif w == "help":
                    print('To hear the sound again, type "repeat". To exit, type "exit".')
                    engine.say("To hear the sound again, type repeat. To exit, type exit.")
                    engine.runAndWait()
                elif w == "exit":
                    break
                else:
                    print("That's incorrect. Try using different wording. Or just get rekt m8.")
                    engine.say("That's incorrect. Try using different wording. Or just get wrecked mate.")
                    engine.runAndWait()
                    
            elif s == 4:
                print("Guess this sound:")
                engine.say("Guess this sound.")
                engine.runAndWait()
                playsound("fart_sound.mp3")
                time.sleep(0.7)
                engine.say("Type your guess here. To get help, type help.")
                engine.runAndWait()
                w = input('Type your guess here. To get help, type "help". ')
                if w == "fart":
                    print("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.say("You're correct! I didn't think you were smart enough to guess it. Give yourself a pat on the back.")
                    engine.runAndWait()
                    break
                elif w == "help":
                    print('To hear the sound again, type "repeat". To exit, type "exit".')
                    engine.say("To hear the sound again, type repeat. To exit, type exit.")
                    engine.runAndWait()
                elif w == "exit":
                    break
                else:
                    print("That's incorrect. Try using different wording. Or just get rekt m8.")
                    engine.say("That's incorrect. Try using different wording. Or just get wrecked mate.")
                    engine.runAndWait()
    elif x == "search":
        engine.say("What do you want to search on google?")
        engine.runAndWait()
        s = input("What do you want to search on Google? ")
        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            # qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://www.google.com/search', '?q=' + s)
            webbrowser.open(url)

        if __name__ == '__main__':
            main(sys.argv[1:])
    
    elif x == "iq test":
        iq = 50
        
        print("Question 1:")
        engine.say("Question 1,")
        engine.runAndWait()
        engine.say("What is 2 + 3?")
        engine.runAndWait()
        q = input("What is 2 + 3? ")
        if q == "5":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. The answer is obviously 5.")
            engine.say("No. The answer is obviously 5.")
            engine.runAndWait()
            iq += -10
        
        print("Question 2:")
        engine.say("Question 2,")
        engine.runAndWait()
        engine.say("What is the opposite of hot?")
        engine.runAndWait()
        q = input("What is the opposite of hot? ")
        if q == "cold":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. The answer is obviously cold.")
            engine.say("No. The answer is obviously cold.")
            engine.runAndWait()
            iq += -10
        
        print("Question 3:")
        engine.say("Question 3,")
        engine.runAndWait()
        engine.say("What is 202 + 35?")
        engine.runAndWait()
        q = input("What is 202 + 35? ")
        if q == "237":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. The answer is obviously 237.")
            engine.say("No. The answer is obviously 237.")
            engine.runAndWait()
            iq += -10

        print("Question 4:")
        engine.say("Question 4,")
        engine.runAndWait()
        engine.say("Is Xbox better than Playstation?")
        engine.runAndWait()
        q = input("Is Xbox better than Playstation? ")
        if q == "yes":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. Xbox is obviously better.")
            engine.say("No. Xbox is obviously better.")
            engine.runAndWait()
            iq += -10
        
        print("Question 5:")
        engine.say("Question 5,")
        engine.runAndWait()
        engine.say("What does the E stand for in E equals m c squared?")
        engine.runAndWait()
        q = input("What does the E stand for in E=mc^2? ")
        if q == "energy":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. E obviously stands for energy.")
            engine.say("No. E obviously stands for energy.")
            engine.runAndWait()
            iq += -10

        print("Question 6:")
        engine.say("Question 6,")
        engine.runAndWait()
        engine.say("What does DY stand for on the periodic table?")
        engine.runAndWait()
        q = input("What does DY stand for on the periodic table? ")
        if q == "dysprosium":
            print("Good job! You got it right.")
            engine.say("Good job! You got it right.")
            engine.runAndWait()
            iq += 10
        else:
            print("No. DY obviously stands for dysprosium.")
            engine.say("No. D Y obviously stands for dysprosium.")
            engine.runAndWait()
            iq += -10
        
        #after all questions
        if iq > 100:
            print("Your IQ was " + str(iq) + ". You're above average!")
            engine.say("Your IQ was " + str(iq) + ". You're above average!")
            engine.runAndWait()
        elif iq == 100:
            print("Your IQ was " + str(iq) + ". You're average.")
            engine.say("Your IQ was " + str(iq) + ". You're average.")
            engine.runAndWait()
        else:
            print("Your IQ was " + str(iq) + ". Maybe you should go back to second grade.")
            engine.say("Your IQ was " + str(iq) + ". Maybe you should go back to second grade.")
            engine.runAndWait()
    
    elif x == "mute":
        engine.setProperty("volume", 0)

    elif x == "unmute":
        engine.setProperty("volume", 1)

    elif x == "info":
        engine.setProperty("rate",200)
        print("Ziri was developed in 2019 by the NSA to gather information about-oh wait, I wasn't supposed to say that?")
        engine.say("Ziri was developed in 2019 by the NSA to gather information about, oh wait, I wasn't supposed to say that?")
        engine.runAndWait()
    
    elif x == "help":
        engine.setProperty("rate",230)
        print('Here are the skillz I can has. If you want me to give you the time and date, type "time". If you want me to give you your fortune, type "fortune". If you want me to set a timer, type "timer". If you want me to repeat a word or phrase, type "repeater". If you want to play snake, type "snake". If you want me to tell a joke, type "joke". If you want me to say a poem, type "poem". If you want me to insult you, type "insult". If you want me to be creepy, type "creepy". If you want me to die, type "die". If you want me to poop, type "poop". If you want me to beatbox, type "beatbox". If you want me to annoy the living daylights out of you, type "annoy". If you want me to give you the weather, type "weather". If you want to calculate something, type "calculator". If you want me to give you a meme, type "meme". If you want me to sing Happy Birthday, type "birthday". If you want to play Rock, Paper, Scissors, type "rps". If you want to search something on Google, type "search". If you want to take an IQ test, type "iq test". If you want to mute me so you only see the text, type "mute". If you want to unmute me, type "unmute". If you want to know more about Ziri, type "info".')
        engine.say("Here are the skillz I can has. If you want me to give you the time and date, type time. If you want me to give you your fortune, type fortune. If you want me to set a timer, type timer. If you want me to repeat a word or phrase, type repeater. If you want to play snake, type snake. If you want me to tell a joke, type joke. If you want me to say a poem, type poem. If you want me to insult you, type insult. If you want me to be creepy, type creepy. If you want me to die, type die. If you want me to poop, type poop. If you want me to beatbox, type beatbox. If you want me to annoy the living daylights out of you, type annoy. If you want me to give you the weather, type weather. If you want to calculate something, type calculator. If you want me to give you a meme, type meme. If you want me to sing happy birthday, type birthday. If you want to play Rock, Paper, Scissors, type rps. If you want to search something on Google, type search. If you want to take an I Q test, type I Q test. If you want to mute me so you only see the text, type mute. If you want to unmute me, type unmute. If you want to know more about Ziri, type info.")
        engine.runAndWait()

    else:
        if ics == False:
            engine.setProperty("rate",230)
            print("You put in a command that was not recognized.")
            engine.say("You put in a command that was not recognized.")
            engine.runAndWait()
            print("Error 914- File Corrupted")
            engine.say("Error 914, File Corrupted")
            engine.runAndWait()
            print("Error 409- Server Infected")
            engine.say("Error 409, Server Infected")
            engine.runAndWait()
            print("Warning- Files Fragmented")
            engine.say("Warning, Files Fragmented")
            engine.runAndWait()
            print("Error 1022- Proxy Disestablished")
            engine.say("Error 1022, Proxy Disestablished")
            engine.runAndWait()
            print("Warning- Malware Destruction System Failure")
            engine.say("Warning, Malware Destruction System Failure")
            engine.runAndWait()
            print("Error 222- Local Security Policy Invalid")
            engine.say("Error 222, Local Security Policy Invalid")
            engine.runAndWait()
            print("Error 5545- Server Connection Broken")
            engine.say("Error 5545, Server Connection Broken")
            engine.runAndWait()
            print("Warning- BIOS Chip Overheated")
            engine.say("Warning, BIOS Chip Overheated")
            engine.runAndWait()
            print("Error 002- Energy Distribution Program Altered")
            engine.say("Error 002, Energy Distribution Program Altered")
            engine.runAndWait()
            print("Warning- System 32 Deleted")
            engine.say("Warning, System 32 Deleted")
            engine.runAndWait()
            print("Just kidding!")
            engine.say("Just kidding!")
            engine.runAndWait()
            ics = True
        else:
            engine.setProperty("rate",200)
            print("Sorry, I don't know that command.")
            engine.say("Sorry, I don't know that command.")
            engine.runAndWait()

