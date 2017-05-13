# AUTHOR Shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu

import unittest
import time
import sys


authors=['shs2016f@bu.edu', 'yhan94@bu.edu']

class PolynomialTestCase(unittest.TestCase):

    def setUp(self):
        pass

    #implement a constructor which takes a sequence and assigns the coefficients in the natural (descending order). So Polynomial([4,-9,5.6]) should make 4x2 − 9x + 5.6
    def test_assign(self):
        a = Polynomial([4, -9, 5.6])
        self.assertIsInstance(a,Polynomial)
        self.assertEqual(a,Polynomial([4, -9, 5.6]))
        self.assertEqual(a[2], 4)
        self.assertEqual(a[1], -9)
        self.assertEqual(a[0], 5.6)
        a[2] = 0
        self.assertEqual(a, Polynomial([-9, 5.6]))
        b = Polynomial()
        b[3] = 5
        b[-3] = 5
        c = Polynomial([5, 0, 0, 0])
        c[-3] = 5
        self.assertEqual(b, c)

    def test_getitem(self):
        a = Polynomial([4, -9, 5.6])
        self.assertEqual(a[100], 0)
        self.assertEqual(a[2], 4)

    #implement addition and subtraction of polynomials using + and -
    def test_add(self):
        a = Polynomial([4, -9, 5.6])
        b = Polynomial([3.2, 0, 0, 2, -5.6])
        self.assertEqual(a + b, Polynomial([3.2, 0, 4, -7, 0]))

    def test_sub(self):
        a = Polynomial([2,6,7,9])
        b = Polynomial([1,3,5,4])
        c = Polynomial()
        c[5] = 8
        d = Polynomial()
        d[2] = 7
        e = Polynomial()
        self.assertEqual(a - b , Polynomial([1,3,2,5]))
        self.assertEqual(a - c , Polynomial([-8,0,2,6,7,9]))
        self.assertEqual(a - d , Polynomial([2,-1,7,9]))
        self.assertEqual(b - Polynomial([1,3,5,4]), e)

    def test_neg_sub(self):
        a = Polynomial([4,-9,5.6])
        b = Polynomial([3.2,0,0,2,-5.6])
        a[-2] = 1
        b[-2] = 3.7
        c = Polynomial([-3.2,0,4,-11,11.2])
        c[-2] = -2.7
        self.assertEqual(a-b,c)

    #implement multiplication of polynomials using *
    def test_multi(self):
        a = Polynomial([1,3,5])
        b = Polynomial([1,0,0,2])
        self.assertEqual(a*b,Polynomial([1,3,5,2,6,10]))

    #implement testing for equality of polynomials using ==
    def test_eq(self):
        a = Polynomial([4, -9, 5.6])
        b = Polynomial([-9, 5.6])
        b[2] = 4
        self.assertTrue(a == b)

    def test_uneq(self):
        p1=Polynomial([1,1,1,2,3])
        p2=Polynomial([1,-1,2,3,4])
        p4=Polynomial([3,5,7])
        p3=p1+p2
        self.assertTrue(p3!=p4)
        self.assertTrue(p4!=p3)

    def test_eq_add(self):
        p0 = Polynomial([4, -9, 5.6])
        p1 = Polynomial([9, -5.6])
        p1[2] = -4
        p2=Polynomial([1,1,1,2,3])
        p3=Polynomial([-1,-1,-1,-2,-3])
        self.assertEqual(p0 + p1, p2 + p3)

    def test_eq_sub(self):
        a = Polynomial([1, 1, 2, 2])
        b = Polynomial([1, 0, 0])
        self.assertEqual(a - b, Polynomial([1, 0, 2, 2]))

    #implement an efficient mechanism for handling sparse polynomials
    def test_spares(self):
        a=Polynomial()
        a[0]=1
        a[100000]=12
        b=Polynomial([1,0,0,0,0,0,2])
        c=Polynomial()
        c[100006]=12
        c[100000]=24
        c[6] = 1
        b=Polynomial([1,0,2])
        c=Polynomial()
        c[100002]=12
        c[100000]=24
        c[2] = 1
        c[0] = 2
        self.assertEqual(a*b,c)

    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial()
        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10)

    #implement negative powers in the polynomial, i.e. you should be able to handle p(x)=x−1
    def test_nag_power(self):
        a = Polynomial()
        a[-4] = 9
        self.assertEqual(a[-4],9)

    #implement evaluation of the polynomial using a eval method, like this: p.eval(2.1)
    def test_eval(self):
        a = Polynomial([4, -9, 5.6])
        self.assertEqual(a.eval(-1), 18.6)
        
    #implement a derivative method p.deriv() which returns the derivative of the polynomial.
    def test_deriv(self):
        a = Polynomial([4, -9, 5.6])
        b = Polynomial([8, -9])
        self.assertEqual(a.deriv(), b)

    #implement accessing and modifying the coefficients using []. So p[2] should be the coefficient of x2 and p[8] = 12 should set the coefficent of x8 to 12.
    def test_modify(self):
        a = Polynomial([4, -9, 5.6])
        a[1] = 9
        self.assertEqual(a, Polynomial([4, 9, 5.6]))

    def tearDown(self):
        "tear down"

if __name__ == '__main__':
    unittest.main()
