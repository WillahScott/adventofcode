# Advent of code - DAY 16
import string


# Read data
with open('data/d16.txt') as f:
    orig_data = f.read()


# -- Problem 1 function --
def dance(moves, start, *, verbose=False):
    PROGRAMS = list(start)    
    
    for m in moves:
        if m[0] == 's':
            # SPIN
            p = int(m[1:])
            PROGRAMS = PROGRAMS[-p:] + PROGRAMS[:-p]
        
        elif m[0] == 'x':
            # Exchange
            i1, i2 = [ int(i) for i in m[1:].split('/') ]
            PROGRAMS[i1], PROGRAMS[i2] = PROGRAMS[i2], PROGRAMS[i1]
        
        elif m[0] == 'p':
            # PARTNER
            p1, p2 = m[1:].split('/')
            i1 = PROGRAMS.index(p1)
            i2 = PROGRAMS.index(p2)
            PROGRAMS[i1], PROGRAMS[i2] = PROGRAMS[i2], PROGRAMS[i1]
        
        else:
            raise ValueError('Unknown move:', m)
        
        if verbose:
            print('{:>6}'.format(m), '::', ''.join(PROGRAMS))
    
    return ''.join(PROGRAMS)

# Test
dance(['s1', 'x3/4', 'pe/b'], string.ascii_lowercase[:5], verbose=True)
  # > baedc

# Run problem 1
dance(raw_data, string.ascii_lowercase[:16])
  # > iabmedjhclofgknp



# -- Problem 2 function --
def repeat_dance(dance_moves, *, total=16, times=10**9):
    
    # Get ORDER OF PERMUTATION first
    START = string.ascii_lowercase[:total]
    current = START[:]  # copy
    perms_done = 0
    HIST = { 0: START }

    while True:
        current = dance(dance_moves, current)
        perms_done += 1
        # add to history
        HIST[perms_done] = ''.join(current)
        
        if current == START:
            ORDER = perms_done
            break
    
    print('Order of permutation:', ORDER)
    
    # Return the final program arrangement
    return HIST[ times % ORDER ]


# Test
repeat_dance(['s1', 'x3/4', 'pe/b'], total=5, times=2)
  # > ceadb

# Run problem 2
repeat_dance(raw_data, total=16, times=10**9)
  # > oildcmfeajhbpngk

