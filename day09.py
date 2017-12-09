# Advent of code - DAY 9

import re


# Read data
with open('data/d09.txt') as f:
    orig_data = f.read()


# -- Problem 1 function --
G_PAT = re.compile(r"(<[^!>]*(?:(?:!.)*|[^!>]*)*>)(.*)")

def parse_garbage(text, verbose=False):
    # find next (valid) '>'
    garb, rest = G_PAT.search(text).groups()
    if verbose:
        print('GARB:', garb, '   -Rest:', rest)
    return rest

def group_score(orig_text, base=0, verbose=False):
    SCORES = []
    text = orig_text

    while text != '':
        # Garbage: parse and discard from text
        if text[0] == '<':
            text = parse_garbage(text, verbose=verbose)

        # Group start -- parse interior with base+1
        elif text[0] == '{':
            if verbose:
                print('Opening group with (new) base={}'.format(base+1))
            text = text[1:]
            base += 1

        # Group end -- return the base and parse the rest with the one less base (siblings)
        elif text[0] == '}':
            SCORES.append(base)
            text = text[1:]
            base -= 1

        # Any other character --> discard and keep going with same base
        else:
            if verbose:
                print('next')
            text = text[1:]

    # when no more text -- return SCORES
    return sum(SCORES)

# Test
group_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')
  # > 9

# Run problem 1
group_score(orig_data)
  # > 20530



# -- Problem 2 function --
def score_garbage(orig_text):
    # find next (valid) '>'
    text = orig_text[1:]  # remove first '<'
    score = 0
    while text != '':
        if text[0] == '!':
            text = text[2:]
        elif text[0] == '>':
            return score, text[1:]
        else:
            score += 1
            text  = text[1:]

def group_garb_score(orig_text):
    SCORE = 0
    text = orig_text

    while text != '':
        # Garbage: parse and discard from text
        if text[0] == '<':
            sc, text = score_garbage(text)
            SCORE += sc

        # Any other character --> discard and keep going with same base
        else:
            text = text[1:]

    # when no more text -- return SCORE
    return SCORE

# Test
group_garb_score('<{o"i!a,<{i<a>')
  # > 10

# Run problem 2
group_garb_score(orig_data)
  # > 9978

