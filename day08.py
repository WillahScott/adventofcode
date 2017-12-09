# Advent of code - DAY 8

# Read data
with open('data/d08.txt') as f:
    raw_data = f.readlines()


# -- Problem 1 function --
def get_max_register(data_lines, verbose=False):
    REGISTERS = {}
    CONDITION = 'REGISTERS.get("{creg}", 0) {rest}'
    OP = {'inc': '+', 'dec': '-'}
    UPD_REG = 'REGISTERS.get("{reg}", 0) {op} {amt}'

    for line in data_lines:
        _pre, cond = line.split(' if ')
        reg, op, _amt = _pre.split()
        amt = int(_amt)

        cond_reg = cond.split()[0]
        rest_cond = ' '.join(cond.split()[1:])

        if eval( CONDITION.format(creg=cond_reg, rest=rest_cond) ):
            REGISTERS[reg] = eval(UPD_REG.format(reg=reg, op=OP[op], amt=amt))
            if verbose:
                print(reg, '->', REGISTERS[reg])

    return max(REGISTERS.items(), key=lambda x: x[1] )

# Test
get_max_register(test, verbose=True)
  # > ('a', 1)

# Run problem 1
get_max_register(raw_data)
  # > ('oui', 6061)



# -- Problem 2 function --
def get_max_hist_register(data_lines, verbose=False):
    REGISTERS = {}
    CONDITION = 'REGISTERS.get("{creg}", 0) {rest}'
    OP = {'inc': '+', 'dec': '-'}
    UPD_REG = 'REGISTERS.get("{reg}", 0) {op} {amt}'

    max_so_far = 0

    for line in data_lines:
        _pre, cond = line.split(' if ')
        reg, op, _amt = _pre.split()
        amt = int(_amt)

        cond_reg = cond.split()[0]
        rest_cond = ' '.join(cond.split()[1:])

        if eval( CONDITION.format(creg=cond_reg, rest=rest_cond) ):
            REGISTERS[reg] = eval(UPD_REG.format(reg=reg, op=OP[op], amt=amt))
            if verbose:
                print(reg, '->', REGISTERS[reg])

            max_so_far = max(max_so_far, REGISTERS[reg])

    return max_so_far

# Test
get_max_hist_register(test, verbose=True)
  # > 10

# Run problem 2
get_max_hist_register(raw_data)
  # > 6696

