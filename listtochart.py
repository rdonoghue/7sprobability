# Given a list full of numbers, generate a chart of their distrbution.
from __future__ import division

def listtochart(mylist):
    mylist = sorted(mylist)
    print "list: %r" % mylist
    total = len(mylist)
    print "total: %r" % total
    first = mylist[0]
    print "first: %r" % first
    last = mylist[total -1]
    print "last: %r" % last
    for x in range (first,last + 1):
        percent = ((mylist.count(x) * 100 /  total))
        print "%r: %r (%r percent)" % (x, mylist.count(x), percent)


samplelist = [4, 6, 4, 5, 5, 4, 5, 9, 5, 4]

listtochart(samplelist)
