import random as rd
import pyttsx3 as pt3
engine1 = pt3.init()
engine1.setProperty('rate', 150)
engine1.setProperty('volume', 0.9)
while True:
    q = input()
    ans = ['yes', 'no', 'hohoho', 'augh']
    rans = rd.choice(ans)
    print(rans)
    engine1.say(q)
    engine1.say(rans)
    engine1.runAndWait()