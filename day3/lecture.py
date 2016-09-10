# # OBJECT ORIENTED PROGRAMMING
# python, at its core, is an object oriented programming language
# the world is organized as things
#
# example = table --> has ways of describing it like
# ATTRIBUTES
# a) number of legs
# b) square footage or area of the surface
# ACTIONS
# a) it can power things
# b) it can roll
#
# When we think about things it's about things that we have and
# things we can do
#
# example, lists you can
# a) append, concatenate etc  --> so many things we can do with it
#
# don't forget ID(object) to see what it is in memory
#
# today we are going to make a library class to check books in and out
#
# three things we can do with objects
# a) Encapsulation
#  - this is kind of like the extension of abstraction
#  - abstraction --> take a complex task and do it behind the scenes without
#  having to tell the user what it is
#  functions abstract away what is actually being done
#  - Encapsulation is like abstraction but at the next level
#  - an object has data, and functions
#  - encapsulation takes functions, ties it together with data, and takes
#  it as a single idea
#  - example: lists - by it being a list there are now so many ways that
#  we can interact with it. we have data and we have access to functionality
#  functions, when with objects, are called 'methods'
#  - the data and functions in objects, these have special names
#  - data OR attributes are referred to as ATTRIBUTES aka fields
#  - functionality is also known as methods - a procedure defined on my object
#
# b) Polymorphism
#  - say i have different classes but they do similar things
#  - if you have similar functions but they do similar things
#  - you can have objects and class interact with each other
#  - it's a generic way of interacting with a group of classes
# c) Inheritance
#  - we can share functionality down a hierarchy
#  - say we have a class of flat surfaces
#  - example we say Table(FlatSurface), then Table inherits all of the
#  - functionality of FlatSurface
#  - FAVOR COMPOSITION OVER Inheritance
#  - instead of inheriting stuff in a generic way - just design you classes
#  - such that the attributes are instances of other classes
#  - example
#  - class Legs(object):
#  -    def __init__(self):
#  -        self.is_broken
#  - what we are doing is making new classes by putting together other classes
#
#
# In python, we are going to make our own objects
# We want to be able to interact with these different things
# in these cases, what we want to do is to write our own new objects
# if in python, we define functions with def; and we define objects with class
#
# class Table(object): for example

class Table(object):
    def __init__(self, legs, area, stuff=None):
        self.legs = legs
        self.area = area
        self.stuff = stuff if stuff else []
    def add_legs(self, num):
        self.legs += num
    def clean(self):
        self.stuff = []
    def add_thing(self, thing):
        self.stuff.append(thing)

# turnerary code
# x = True
# a = 5 if x else 6

# then you can call this in python with, example
# my_table = Table(4, 12)
# if you do my_table.legs, it would output 4
# similarly, if you do my_table.legs = 12
# if you do other_table = Table(4, 18) then you now have something else
# what self is doing is that is it represents the potential object
# once you make this blueprint
# let's try another method

# start indented
    # def add_legs(self, num):
    #     self.legs += num

# example of Polymorphism
class Floor(object):
    def __init__(self, stuff=None):
        self.stuff = stuff if stuff else []
    def drop_stuff(self, stuff):
        self.stuff.append(stuff)
    def clean(self):
        self.stuff = []

# since you have similar methods, you can iterate over different objects
# and they can "work" in the same space together

# another example
# class Books(object):
#     def__init__(self):
#         self.books = []
#     def add book(self, book):
#         self.books.append(book)

# pero why do this? if you have a class na init and one function, wag na
# if you are going to do this, just make a function
# write a lot of functions, ok lang yun
# write functions first
# if it will be worthwhile, then write out code to specify what the class would do
# plan on how to interact with this object? then decide to make a class

# PYTHON WORKFLOWS
# automated testing
# in a large code base or a larger company, you want to make sure that your
# code works, you commit that to your repo and then you push it onto github
# then it goes through automated testing to check if the code still works
# when developing locally on your laptop and you want to see if somethiing works
# if you are writing code in one editor
# and then you want to switch over to your terminal
# automated testing is built into python

# so let's do ayutomated testing

def foo(x):
    z = x+1
    # import pdb
    # pdb.set_trace()
    return z

# python has a package named unittest
# view test.py

# atom text editor flaking configuration

# sniffer scent.py

# autotesting, what the fuck?

# initialize sniffer by typing SNIFFER

def median(l):
    length = len(l)
    midway = length//2
    s=sorted(l)
    if length % 2 != 0:
        median_val = s[midway]
    else:
        median_val = (s[midway]+s[midway-1])/2.0
    return median_val

def median_after_throwing_out_outliers(l):
    return median(l)

print 'finished pdb_example_unsed_result'
print 'another print statement'
a = foo(2)
print 'finished foo again'


# pep is a styleguide for python --> follow pep standards (sonofabitch)
# flake
# flake8 is the combination of pep8 and flake

# don't debug with print statements
# python debugger

# how to use PDB?
# pdb_example_unsed_result = foo(1000)
# you have pdb and then run the python script
# then from there you can select what to print like -
# print x, print z
# we've learned
# c to continue until the next breakpoint
# n for next line
# w for where we area
# the variables - to see the variable values
# q for quit
