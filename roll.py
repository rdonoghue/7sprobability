import random


def sevenroll(poolsize):
    localresult = []
    for x in range(0, poolsize):
        dieroll = random.randint(1, 10)
        localresult.append(dieroll)
    localresult = sorted(localresult, reverse=True)
    return localresult

def tens(rollset):
    raises = rollset.count(10)
#    print "Initial roll: %r" % (rollset)
#    print "%r Raises" % (raises)
    for x in range (0, raises):
        rollset.pop(0)
    return raises, rollset

def pairs(rollset, raises):
    setsize=len(rollset)
    for x in range (0, setsize):
        for y in range (0,setsize):
            print "%r, %r" % (rollset[x], rollset[y]),
            if x < y:
                if rollset[x] + rollset[y] == 10:
                    raises += 1
                    rollset.pop(y)
                    rollset.pop(x)
                    setsize = setsize - 2
            elif x > y:
                if rollset[x] + rollset[y] == 10:
                    raises += 1
                    rollset.pop(x)
                    rollset.pop(y)
                    setsize = setsize - 2
#    return raises, rollset
# Note to self - when it comes time to tighten the stack, check if 0 + 1 < 10


dicerolled = 10
skillpool = 2
raises = 0


diceroll = sevenroll(dicerolled)
print "Initial: %r" % (diceroll)
result1, diceleft =tens(diceroll)

print "Tens: %r: %r" %(result1, diceleft)
pairs(diceleft, result1)
print "Pairs: "





# raisescount[raises] += 1

# for x in range (0, dicerolled):
#    print "%i: %i" % (x, raisescount[x])
