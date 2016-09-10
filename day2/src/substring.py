from collections import defaultdict


def substring_old(words, substrings):
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


def substring_new(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    # in the old method, i was going through the substring list 5 times

    dict = defaultdict(str)
    for word in words:
        for substring in substrings:
            if word.find(substring) != -1:
                dict[word]=substring
    return dict.values()
