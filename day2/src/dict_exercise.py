def dict_to_str(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is separated by a new
    line.

    For example:
    a: 1
    b: 2

    For nice pythonic code, use iteritems!

    Note: it's possible to do this in 1 line using list comprehensions and the
    join method.
    '''

    return '\n'.join([elem[0]+': '+str(elem[1]) for elem in [item for item in d.iteritems()]])

def dict_to_str_sorted(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is sorted in ascending order by key.
    This is sorted version of dict_to_str().

    Note: This one is also doable in one line!
    '''
    return '\n'.join([elem[0]+': '+str(elem[1]) for elem in sorted([item for item in d.iteritems()])])

def dict_difference(d1, d2):
    '''
    INPUT: dict, dict
    OUTPUT: dict

    Combine the two dictionaries, d1 and d2 as follows. The keys are the union of the keys
    from each dictionary. If the keys are in both dictionaries then the values should be the
    absolute value of the difference between the two values. If a value is only in one dictionary,
    the value should be the absolute value of that value.
    '''
    from collections import defaultdict
    allkeys = d1.keys()+d2.keys()
    result = defaultdict(int)
    for key in allkeys:
        if key in d1 and key in d2:
            result[key]=abs(d1[key]-d2[key])
        elif key in d1:
            result[key] = abs(d1[key])
        elif key in d2:
            result[key] = abs(d2[key])
    return dict(result)
