from collections import defaultdict, Counter

def dict_fun(d):
    '''
    Returns all keys in a list from a dict
    '''
    #return d.keys()
    #for k,v in d.iteritems():
    #    print k, v
    for i,j in d.items():
        print i,j
my_dict = {'steak':10, 'banana': 1, 'ice cream':5}

my_list = ['a', 'b', 'c', 'a', 'b', 'd', 'c']

def get_idxs(l):
    '''
    return a dictionary of items in the list
    as keys and values as a list of indices where
    those items occurred.
    '''
    result = {}
    #for i, elem in enumerate(l):
    #    if elem not in result:
    #        result[elem] = [i]
    #    else:
    #        result[elem].append(i)
    #for i, elem in enumerate(l):
    #    result[elem]=result.get(elem, [])+[i]
    d = defaultdict(list)
    for i, elem in enumerate(l):
        d[elem].append(i)
    return d

idx_dict=get_idxs(my_list)

def count_items(l):
    '''
    Returns dict with keys as items in l, and values
    as number of times they occured in l
    '''
    #key = set(l)
    #d = defaultdict(int)
    #for item in key:
    #    d[item] = l.count(item)
    #return d
    return Counter(l)


count_dict = count_items(my_list)
