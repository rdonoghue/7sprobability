import random

def sevenroll(poolsize,skillpool):
    myroll = []
    for x in range(0, poolsize):
        dieroll = random.randint(1, 10)
        #exploding 10's for 5 dots
        if skillpool >= 5:
            while dieroll == 10:
                myroll.append(dieroll)
                print "A 10 exploded!"
                dieroll = random.randint(1, 10)
        myroll.append(dieroll)
    myroll = sorted(myroll, reverse=True)
    return myroll


dicerolled = 10
skillpool = 5
diceroll = sevenroll(dicerolled,skillpool)

print "%r:%r" % (len(diceroll), diceroll)
