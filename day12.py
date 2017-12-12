# Advent of code - DAY 12

# Read data
with open('data/d12.txt') as f:
    raw_data = f.readlines()


# -- Problem 1 function --
class PipeVillage(object):

    def __init__(self):
        self.PIPES = {}
        self.CC_zero = { 0 }  # set

    def update_CC(self, sinks):
        for s in sinks:
            if s not in self.CC_zero:
                self.CC_zero.add(s)
                for ss in self.PIPES.get(s,[]):
                    # check update of children as well
                    if ss not in self.CC_zero:
                        self.update_CC([ss])

    def parse_data(self, raw_data):
        for line in raw_data:
            # Parse line: source <-> [ sinks ]
            _src, _snk = line.split(' <-> ')
            source = int(_src)
            sinks = [ int(s) for s in _snk.split(',') ]

            # add to pipes
            self.PIPES[source] = sinks

            # update connected component
            if source in self.CC_zero:
                self.update_CC(set(sinks))


# Run problem 1
pv = PipeVillage()
pv.parse_data(raw_data=raw_data)
print(len(pv.CC_zero))
  # > 380



# -- Problem 2 function --
class PipeVillageCC(object):

    def __init__(self):
        self.PIPES = {}
        self.CComponents = []  # list of sets (each CC)

    def update_CCs(self, cc):
        to_merge = []
        for i, _cc in enumerate(self.CComponents):
            if len(_cc.intersection(cc)) > 0:
                to_merge.insert(0, i)    # to_merge will be ordered desc -- see next loop

        for ind_mcc in to_merge:  # so as to preserve index for popping here
            mcc = self.CComponents.pop(ind_mcc)
            cc.update(mcc)

        self.CComponents.append(cc)


    def parse_data(self, raw_data):
        for line in raw_data:
            # Parse line: source <-> [ sinks ]
            _src, _snk = line.split(' <-> ')
            source = int(_src)
            sinks = [ int(s) for s in _snk.split(',') ]

            # add to pipes
            self.PIPES[source] = sinks

            self.update_CCs( set([source] + sinks) )

# Run problem 2
pv2 = PipeVillageCC()
pv2.parse_data(raw_data=raw_data)
print(len(pv2.CComponents))
  # > 181

