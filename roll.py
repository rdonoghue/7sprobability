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
#            print "%r, %r" % (rollset[x], rollset[y]),
            if x != y:
                if rollset[x] + rollset[y] == 10:
                    raises += 1
                    rollset[y]=0
                    rollset[x]=0
    return raises, rollset
# Note to self - when it comes time to tighten the stack, check if 0 + 1 < 10

def trios(rollset, raises):
    setsize=len(rollset)
    for x in range (0, setsize):
        for y in range (0,setsize):
            for z in range (0,setsize):
                if (x!= y and x!= z and y!=z):
                    if rollset[x] + rollset[y] + rollset[z] == 10:
                        raises += 1
                        rollset[y]=0
                        rollset[x]=0
                        rollset[z]=0
    return raises, rollset


def cleanzeroes(rollset):
    # This is probably uncessary, but leaving the step in for now to be clean
    while 0 in rollset:
        for x in range (0, len(rollset)):
            if rollset[x] == 0:
                rollset.pop(x)
                break
    return rollset




dicerolled = 10
skillpool = 2
raises = 0


diceroll = sevenroll(dicerolled)
print "Initial: %r" % (diceroll)

result1, diceleft =tens(diceroll)
print "Tens: %r: %r" % (result1, diceleft)

result2, diceleft = pairs(diceleft, result1)
print "Pairs: %r: %r" % (result2, diceleft)

diceleft = cleanzeroes(diceleft)
print "Cleaned: %r: %r" % (result2, diceleft)

result3, diceleft = trios(diceleft, result2)
print "Trios: %r: %r" % (result3, diceleft)

diceleft = cleanzeroes(diceleft)
print "Cleaned: %r: %r" % (result3, diceleft)




# raisescount[raises] += 1

# for x in range (0, dicerolled):
#    print "%i: %i" % (x, raisescount[x])
