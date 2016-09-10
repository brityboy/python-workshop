# from lecture import *
# but this is a bad practice
# uses a lot of memory
# this is oging to cause what's called namespace pollution
# it can happen that you import libraries where one function
# is similarly named as another functions
# example - sum is in both pandas and numpy - then tepok ka
# you want to make sure that you import only what you need so that
# you don't overwrite and confuse the namespace in python

# you can correct this with

#import W00D01 as week
#print week.sum_absolute_values([-1, 1])

#string = 'Brian'
#print 'Hello %f' % 3.141592

#print_string = 'Hello %s, you are %d years old'
#print print_string % ('Brian', 30)

#print_string = 'Hello {name}, you are {age} years old\nGood to meet you, {name}'
#print_string = 'Hello {0}, you are {1:.2f} years old\nGood to meet you, {0}'
#print print_string.format('Brian',30.45209)

#with open('W00D01.py') as f:
#    count = 0
#    for line in f:
#        if 'a' in line:
#            count += 1
#print count
#print 'Test\nOther'

#with open('thing.txt', 'w') as f:
#    f.write('This is a test')
