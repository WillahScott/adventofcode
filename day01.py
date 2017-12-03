# Advent of code - DAY 1

from itertools import groupby

# Read data
with open("data/d01.txt") as f:
    data = f.read().strip()


# -- Problem 1 function --
def sum_reps(number):
    # add first number to the end
    looped_number = str(number) + str(number)[0]
    
    # running count of sum_reps
    out = 0
    
    for i,_reps in groupby(looped_number):
        reps = list(_reps)  # iter to list
        if len(reps) > 1:
            out += (len(reps)-1) * int(i)
    
    return out

# Alternative function
def sum_reps_alt(number):
        
    # add first number to the end
    looped_number = str(number) + str(number)[0]

    # running count of sum_reps
    out = 0
    
    for i, n in enumerate(looped_number[:-1]):
        if n == looped_number[i+1]:
            out += int(n)
            
    return out

# Tests
#sum_reps(1122)
#sum_reps(1111)
#sum_reps(1234)
#sum_reps(91212129)

# Run problem 1
sum_reps(data)



# -- Problem 2 function --
def sum_nexthalf(number):
        
    # get the jump increment (half the length)
    jump = len(number) / 2
    
    # double the number to not run out of space
    looped_number = str(number) + str(number)[:jump]

    # running count of sum_nexthalf
    out = 0    
    
    for i, n in enumerate(looped_number[:-1]):
        if n == looped_number[i+jump]:
            out += int(n)
            
    return out

# Tests
#print(sum_nexthalf(1212))
#print(sum_nexthalf(1221))
#print(sum_nexthalf(123425))
#print(sum_nexthalf(123123))
#print(sum_nexthalf(12131415))

# Run problem 2
sum_nexthalf(data)


