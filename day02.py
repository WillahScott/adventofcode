# Advent of code - DAY 2

from itertools import product

# Read data
with open("data/d02.txt") as f:
    data = f.read()


# -- Problem 1 function --
def checksum(data):
    out = 0

    for line in data.split('\n'):
        numbers = [int(x) for x in line.split()]
        out += max(numbers) - min(numbers)
    
    return out

# Test
#test = """5 1 9 5
#7 5 3
#2 4 6 8"""
# checksum(test)
  # > 18

# Run problem 1
checksum(data)
  # > 30994



# -- Problem 2 function --
def divsum(data):
    out = 0

    for line in data.split('\n'):
        numbers = [int(x) for x in line.split()]
        for a,b in product(numbers, numbers):
            if a != b:
                if a%b == 0:
                    out += a/b
                    break
                elif b%a == 0:
                    out += b/a
                    break
                
    return out

# Test
#test = """5 9 2 8
#9 4 7 3
#3 8 6 5"""
# divsum(test)
  # > 9.0

# Run problem 2
divsum(data)
  # > 233.0

