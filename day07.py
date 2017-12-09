# Advent of code - DAY 7

import re

# Read and Process data
PATTERN = re.compile('([a-zA-Z]*) \((\d*)\)(?: -> (.*))?')
def parse_data(raw):
    return [ re.findall(PATTERN, x)[0] for x in raw ]

with open('data/d07.txt') as f:
    raw_data = f.read()
orig_data = parse_data(raw_data)


# -- Problem 1 function --
def bottom_node(orig_data, verbose=False):
    NON_ROOTS = set()
    ROOTS = set()

    for node in orig_data:
        if node[2] == '':
            # No kids = leaf --> SKIP
            continue

        children = node[2].split(', ')
        NON_ROOTS.update(set(children))  # add kids to CHILDREN
        for k in children:
            if k in ROOTS:
                ROOTS.discard(k)

        # else --> could be parent
        if node[0] not in NON_ROOTS:
            if verbose:
                print('adding:', node[0], '   --> line:', node)
            ROOTS.add(node[0])

    # check for only one root at end
    if len(ROOTS) > 1:
        raise ValueError("Too many roots: {}".format(ROOTS))

    return ROOTS

# Test
test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n')

orig_test = parse_data(test)  # parse test data

bottom_node(orig_test, verbose=True)
  # > 'tknk'

# Run problem 1
bottom_node(orig_data)
  # > dgoocsw




# -- Problem 2 function --
class BalanceTree(object):
    PATTERN = re.compile('([a-zA-Z]*) \((\d*)\)(?: -> (.*))?')

    def __init__(self, verbose=False):
        self.WEIGHT = {}  # <node>: [<self-weight>, <kids-weights>* ]
        self.PART_WEIGHT = {}  # for unfinished, same format as WEIGHT
        self.PART_MISS = {}  # <parent-name>: [ <missing-leaf-nodes>* ]
        self.MISSING = {}  # <leaf-name>: <parent-node>
        self.CHILDREN = {}  # <node>: [ <leaf-nodes> ]
        self.verbose = verbose

    @classmethod
    def parse_line(cls, raw_line):
        return re.findall(cls.PATTERN, raw_line)[0]

    def update_missing(self, parent, kid):
        if kid in self.MISSING:
            self.MISSING[kid].append(parent)
        else:
            self.MISSING[kid] = [parent]


    def update_partweight(self, name, weight):
        if name in self.PART_WEIGHT:
            self.PART_WEIGHT[name].append(weight)
        else:
            self.PART_WEIGHT[name] = [weight]


    def update_weight(self, name, weight_list):
        self.WEIGHT[name] = weight_list

        # check if balanced
        _ws = set(weight_list[1:])
        if len(_ws) > 1:
            ch_weights = [ (k, self.WEIGHT[k][0], sum(self.WEIGHT[k]))
                           for k in self.CHILDREN[name] ]
            raise ValueError('{}:'.format(name), ch_weights)

        # check for partials waiting for the node
        weight = sum(weight_list)
        for n in self.MISSING.get(name, []):
            self.update_partweight(n, weight)  # append to partial
            self.PART_MISS[n].remove(name)  # update missing tracker

            if len(self.PART_MISS[n]) < 1:
                # Move from PART_WEIGHT to WEIGHT
                self.PART_MISS.pop(n)  # remove from PART_MISS
                weight_list = self.PART_WEIGHT.pop(n)
                self.update_weight(n, weight_list)

        self.MISSING.pop(name, None)  # None silences KeyError if not there


    def new_node(self, node):
        name = node[0]
        weight = int(node[1])
        children = node[2].split(', ')

        self.CHILDREN[name] = children

        if node[2] == '':
            # No kids = leaf --> record weight
            self.update_weight(name, [weight])

        else:

            if all([k in self.WEIGHT for k in children]):
                # add to self.WEIGHT
                self.update_weight(name, [weight] + [sum(self.WEIGHT[k]) for k in children])

            else:
                # Add to self.PART_WEIGHT and PART_MISS
                self.update_partweight(name, weight)
                self.PART_MISS[name] = []

                for k in children:
                    if k in self.WEIGHT:
                        self.update_partweight(name, sum(self.WEIGHT[k]))
                    else:
                        self.PART_MISS[name].append(k)
                        self.update_missing(parent=name, kid=k)


    def feed_data(self, node_data):
        for node_line in node_data:
            if self.verbose:
                print(node_line)
            self.new_node(self.parse_line(node_line))


# Test
testT = BalanceTree(verbose=True)
testT.feed_data(test)
  # ERROR reads:
  #   ValueError: ('tknk:', [('ugml', 68, 251), ('padx', 45, 243), ('fwft', 72, 243)])


# Run problem 2
dataT = BalanceTree(verbose=False)
dataT.feed_data(raw_data)
  # ERROR reads:
  #   ValueError: ('jfdck:', [('marnqj', 1283, 1823), ('moxiw', 184, 1815),
  #                ('sxijke', 987, 1815), ('ojgdow', 15, 1815), ('fnlapoh', 1284, 1815)])

