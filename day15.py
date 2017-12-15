# Advent of code - DAY 15



# -- Problem 1 function --
def get_matches(start_A, start_B, rounds=5, verbose=False):
    genA = 16807
    genB = 48271
    div = 2147483647

    a = start_A
    b = start_B
    matches = 0
    for r in range(rounds):
        # update values
        a = (a * genA) % div
        b = (b * genB) % div

        # check match
        if bin(a)[-16:] == bin(b)[-16:]:
            matches += 1
            if verbose:
                print('Round {} MATCH!'.format(r))
    return matches

# Test
get_matches(65, 8921, rounds=5, verbose=True)
  # > 1

# Run problem 1
get_matches(703, 516, rounds=4*10**7)
  # > 594  # Aprox 40s time (no speedup with numba.autojit)



# -- Problem 2 function --
def get_matches_mults(start_A, start_B, rounds=5, verbose=False):
    genA = 16807
    genB = 48271
    div = 2147483647

    a = start_A
    b = start_B
    matches = 0
    for r in range(rounds):
        # update values
        while True:
            a = (a * genA) % div
            if (a % 4) == 0:
                break
        while True:
            b = (b * genB) % div
            if (b % 8) == 0:
                break
        
        # check match
        if bin(a)[-16:] == bin(b)[-16:]:
            matches += 1
            if verbose:
                print('Round {} MATCH!'.format(r))
    return matches

# Test
get_matches_mults(65, 8921, rounds=5*10**6)
  # > 309

# Run problem 2
get_matches_mults(703, 516, rounds=5*10**6)
  # > 328  # Aprox 20s time (no speedup with numba.autojit)

