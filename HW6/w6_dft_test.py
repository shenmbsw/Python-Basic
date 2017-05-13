# AUTHOR Shen Shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu

import unittest
from w6_dft import DFT
import random
import numpy as np

class DFTTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_type(self):
        N=5
        a = np.zeros(N, complex)
        for n in range(N):
            a[n] = (-1 + 2 * random.random()) + (-1 + 2 * random.random())*1j
            y = DFT(a)
            self.assertIsInstance(y, np.ndarray)

    def test_imputtype(self):
        a="2+3j,3+5j,2"
        self.assertRaises(ValueError,DFT,a)
        a=['h',2+3j]
        self.assertRaises(ValueError,DFT,a)
        a={1:2j,2:2j}
        self.assertRaises(ValueError,DFT,a)
        try:
            DFT([2+3j])
        except:
            self.fail()

    def test_shape(self):
        for N in [5,8,10]:
            a = np.zeros(N, complex)
            for n in range(N):
                a[n] = (-1 + 2 * random.random()) + (-1 + 2 * random.random())*1j
                y = DFT(a)
                temp=np.array(y)
                self.assertEqual(temp.shape, (N,))
    def test_std(self):
        for N in range(2, 21):
            a = np.zeros(N, complex)
            for i in range(0, 10):
                for n in range(0, N):
                    a[n] = (-1 + 2 * random.random()) + (-1 + 2 * random.random())*1j
                    y=DFT(a)
                    sub = y - np.fft.fft(a)
                    for k in sub:
                        err = abs(k)
                        self.assertTrue(err < 0.0001*abs(y[1]))
                    
    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()
