## EFFICIENCY
my_dict = {'steak':10, 'banana': 1, 'ice cream':5}

# dictionaries re mutable
# you can do a bunch of stuff with them and put

# thing to think about
# do I REALLY need to make a list of this?

# you can access values in dictionaries like this
#     for i,j in d.items():
#        print i,j
# this way, you are unpacking the tuple that d.items
# generates

# whenever you create a list, it is a sneaky
# and memory intensive way of doing something

# dictionaries are built on top of hashtables
# and you can

# your default go to should be
# mydict.iteritems
# mydict.itekeys
# mydict.itervalues

# this code works but this code sucks
#    for i, elem in enumerate(l):
#        if elem not in result:
#            result[elem] = [i]
#        else:
#            result[elem].append(i)
#    return result
# because it's not as easily readable so sad...

#this code is a LITTLE better
#    for i, elem in enumerate(l):
#        result[elem]=result.get(elem, [])+[i]

# but this code is best
#     d = defaultdict(list)
#    for i, elem in enumerate(l):
#        d[elem].append(i)
#    return d
# default dict is going to set a default key value
# so that you can do whatever it is you need to do
# to the key value - nice!
# you can treat a default dictionary like a normal dict
# you can turn a default dict into a dictionary and then
# just use dict(default_dict)

# instead of using a counter or an iterator
# just use counter
# from collections import Counter
# you can add count dict together

# lets revisit the notion that sets and dictionaries
# are VERY VERY fast

from math import sqrt

def all_divisors(num):
    '''
    INPUT: int
    OUTPUT: list of ints

    Given an integer, return a list of all the divisors of that number.
    '''
    result = []
    for i in xrange(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            result.append(num / i)
    return result


def get_divisors(numbers, divisors):
    '''
    INPUT: list of ints, list of ints
    OUTPUT: list of ints

    Return a list of the values from the second list that are proper divisors
    of elements in the first list.
    '''
    #s = set()
    d = Counter()
    for num in numbers:
        s.update(all_divisors(num))
    #return [divisor for divisor in divisors if divisor in s]
    return [divisor for divisor in divisors if d[divisor] >= 2]

# fuck that code didn't work tangina

# you will NEED python when you deploy code like on a server
# you will use ipython when you are interacting with it for
# python will be installed in EVERY unit distro
