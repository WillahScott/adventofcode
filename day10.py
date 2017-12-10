# Advent of code - DAY 10

from functools import reduce


# Read data
with open('data/d10.txt') as f:
    data = [ int(x) for x in f.read().split(',') ]


# -- Problem 1 function --
def elve_hash(lengths, init_list_length, verbose=False):
    skip = 0
    pos = 0
    data = [ i for i in range(init_list_length) ]
    LENGTH = len(data)

    for n in lengths:
        if verbose:
            print('length:', n, data, 'pos:', pos)

        if pos+n < LENGTH:
            # no wraparound
            data[pos: pos+n] = data[pos: pos+n][::-1]
            if verbose:
                print('  f-sub', data[pos: pos+n])
        else:
            # Wraparound -- get data, then assign to correct part
            subl = (data[pos:] + data[:(pos+n)%LENGTH])[::-1]
            data[pos:] = subl[:LENGTH-pos]
            data[:(pos+n)%LENGTH] = subl[LENGTH-pos:]
            if verbose:
                print('  flipped-sub', subl)

        # Update pos and skip
        pos = (pos + n + skip) % LENGTH
        if verbose:
            print('  -> ', data, 'new pos:', pos, '\n')
        skip += 1

    return data[0] * data[1]

# Test
elve_hash([3, 4, 1, 5], 5, verbose=True)
  # > 12

# Run problem 1
elve_hash(data, 256)
  # > 52070



# -- Problem 2 function --
with open('data/d10.txt') as f:
    new_data = f.read()

def elve_round_hash(length_str, rounds=64, init_list_length=256, verbose=False):
    lengths = [ ord(x) for x in length_str ] + [17, 31, 73, 47, 23]
    skip = 0
    pos = 0
    data = [ i for i in range(init_list_length) ]
    LENGTH = len(data)

    for _r in range(rounds):
        for n in lengths:
            if verbose:
                print('length:', n, data, 'pos:', pos)

            if pos+n < LENGTH:
                # no wraparound
                data[pos: pos+n] = data[pos: pos+n][::-1]
                if verbose:
                    print('  f-sub', data[pos: pos+n])
            else:
                # Wraparound -- get data, then assign to correct part
                subl = (data[pos:] + data[:(pos+n)%LENGTH])[::-1]
                data[pos:] = subl[:LENGTH-pos]
                data[:(pos+n)%LENGTH] = subl[LENGTH-pos:]
                if verbose:
                    print('  flipped-sub', subl)

            # Update pos and skip
            pos = (pos + n + skip) % LENGTH
            if verbose:
                print('  -> ', data, 'new pos:', pos, '\n')
            skip += 1

    dense_hash = [ reduce(lambda a,b: a^b, data[(16*p):(16*p)+16]) for p in range(16) ]

    hex_rep = ''.join([ hex(n)[2:] if len(hex(n)) == 4 else '0'+ hex(n)[2:]
                        for n in dense_hash ])
      # corrects for single digit hex: 0xe --> 0e (instead of just e)

    return hex_rep

# Test
elve_round_hash('')
  # > 'a2582a3a0e66e6e86e3812dcb672a272'

# Run problem 2
elve_round_hash(new_data)
  # > '7f94112db4e32e19cf6502073c66f9bb'

