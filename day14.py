# Advent of code - DAY 14
from day10 import elve_round_hash as hex_hash

import numpy as np
from scipy import ndimage  # will use label


# -- Problem 1 function --
def get_used(key):
    total = 0
    for post in range(128):
        total += sum([sum(map(int, bin(int('0x{}'.format(i), 16))[2:]))
                        for i in hex_hash('{}-{}'.format(key, post))])

    return total

# Test
get_used('flqrgnkx')
  # > 8108

# Run problem 1
get_used('jzgqcdpd')
  # > 8074



# -- Problem 2 function --
def get_regions(key):
    MAP = []
    for post in range(128):
        MAP.append(''.join([bin(int('0x{}'.format(i), 16))[2:].zfill(4)
                    for i in hex_hash('{}-{}'.format(key, post))]))
    
    # convert to numpy array
    data = np.array([ [int(x) for x in m] for m in MAP ])
    
    region_map, num_regions = ndimage.label(data)
      # TODO: implement own version
    
    return num_regions 

# Test
get_regions('jzgqcdpd')
  # > 1242

# Run problem 2
get_regions('jzgqcdpd')
  # > 1212

