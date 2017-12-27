# Advent of code - DAY 24

# Read data
with open('data/d24.txt') as f:
    raw_data = f.readlines()
    
components = [ tuple(map(int,x.strip().split('/'))) for x in raw_data ]


class CompList(object):
    def __init__(self, comps):
        self.__comps = comps
        
        self.DICT = {}
        for t in self.__comps:
            self.add(t)
                
    def add(self, t):
        a,b = t
        self.DICT[a] = self.DICT.get(a,[]) + [(a,b)]
        if a != b:
            self.DICT[b] = self.DICT.get(b,[]) + [(a,b)]
    
    def get_possible(self, x):
        return sorted(self.DICT.get(x, []), key=lambda x: sum(x), reverse=True)

    def use(self, t):
        self.__comps.remove(t)
        self.DICT[t[0]].remove(t)
        if t[0] != t[1]:
            self.DICT[t[1]].remove(t)
        
    @staticmethod
    def other(t, x):
        return t[1] if x == t[0] else t[0]

    def copy(self):
        return CompList(self.__comps.copy())
    
    def __str__(self):
        return str(self.DICT)
    
    def __repr__(self):
        return str(len(self.__comps))


# -- Problem 1 function --
def get_strongest_path(components, *, verbose=False):
    active_port = 0
    strength = 0
    
    COMPLETE = []  # list of (strength, path)
    INCOMPLETE = [(0, strength, components, [])]  # list of (active_port, strength, components, path)

    
    while len(INCOMPLETE) > 0:
        
        active_port, strength, comps, path = INCOMPLETE.pop()
        cands = comps.get_possible(active_port)
        
        if len(cands) == 0:
            if verbose:
                print('FINISHED ({}) PATH: {}'.format(strength,path))
            COMPLETE.append((strength, path))

        else:
            for c in cands:
                new_comps = comps.copy()
                new_comps.use(c)
                
                act_port = comps.other(c, active_port)
                INCOMPLETE.append( (act_port, strength + sum(c), new_comps, path[:] + [c]) )

    return max(COMPLETE, key=lambda x: x[0])

# Test
components_alt = [(0,2),
(2,2),
(2,3),
(3,4),
(3,5),
(0,1),
(10,1),
(9,10)]
COMPS_ALT = CompList(components_alt)

get_path(COMPS_ALT, verbose=True)
  # > 19

# Run problem 1
COMPS = CompList(components)
get_strongest_path(COMPS, verbose=False)
  # > 1940



# -- Problem 2 function --

# Only changed the return line
def get_longest_path(components, *, verbose=False):
    active_port = 0
    strength = 0
    
    COMPLETE = []  # list of (strength, path)
    INCOMPLETE = [(0, strength, components, [])]  # list of (active_port, strength, components, path)

    
    while len(INCOMPLETE) > 0:
        
        active_port, strength, comps, path = INCOMPLETE.pop()
        cands = comps.get_possible(active_port)
        
        if len(cands) == 0:
            if verbose:
                print('FINISHED ({}) PATH: {}'.format(strength,path))
            COMPLETE.append((strength, path))

        else:
            for c in cands:
                new_comps = comps.copy()
                new_comps.use(c)
                
                act_port = comps.other(c, active_port)
                INCOMPLETE.append( (act_port, strength + sum(c), new_comps, path[:] + [c]) )

    return max(COMPLETE, key=lambda x: (len(x[1]), x[0]))


# Run problem 2
get_longest_path(COMPS, verbose=False)
  # > 1928

