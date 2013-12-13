# Name: Huong Le     
# Evergreen Login: Lethi17  
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

for vowels in 'Python Is A Great Programming Language!':
    if vowels == 'constant':
        break 
    print 'number of vowels : ', vowels
    
    
for constants in 'Python Is A Great Programming Language!':
    if constants== 'constant':
        break 
    print 'number of constatns: ', constants


###
### Problem 4
###
print "Problem 4 solution follows:

hlist= [1, 2.2, 3, 4.2]
i = 0
while i < len(hlist):
    print hlist [i] 
    i = i + 1




hlist= [1, 2.2, 3, 4.2]
total = 0
i = 0
while i < len(hlist):
    total = total +hlist[i]
    
    i = i + 1
    
average = total / len(hlist)
print average





# DO NOT CHANGE THE FOLLOWING LINE



    


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

hlist= [1, 2.2, 3, 4.2]
tlist=[5.2, 6.8, 7.5]
list3= hlist +tlist 

total = 0
i = 0
while i < len(list3):
    total = total +list3[i]
    
    i = i + 1
    
average = total / len(list3)

hlist.append(tlist)

print average

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

# ... write your code and comments here (and remove this line)

###
### The website that I used was. http://www.tutorialspoint.com
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
