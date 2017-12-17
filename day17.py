# Advent of code - DAY 17


# -- Problem 1 function --
def spinlock(jump_size, *, last_insertion=2017, verbose=False):
    current_pos = 0
    BUFFER = [ 0, ]

    # Get new position and insert
    for step in range(1, last_insertion+1):
        current_pos = (current_pos+jump_size) % len(BUFFER) + 1
        BUFFER.insert(current_pos, step)

        if verbose:
            print(current_pos, BUFFER)

    # Return the last position and the next element
    return BUFFER[current_pos : current_pos+2]

# Test
spinlock(3, last_insertion=9, verbose=True)
  # > [9, 5]

# # Run problem 1
spinlock(316, last_insertion=2017)
  # > [2017, 180]



# -- Problem 2 function --
def spinlock_nobuff(jump_size, *, last_insertion=2017):
    current_pos = 0
    len_BUFFER = 1
    
    last_next = None

    for step in range(1, last_insertion+1):
        current_pos = (current_pos+jump_size) % len_BUFFER + 1
        len_BUFFER += 1
        
        if current_pos == 1:
            last_next = step
                
    return last_next

# Run problem 2
spinlock_nobuff(316, last_insertion=50000000)
  # > 13326437

