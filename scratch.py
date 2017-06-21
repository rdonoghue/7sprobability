import random



def roll(poolsize):
    localresult = []
    for x in range(0, poolsize):
        dieroll = random.randint(1, 10)
        localresult.append(dieroll)
#        print "Results: %i" % len(localresult)
#        print "Rolled a %i" % (dieroll)
    return localresult

result = 1,2,3,4,5,6,7,8,9,10

# print "Results: %i" % len(result)

# dieroll = random.randint(1, 10)
# print "Rolled a %i" % dieroll

# dicearray = []
dicearry=roll(7)

print "Results: %i" % len(dicearry)
print "---"
for outcome in dicearry:
    print "%i" % (outcome),
print "---"
cleanarry=sorted(dicearry)

for outcome in cleanarry:
    print "%i" % (outcome),
