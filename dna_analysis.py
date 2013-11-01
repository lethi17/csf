# Name Huong Le 
# Evergreen Login: Lethi17
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0



# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        
# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
##################################################################


# for each base pair in string,
totalat_count2 = 0

at_count = 0

for at in seq:
    #  increment the total numver of ATs we've seen 
    totalat_count2 = totalat_count2 + 1
    
    # next, if the bp is a A or a T,
    if at == 'A' or at =='T':
        # increment the count of AT
        at_count = at_count +1
        

at_content = float(at_count)/totalat_count2        
        
################################################################
totalcount3 = 0

a_count=0 
t_count=0
g_count=0
c_count=0

for bp in seq:
    totalcount3 = totalcount3 + 1 

    if bp == 'A':
       a_count = a_count + 1
    elif bp == 'T':
        t_count = t_count + 1
    elif bp == 'G':
        g_count = g_count + 1
    elif bp == 'C':
        c_count = c_count + 1
        
a_count = float(a_count) / totalcount3
t_count = float(t_count) / totalcount3
g_count = float(g_count) / totalcount3
c_count = float(c_count) / totalcount3 
##############################################################      
numbercount = 0

numbercount = a_count + t_count + g_count + c_count       
        
        
ratio = gc_count / numbercount 

#(a+t)/(g+c)

ratio2 = at_content / gc_content


HighGC = 0
LowGC = 0 

HighGC = numbercount * .60
LowGC = numbercount * .40

if gc_content > HighGC:
    print 'High GC content'
elif gc_content < LowGC:
    print 'Low GC content'
else: 
    print 'moderate GC content'
###############################################################


# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content

print 'A-content:', a_count
print 'T-content:', t_count
print 'G-content:', g_count
print 'C-content:', c_count

print 'total A,T,C,G:', numbercount  

print 'variable:', totalat_count2 
print 'lenght:', len(seq) 

print 'GC content test:', ratio
print 'ratio;', ratio2
########################



########################################