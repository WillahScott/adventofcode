# Advent of code - DAY 4


# Read data
with open("data/d04.txt") as f:
    data = f.read()


# -- Problem 1 function --
def valid_passphrases(pps):
    out = 0

    for passp in pps:
        words = passp.split()
        if len(words) == len(set(words)):
            out += 1
                
    return out

# Run problem 1
passphrases = data.split('\n')
valid_passphrases(passphrases)
  # > 455



# -- Problem 2 function --
def valid_passphrases_no_ana(pps):
    out = 0

    for passp in pps:
        words = passp.split()
        if len(words) == len(set([frozenset(w) for w in words])):
            out += 1
                
    return out

# Run problem 2
valid_passphrases_no_ana(passphrases)
  # > 186

