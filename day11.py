# Advent of code - DAY 11

from itertools import groupby

# Read data
with open('data/d11.txt') as f:
    new_data = f.read().split(',')


# -- Problem 1 function --
def get_path_dict(steps):
    gpb = groupby(sorted(steps))

    return { i: len(list(v)) for i, v in gpb }



OPP = [('n', 's'), ('ne', 'sw'), ('nw', 'se')]
DIAG = { 'n': {'sw': 'nw', 'se': 'ne'},
         'nw': {'s': 'sw', 'ne': 'n'},
         'ne': {'s': 'se', 'nw': 'n'},
         's': {'nw': 'sw', 'ne': 'se'},
         'sw': {'n': 'nw', 'se': 's'},
         'se': {'n': 'ne', 'sw': 's'},
       }

def reduce_path(long_path_d, verbose=False):
    int_path = []

    # reduce opposites - sort by max to min
    for i, j in OPP:
        _steps = long_path_d[i] - long_path_d[j]
        int_path.append([i if _steps > 0 else j, abs(_steps)])
    int_path.sort(key=lambda x: x[1], reverse=True)

    if verbose:
        print('No opps:', int_path)

    # reduce diagonals
    red_path = {}

    while int_path:
        k_red, v_red = int_path.pop(0)  # to reduce
        pos_reds = DIAG[k_red]  # possible reductions

        for k, v in int_path:
            if k in pos_reds:
                # reduce and remove the other with which we reduced
                red_path[pos_reds[k]] = red_path.get(pos_reds[k],0) +  v
                int_path.remove([k,v])

                left = v_red - v
                if left > 0:  # if there is still left
                    int_path.append( [k_red, left] )
                    int_path.sort(key=lambda x: x[1], reverse=True)

                break
        else:
            # the item is irreducible
            red_path[k_red] = red_path.get(k_red,0) + v_red

    if verbose:
        print('PATH:', red_path )

    return sum(red_path.values())

# Test
  # > ?

# Run problem 1
reduce_path( get_path_dict(new_data), verbose=True )
  # > 707  ## PATH: {'n': 317, 'nw': 390}



# -- Problem 2 function --
PAST_PATH = []
max_steps = 0
for d in new_data:
    PAST_PATH.append(d)
    max_steps = max( max_steps, reduce_path(get_path_dict(PAST_PATH)) )

# Run problem 2
print(max_steps)
  # > 1490

