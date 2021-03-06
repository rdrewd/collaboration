#! `env python` -t
def seq(n):
    """
    Generate the sequence for Project Euler problem 14.
    ===================================================

    n is a positive integer that is the first number in the sequence.

    I'm told that although it hasn't been proven, that it is believed that
    regardless of the starting number, the sequence eventually gets to 1,
    which is where we stop.
             1         2          3         4         5         6         7         8
    123456789012345678901234567989012345678901234567890123456789012345678901234567890
    """

    while True:
        if n % 2 == 0:
            next=n/2
        else:
            next=3*n+1
        yield n
        if n == 1:
            return
        n=next

# end seq

class Cache:
    """
    A Cache is a place where a value can be associated with an integer.
    When the Cache is created, an upper bound for the integer is set.
    When a value is stashed into the cache, if the associated integer is out of
    bounds, then the stash operation is a no-op.
    The value associated with an integer can be retrieved using the value(i) routine.
    If no value has ever been passed to stash for association with the given integer,
    then a value of 0 is returned.
    If the value of i is out of bounds, a value of 0 is returned.
    """
    def __init__(self, bound):
        self.c=[0 for i in xrange(bound)]
        self.bound=bound
    # end "Cache.__init__"

    def stash(self, i, val):
        if i >= self.bound:
            return
        self.c[i]=val
     # end Cache.stash

    def value(self,  i):
        if i >= self.bound:
            return 0
        return self.c[i]
    # end Cache.value

def runlen(n, c):
    """
    runlen returns the length of the sequence
    generated by seq(n)
    c is a Cache where we remember runlen's of n's we've already done.
    If we run into a remembered runlen, we don't have to generate the rest of the sequence,
    but can just add on how long we remember the sequence goes from here.
    """

    count=0
    for s in seq(n):
        lookupcount=c.value(s)
        if lookupcount != 0:
            count += lookupcount
            break
            # Need something to abort seq(n) since we are quitting the loop before running the
            # generator to exhaustion?? XXX
        count += 1
    # end "for s"
    c.stash(n, count)
    return count
# end runlen

def main():
    c=Cache(100000)
    # if we have lots of memory available, Cache(1000000) would be great for this problem,
    # but I'm thinking that a smaller Cache than that would still help the runtime.
    # For this run I'm trying 100,000 for the Cache size.
    longest=0
    basis=0
    for i in xrange(1, 1000000):
        r=runlen(i, c)
        if r > longest:
            basis=i
            longest=r
#        print 'runlen(', i, ',c)=', runlen(i,c)
        #   end "for i"
    print "longest=", longest,\
        "generated from", basis
# end main

if __name__ == '__main__':
    from time import time
    tstart=time()*1000
    main()
    tend=time()*1000
    print 'start time=%8.6f;' \
        'end time=%8.6f' % (tstart, tend)
    print 'runtime (elapsed milliseconds)=%8.6f' % \
        (tend-tstart)

# end __main__

