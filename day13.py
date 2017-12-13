# Advent of code - DAY 13

# Read data
with open('data/d13.txt') as f:
    raw_data = f.readlines()


# -- Problem 1 function --
def get_severity(d, verbose=False):
    severity = 0
    for line in d:
        depth, rang = [int(x) for x in line.split(': ')]
        
        if (start + depth) % ((rang-1)*2) == 0:
            # Caught!
            severity += depth * rang
            if verbose:
                print('CAUGHT: l={} range={}'.format(depth, rang))

    return severity

# Test
test ="""0: 3
1: 2
4: 4
6: 4""".split('\n')
get_severity(test, verbose=True)
  # > ?

# Run problem 1
get_severity(raw_data)
  # > 748



# -- Problem 2 function -- CRUDE VERSION (long computation)
def firewall(d, start=0, verbose=False):
    severity = 0
    for line in d:
        depth, rang = [int(x) for x in line.split(': ')]
        
        if (start + depth) % ((rang-1)*2) == 0:
        	return False
    else:
	    return True


def bypass_firewall(d, verbose=False):
    start = 0
    while not firewall(d, start, verbose=verbose):
        start += 1
    
    return start

# Test
bypass_firewall(test, verbose=True)
  # > 10

# Run problem 2
bypass_firewall(raw_data)
  # > 3873662  (takes ~12s)

