# Advent of code - DAY 5


# Read data
with open("data/d05.txt") as f:
    orig_data = [int(x) for x in f.readlines()]

    
# -- Problem 1 function --
def jumps_out(orig_data, verbose=False):
    data = orig_data[:]  # copy to avoid changing the data
    steps = 0
    position = 0
    len_data = len(data)
    
    while True:
        steps += 1
        jumpto = data[position]
        data[position] += 1
        position += jumpto
        if verbose:
            print(position)
            print(data[:10])
        
        if position < 0 or position >= len_data:
            if verbose:
                print(f'->{position}')
            break

    return steps

# Test
jumps_out([0,3,0,1,-3], verbose=True)
  # > 5

# Run problem 1
jumps_out(data)
  # > 376976



# -- Problem 2 function --
def jumps_out_2(orig_data, verbose=False):
    data = orig_data[:]  # copy to avoid changing the data
    steps = 0
    position = 0
    len_data = len(data)
    
    while True:
        steps += 1
        jumpto = data[position]
        data[position] += 1 if jumpto < 3 else -1
        position += jumpto
        if verbose:
            print(position)
            print(data[:10])
        
        if position < 0 or position >= len_data:
            if verbose:
                print(f'->{position}')
            break

    return steps

# Test
jumps_out_2([0,3,0,1,-3], verbose=True)
  # > 10

# Run problem 1
jumps_out_2(data)
  # > 29227751

