from examples import is_palindrome


def sum_ints(lst):
    '''
    INPUT: list
    OUTPUT: int

    The input list contains a mixture of integers, floats and strings. Sum up
    only the ints.
    Hint: Use the isinstance function.
    '''

    return sum(elem for elem in [item for item in lst if isinstance(item, int)])


def min_and_max(lst):
    '''
    INPUT: list
    OUTPUT: tuple of two ints/floats

    Given a list of ints and/or floats, return a 2-tuple containing the values
    of the items with the smallest and largest absolute values.

    In the case of an empty list, return None.
    '''
    result = None
    if len(lst) != 0:
        abslist = map(lambda x: abs(x), lst)
        maxvalue = max(abslist)
        maxindex = abslist.index(maxvalue)
        minvalue = min(abslist)
        minindex = abslist.index(minvalue)
        # return abslist
        result = (lst[minindex], lst[maxindex])
    # return maxvalue, maxindex, minvalue, minindex
    return result

def are_palindromes(words):
    '''
    INPUT: list
    OUTPUT: bool

    Given a list of strings, return whether ALL of the elements are
    palindromes.

    Hint: use the is_palindrome function that has been imported at
    the top of this file
    '''
    result = True
    for word in words:
        if word[::-1] != word:
            result = False
    return result


def substring(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    result = []
    for word in words:
        for substring in substrings:
            if word.find(substring) != -1:
                result.append(substring)
    return result
