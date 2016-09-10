## FUNCTIONS

# good readable code - this is something that's going to be very important and this involves
# - writing functions
# - understanding python data structures
# - importing

# use vim
# the text editor should help us, it should't work against us - don't touch the mouse EVER (wtf?)

# functions
# - take something in, process it, push something out

def sum_absolute_values(L):
    '''
    INPUT: lst
    OUTPUT: int/float

    Given a list of ints/floats, return the sum of the
    absolute values of all the elements.
    '''

    tot = 0
    for elem in L:
        tot += abs(elem)
        #print elem

    #return tot
    #return sum(abs(elem) for elem in L)
    return sum(find_stat(df) for df in L)

def sum(L):
    '''
    sum the squares
    '''
    pass

# python is a duct type language
# if the code is easier to read, then that's better
# one of the things that is nice about list comprehension is that
# you can use functions that you've written to process the data
# for example
# return sum(find_stat(df) for df in L)

# with python code, make it read like english
# use functions, name them appropriately

# example
def find_stat(df):
    '''
    input: dataframe
    output: int-sum of column means
    '''
    return abs(df)

# underscore underscore name is something associated with every
# script so that python can associate everything that python
# is run in
if __name__ == '__main__':
    print sum_absolute_values([-5, -4, 6, 3])

# in short a main block is used so that you don't run script
# that you don't want to run



# don't do this --> from lecture import *
# but this is a bad practice
# uses a lot of memory
# this is oging to cause what's called namespace pollution
# it can happen that you import libraries where one function
# is similarly named as another functions
# example - sum is in both pandas and numpy - then tepok ka
# you want to make sure that you import only what you need so that
# you don't overwrite and confuse the namespace in python

## DATA STRUCTURES
# data structures are mutable, immutable, ordered, unordered
# mutable and ordered --> lists
# mutable and unordered --> dictionaries
# dictionaries have keys
# d.get(4, 'key not found')
# i want this number of items to be a key -
# this person's name, their birthday, their hometown
# as a list BUT this can't be because lists are mutable
# immutable ordered = tuples
# tuples are immutable and thus can be hashed
# immutable and unordered --> sets

# sets are like lists but not ordered, there's no index
# s.add(7) is how you add to sets
# sets keep things unique
# best to use sets to keep track of unique items
# elements in a set need to be hashable

# mutable means that you can modify them in place - this means that
# you don't need to do another assignment
# for a list to be ordered means that it follows an index

# mutability of strings
# if we do this
# s = 'hello'
# s = 'hi'
# if we do this, we just re-point s to another variable
# 'hello' still exists, but s just now points to 'hi'
# python is pass by object reference
# when we have somthing on the other side of the = operator,
# we are simply reassigning things

def ex_fun(l):
    l.append('baa')

# you'll have to hunt down bugs that fuck lists up because
# well, they're real bastards

## STRING FORMATTING
# NEVER USE this
#'''
#print_string = 'Hello %s, you are %d years old'
#print print_string % ('Brian', 30)
#'''

# this is what we are going to use
#'''
#print_string = 'Hello {name}, you are {age} years old\nGood to meet you, {name}'
#print print_string.format(name='Brian', age=30)
#'''

## FILE INPUT OUTPUT
# f.open(filename, 'r')
# f.readline()
# never do this

# should do
# with open(filename) as f:
#    lec = f.read()

# do this for EVERYTHING like sql databases, etc

# if it is something 30 gb large, for example, one can do
# f = open(filename, 'r'):
# for line in f:
#   print line

# from datetime import datetime
