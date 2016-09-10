from collections import defaultdict
import numpy as np

#take advantage of the dictionary
#make sure that the keys are tuples referring to the indices


class SparseMatrix(object):
    def __init__(self, n, m, default=0):
        self.n = n
        self.m = m
        # self.mat = defaultdict(int)
        # self.mat = defaultdict(float)
        self.mat = {}
        self.default = default

    def __repr__(self):
        result = ''
        for i in xrange(0, self.n):
            printstring = ''
            for j in xrange(0, self.m):
                if (i, j) in self.mat:
                    value = self.mat[(i, j)]
                else:
                    value = self.default
                # printstring += '{}.00\t'.format(value)
                printstring += '{0:.2f}\t'.format(value)
            result += printstring+'\n'
        return result

    def __setitem__(self, key, value):
        # self.n, m = key
        self.mat[key] = value

    def __getitem__(self, key):
        # if self.mat[key] == 0:
        #     return self.default
        # return self.mat[key]
        return self.mat.get(key, self.default)

#mat=SparseMatrix(3, 5)
