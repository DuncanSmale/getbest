import unittest
import getbest

class testMarks(unittest.TestCase):

        def cols(self):
                cols = [1,1]
                testcols = getbest.getCols("data/bestdat0.csv")
                self.assertEquals(cols,testcols)

        def mark(self):
                bestindex,bestmark = getbest.findtop("data/bestdat0.csv",4,1)
                self.assertEquals(bestmark,90)
        
