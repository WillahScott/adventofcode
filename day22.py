# Advent of code - DAY 22

# Read data
with open('data/d22.txt') as f:
    data = f.readlines()

BOARD = np.array([ [0 if x == '.' else 1 for x in l.strip()] for l in data])


# -- Problem 1 function --
def print_board(board, pos):
    for i,l in enumerate(board):
        line = ' ' + ' '.join(['#' if x else '.' for x in l])
        if i == pos[0]:
            print(line[:pos[1]*2] + '[' + line[pos[1]*2+1] + ']' + line[pos[1]*2+3:])
        else:
            print(line)

def extend_UL(orig):
    n = orig.shape[0]
    _aux = np.hstack([np.zeros((n,2)) , orig])
    return np.vstack([np.zeros((2,n+2)) , _aux])

def extend_DR(orig):
    n = orig.shape[0]
    _aux = np.hstack([orig, np.zeros((n,2))])
    return np.vstack([_aux, np.zeros((2,n+2))])

# DIRECTIONS = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}

def next_pos(current, direction):
    if direction == 0:  # UP -> -1,0
        return [current[0]-1, current[1]]
    elif direction == 1:  # RIGHT -> 0,+1
        return [current[0], current[1]+1]
    elif direction == 2:  # DOWN -> +1,0
        return [current[0]+1, current[1]]
    elif direction == 3:  # LEFT -> 0,-1
        return [current[0], current[1]-1]
    else:
        raise ValueError('Invalid direction {}'.format(direction))

def virus_move(current, direction, infected):
    if infected:
        # turn to the right
        new_direction = (direction + 1) % 4 
    else:
        # turn to the left
        new_direction = (direction - 1) % 4 
    # move forward
    return next_pos(current, new_direction), new_direction

def virus_live(board, num_bursts, *, verbose=False):
    infections = 0
    board = board.copy()
    
    # Initialize position
    position = [ n//2 for n in board.shape ]  # center of the board
    direction = 0  # up

    for s in range(num_bursts):
        if verbose:
            print('\nPOSITION: {}'.format(position), end='')
            
        # Check if we need to extend the board
        if min(position) < 0:
            board = extend_UL(board)
            position = [ x+2 for x in position ]
            if verbose:
                print(' -> {}'.format(position), end='')
        elif max(position) >= max(board.shape):
            board = extend_DR(board)
            if verbose:
                print(' -> {}'.format(position), end='')

        if verbose:
            print('')
            print_board(board, position)

        val = board.item(*position)
        infections += (val^1)
        
        if verbose and (val^1):
            print('+++ INF (Total: {})'.format(infections))
        
        board.itemset(*position, val ^ 1)
        position, direction = virus_move(position, direction, val)
    print('\n\n Infections: {}'.format(infections))
    return infections, board


# Test
test_data = """..#
#..
...""".split('\n')

TEST_BOARD = np.array([ [0 if x == '.' else 1 for x in l.strip()] for l in test_data])

inf, brd = virus_live(TEST_BOARD, 70, verbose=False)
print_board(brd, (0,0))
  # > 41

# Run problem 1
inf, brd = virus_live(BOARD, 10000, verbose=False)
  # > 5404



# -- Problem 2 function --
STATUS = { 0: '.', 1: 'W', 2: '#', 3: 'F' }

def print_board2(board, pos):
    for i,l in enumerate(board):
        line = ' ' + ' '.join([STATUS[x] for x in l])
        if i == pos[0]:
            print(line[:pos[1]*2] + '[' + line[pos[1]*2+1] + ']' + line[pos[1]*2+3:])
        else:
            print(line)

# DIRECTIONS = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}
def virus_move2(current, direction, status):
    if status == 0:  # CLEAN -> LEFT
        new_direction = (direction - 1) % 4 
    elif status == 1:  # WEAKENED -> continue
        new_direction = direction
    elif status == 2:  # INFECTED -> RIGHT
        new_direction = (direction + 1) % 4 
    elif status == 3:  # FLAGGED -> reverse
        new_direction = (direction + 2) % 4 
    # move forward
    return next_pos(current, new_direction), new_direction

def virus_live2(board, num_bursts, *, verbose=False):
    infections = 0
    board = board.copy()
    
    # Initialize position
    position = [ n//2 for n in board.shape ]  # center of the board
    direction = 0  # up

    for s in range(num_bursts):
        if verbose:
            print('\nPOSITION: {}'.format(position), end='')
            
        # Check if we need to extend the board
        if min(position) < 0:
            board = extend_UL(board)
            position = [ x+2 for x in position ]
            if verbose:
                print(' -> {}'.format(position), end='')
        elif max(position) >= max(board.shape):
            board = extend_DR(board)
            if verbose:
                print(' -> {}'.format(position), end='')

        if verbose:
            print('')
            print_board2(board, position)

        val = board.item(*position)
        if val == 1:  # weakened
            infections += 1
        
        if verbose and (val == 1):
            print('+++ INF (Total: {})'.format(infections))
        
        board.itemset(*position, (val + 1)%4 )
        position, direction = virus_move2(position, direction, val)  # old `val`
    print('\n\n Infections: {}'.format(infections))
    return infections, board


# Test
inf, brd = virus_live2(TEST_BOARD*2, 100, verbose=False)  # multiply BOARD by 2 to update
  # > 26
inf, brd = virus_live2(TEST_BOARD*2, 10000000, verbose=False)  # multiply BOARD by 2 to update
  # > 2511944

# Run problem 2
inf, brd = virus_live2(BOARD*2, 10000000, verbose=False)  # multiply BOARD by 2 to update
  # > 2511672

