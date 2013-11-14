# Name:Huong Le
# Evergreen Login: lethi17
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1


# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###



                
print "Problem 1 solution follows:"

import math


def solver( a, b, c):
        delta = (b*b) - (4*b*c)

        if delta < 0 :
                print ("None")
        
        elif delta == 0 :
                x = -b / (2 * a)
                print(x)
        
        elif delta > 0 :
                x1 = ( -b + math.sqrt( delta )) / (2 * a)
                x2 = ( -b - math.sqrt( delta )) / (2 * a)
                print ( str(x1) + " " + str(x2) )

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test.pdf
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f

###
### Problem 3
###

print "Problem 3 solution follows:"

# print "Problem 2 solution follows:"



import hw1_test

print ( str(hw1_tets.a)print ( str(hw1_test.a) + "\n" + str(hw1_test.b) + "\n" + str(hw1_test.c) + "\n" + str(hw1_test.d) + "\n" + str(hw1_test.e) + "\n" + str(hw1_test.f) )







###
### Collaboration
###

# ..I was working with Hien and Hao on this assignment.
###
### Reflectio
###

The first week was very confusing. I was very lost. This took us about 3 hrs to do. 
