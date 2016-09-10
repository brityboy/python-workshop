from string import punctuation


def invalid_words(wordlist, document_filename):
    '''
    INPUT: list, str
    OUTPUT: int

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    '''
    wordlist = set(wordlist)
    with open(document_filename) as doc:
        result = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                if word.lower().strip(punctuation) not in wordlist:
                    result.append(word)
        return result


def common_characters(s, num):
    '''
    INPUT: str, int
    OUTPUT: list of chars

    Return the list of characters which appear in the string s more than num
    times.
    '''
    from collections import defaultdict, Counter
    dict_string = Counter(sorted(s))
    return [string for string in dict_string if dict_string[string]>num]
    #result = []
    #for char in set(s):
    #for char in s:
    #    if s.count(char) > num:
    #        if char not in result:
    #            result.append(char)
    #return result

def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''
    # remove duplicates
    # for i, item1 in enumerate(lst):
    #     for item2 in lst[i + 1:]:
    #         if item1 + item2 == 0:
    #             return item1, item2
    set_lst = set(lst)
    for item in set_lst:
       if -1*item in set_lst:
           return item, -1*item
