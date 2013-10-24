series = raw_input("asnswer ")
n= 3

# series = "fibonacci" 

def lab3():
    if series == "fibonacci":
        return sum(range(0, 3 * n + 1, 3)) 
    elif series == 'sum':
        return 1000
    else:
        return 0
        
print lab3() + 1