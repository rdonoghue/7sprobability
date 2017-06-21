from __future__ import division
import random

def listtochart(mylist):
    mylist = sorted(mylist)
#    print "list: %r" % mylist
    total = len(mylist)
#    print "total: %r" % total
    first = mylist[0]
#    print "first: %r" % first
    last = mylist[total -1]
#    print "last: %r" % last
    for x in range (first,last + 1):
        percent = ((mylist.count(x) * 100 /  total))
        print "%r,%r" % (x, percent)


def listtocsv(index,mylist):
    mylist = sorted(mylist)
#    print "list: %r" % mylist
    total = len(mylist)
#    print "total: %r" % total
    first = mylist[0]
#    print "first: %r" % first
    last = mylist[total -1]
#    print "last: %r" % last
    for x in range (first,last + 1):
        percent = ((mylist.count(x) * 100 /  total))
        print "%r,%r,%r" % (index, x, percent)
# Ok, if I want to do something fancy witht his, then I may need to make
# list of lists, which I think is a thing



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


def countraises(diceroll, raises, target, skillpool):
    while sum(diceroll) >= target:
        raises, diceroll =raisetens(diceroll, raises, target)
        print "Tens: %r: %r" % (raises, diceroll)
        raises, diceroll = raisepairs(diceroll, raises, target)
        print "Pairs: %r: %r" % (raises, diceroll)
        raises, diceroll = raisetrios(diceroll, raises, target)
        print "Trios: %r: %r" % (raises, diceroll)
        dicetally = len(diceroll)
        if (dicetally > 1 and sum(diceroll) >= target):
            diceroll[0]= diceroll[0] + diceroll[dicetally -1]
            diceroll.pop(dicetally - 1)
            print "update: %r:%r" % (raises, diceroll)
    print
    return raises, diceroll



def raisetens(rollset, raises, target):
    for x in range (0, len(rollset)):
        if rollset[x] >= target:
            rollset[x] = 0
            raises +=1
    rollset = cleanzeroes(rollset)
    return raises, rollset

def raisepairs(rollset, raises,target):
    setsize=len(rollset)
    for x in range (0, setsize):
        for y in range (0,setsize):
#            print "%r, %r" % (rollset[x], rollset[y]),
            if x != y:
                if rollset[x] + rollset[y] == target:
                    raises += 1
                    rollset[y]=0
                    rollset[x]=0
    rollset = cleanzeroes(rollset)
    return raises, rollset
# Note to self - when it comes time to tighten the stack, check if 0 + 1 < 10

def raisetrios(rollset, raises, target):
    setsize=len(rollset)
    for x in range (0, setsize):
        for y in range (0,setsize):
            for z in range (0,setsize):
                if (x!= y and x!= z and y!=z):
                    if rollset[x] + rollset[y] + rollset[z] == target:
                        raises += 1
                        rollset[y]=0
                        rollset[x]=0
                        rollset[z]=0
    rollset = cleanzeroes(rollset)
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
skillpool = 4
raises = 0
target = 15

# This is the results inspector
# (With print steps uncommented in the functions)
diceroll = sevenroll(dicerolled,skillpool)
print "%r: (%r)" % (diceroll, len(diceroll))
raises, diceroll = countraises(diceroll, raises, target, skillpool)








'''
# This is the result generator

testrolls= 1000
for y in range (10,11):

    skill10result = []
    for x in range (0,testrolls):
        dicerolled = y
        skillpool = 2
        raises = 0
        target = 10
        diceroll = sevenroll(dicerolled,skillpool)
        raises, diceroll = countraises(diceroll, raises, target, skillpool)
#        print "%r. %r (%r)" % (x, raises, len(diceroll))
        skill10result.append(raises)
#    print "%r rolls, %r dice rolled" % (testrolls, dicerolled)
#    print "----------------"
    listtocsv(y,skill10result)
    print
'''
