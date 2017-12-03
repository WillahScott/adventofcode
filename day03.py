# Advent of code - DAY 3

from itertools import product

# Read data
with open("data/d03.txt") as f:
    data = f.read()


# -- Problem 1 function --
def midpoints(layer):
    return [layer**2 + int((layer+1)/2) + i*(layer+1) for i in range(4)]

def get_steps(x):
    for steps in range(1000):
        if (2*steps + 1)**2 > x:
            break
    layer = 2*steps - 1
    mps = midpoints(layer)
    d_mps = [abs(m - x) for m in mps]
    tras = min(d_mps)

    print('steps:', steps)
    print('last_layer:', layer)
    print('midpoints:', '-'.join([str(k) for k in mps]))
    print('distance to mp:', '-'.join([str(k) for k in d_mps]))
    print('\n LAYER {} + TRAS {} = {}'.format(steps, tras, steps + tras))
    
    return steps + tras


# Run problem 1
get_steps(312051)
  # > 430



# -- Problem 2 function --
class Board(dict):
    def __init__(self, starting=None):
        self.__b = {'0;0': 1}
        self.last_pos = [0,0]
    
    @staticmethod
    def __pos2str(r,c):
        return '{};{}'.format(r,c)

    @staticmethod
    def __str2pos(s):
        return [ int(x) for x in s.split(';') ]
    
    def insert(self,r,c, value):
        self.__b.update({self.__pos2str(r,c): value})
        
    def find(self, r,c):
        return self.__b.get(self.__pos2str(r,c), 0)
    
    @staticmethod
    def next_pos(r, c):
        if abs(r) > abs(c):  # VERTICAL
            if r > 0:  # right vertical
                return r, c+1
            else:  # left vertical
                return r, c-1
        elif abs(r) < abs(c):  # HORIZONTALS
            if c > 0:  # upper horizontal
                return r-1, c
            else:  # lower horizontal
                return r+1, c
        else:  # CORNERS (|r| == |c|)
            if r > 0 and c < 0:  # lower right -> new layer
                return r+1, c
            elif r > 0 and c > 0:  # upper right
                return r-1, c
            elif r < 0 and c > 0:  # upper left
                return r, c-1
            elif r < 0 and c < 0:  # lower left
                return r+1, c
            else:  # 0,0
                return 1,0
    
    def step(self):
        nr, nc = self.next_pos(*self.last_pos)
        
        # get value of next square by summing surrounding values
        nextv = 0
        sq = product([-1,0,1], [-1,0,1])
        for i,v in sq:
            nextv += self.find(nr+i, nc+v)

        # insert new square to board, update last_pos
        self.insert(nr, nc, nextv)
        self.last_pos = [nr, nc]
        
        return nextv

    def __repr__(self):
        return repr(self.__b)


# Run problem 2
board = Board()

while True:
    _next = board.step()
    if _next > 312051:
        break

print(board)
  # > 312453

