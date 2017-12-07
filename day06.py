# Advent of code - DAY 6

# Read data
with open('data/d06.txt') as f:
    orig_data = [ int(x) for x in f.read().spit() ]


# -- Problem 1 function --
def cycles(orig_data, verbose=False):
    data = orig_data[:]  # copy to avoid changing the data
    steps = 0
    len_data = len(data)

    history = { '-'.join(map(str, data)) }  # set

    while True:
        steps += 1
        pos_biggest, val_biggest = max(enumerate(data), key=lambda x: x[1])
        added = val_biggest // len_data
        rem = val_biggest % len_data
        data[pos_biggest] = 0

        if verbose:
            print(pos_biggest, val_biggest, '  a:', added, '  r:', rem)
            print([ (i-pos_biggest-1)%len_data < (rem) for i in range(len_data) ])

        new_data = [ x + added + ( (i-pos_biggest-1)%len_data < (rem) )
                    for i, x in enumerate(data) ]
        new_data_repr = '-'.join(map(str, new_data))

        if new_data_repr in history:
            if verbose:
                print(new_data_repr, '<=====')
            break
        else:
            if verbose:
                print(new_data_repr, '<=====')
            history.add(new_data_repr)
            data = new_data

    return steps

# Test
cycles([0,2,7,0], verbose=True)
  # > 5

# Run problem 1
cycles(orig_data)
  # > 12841



# -- Problem 2 function --
def cycles_loop(orig_data, verbose=False):
    data = orig_data[:]  # copy to avoid changing the data
    steps = 0
    len_data = len(data)

    history = { '-'.join(map(str, data)): 0 }  # dict

    while True:
        steps += 1
        pos_biggest, val_biggest = max(enumerate(data), key=lambda x: x[1])
        added = val_biggest // len_data
        rem = val_biggest % len_data
        data[pos_biggest] = 0

        if verbose:
            print(pos_biggest, val_biggest, '  a:', added, '  r:', rem)
            print([ (i-pos_biggest-1)%len_data < (rem) for i in range(len_data) ])

        new_data = [ x + added + ( (i-pos_biggest-1)%len_data < (rem) )
                    for i, x in enumerate(data) ]
        new_data_repr = '-'.join(map(str, new_data))

        if new_data_repr in history:
            if verbose:
                print(new_data_repr, '<=====')
            loop_size = steps - history[new_data_repr]
            break
        else:
            if verbose:
                print(new_data_repr, '<=====')
            history[new_data_repr] = steps
            data = new_data

    return loop_size

# Test
cycles_loop([0,2,7,0], verbose=True)
  # > 4

# Run problem 1
cycles_loop(orig_data)
  # > ?

