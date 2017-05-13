# Test program for w8c_multiply and w8p_multiply
# EC602 
# Author: J Carruthers

import unittest
import subprocess
import time
import numpy
import os
uniform=numpy.random.uniform
randint=numpy.random.randint

# Setup data files for our tests.

FNames=['a55.txt','b55.txt','a23.txt','b32.txt','aCC.txt','bCC.txt','av.txt','bv.txt','avt.txt','bvt.txt']

for fname in FNames:
    try:
        os.chmod(fname,0o644)
    except:
        pass

A5=randint(-10,10,(5,5))
B5=randint(-10,10,(5,5))
C5=A5 @ B5
numpy.savetxt('a55.txt',A5,fmt="%d")
numpy.savetxt('b55.txt',B5,fmt="%d")

Av=uniform(-10,10,(1,10))
Bv=uniform(-10,10,(10,1))
numpy.savetxt('av.txt',Av,fmt="%5.2f")
numpy.savetxt('bv.txt',Bv,fmt="%5.2f")
Av=numpy.loadtxt('av.txt',dtype=float)
Bv=numpy.loadtxt('bv.txt',dtype=float)
Cv = Av @ Bv

Avt = randint(-10,10,(10,1))
Bvt = randint(-10,10,(1,10))
numpy.savetxt('avt.txt',Avt,fmt="%d")
numpy.savetxt('bvt.txt',Bvt,fmt="%d")
Cvt = Avt @ Bvt

A23=uniform(-10,10,(2,3))
B32=uniform(-10,10,(3,2))
numpy.savetxt('a23.txt',A23,fmt="%5.2f")
numpy.savetxt('b32.txt',B32,fmt="%5.2f")
A23=numpy.loadtxt('a23.txt',dtype=float)
B32=numpy.loadtxt('b32.txt',dtype=float)
C22 = A23 @ B32

AC=randint(-10,10,(200,200))
BC=randint(-10,10,(200,200))
CC=AC @ BC
numpy.savetxt('aCC.txt',AC,fmt="%d")
numpy.savetxt('bCC.txt',BC,fmt="%d")
TIMELIMIT=0.5

#protect these files
for fname in FNames:
    os.chmod(fname,0o400)

# Flag definitions
INVALIDARGS = 1
NOFILE = 2
BADVALUES = 3
NOOUTPUT = 4
UNKNOWN = 5

progname=os.getcwd() +"/w8p_multiply" # or w8c_multiply

TestCases={\
'invalid':"""{p} int
{p} int 5 1 2 3 a b {out} UNREADABLE
{p} int 5 2 a b {out} UNREADABLE
{p} double 0 0 0  a23.txt b32.txt {out}
{p} double -2 3 3  a23.txt b32.txt {out}
{p} integer 5 a55.txt b55.txt {out}
{p} Double 5 a55.txt b55.txt {out}
{p} int 5 1 2
""",
"nofile":"""{p} int 5 XYZ QWE {out}
{p} int 5 a55.txt QWE {out}
{p} int 5 XYZ b55.txt {out}
{p} int 5 UNREADABLE a55.txt {out}
""",
"unreadableinput":"""{p} int 5 UNREADABLE a55.txt {out}
""",
"badvalues":"""{p} int 2 3 2 a23.txt b32.txt {out}
{p} int 6 a55.txt b55.txt {out}
{p} double 4 a55.txt b55.txt {out}
{p} double 2 3 3  a23.txt b32.txt {out}
{p} double 3 3 2  a23.txt b32.txt {out}
""",
"nooutput":"""{p} double 2 3 2  a23.txt b32.txt UNREADABLE""",
}


os.system('chmod 600 UNREADABLE;cp a55.txt UNREADABLE;chmod 000 UNREADABLE')

def myremove(filename):
    try:
        os.remove(filename)
    except:
        pass

class multiplyTestCase(unittest.TestCase):
    def setUp(self):
        self.TestCases={x:TestCases[x].format(p=progname,out="{out}").splitlines() for x in TestCases}


    def test_invalid_command_line(self):
        for cmd in self.TestCases['invalid']:
            with self.subTest(CMD=cmd):
                outp = "invalid_test_{}".format(randint(1,2000))
                cmd=cmd.format(p=progname,out=outp) 
                T = subprocess.run(cmd.split())
                self.assertEqual(T.returncode,INVALIDARGS,msg="Wrong return code.")

    def test_no_input_files(self):
        for cmd in self.TestCases['nofile']:
            with self.subTest(CMD=cmd):
                outp = "noinput_test_{}".format(randint(1,2000))
                cmd=cmd.format(p=progname,out=outp)                
                T = subprocess.run(cmd.split())                
                self.assertEqual(T.returncode,NOFILE,msg="Wrong return code.")
                myremove(outp)

    def test_no_input_files(self):
        for cmd in self.TestCases['nofile']:
            with self.subTest(CMD=cmd):
                outp = "unreadable_{}".format(randint(1,2000))
                cmd=cmd.format(p=progname,out=outp)                
                T = subprocess.run(cmd.split())                
                self.assertTrue(T.returncode==NOFILE or T.returncode==BADVALUES,msg="Wrong return code.")
                myremove(outp)

    def test_bad_number_values(self):
        for cmd in self.TestCases['badvalues']:
            with self.subTest(CMD=cmd):
                outp = "badvalues_{}".format(randint(1,2000))
                cmd=cmd.format(p=progname,out=outp)
                T = subprocess.run(cmd.split())                
                self.assertEqual(T.returncode,BADVALUES,msg="Wrong return code.")
                myremove(outp)

    def test_no_output(self):
        for cmd in self.TestCases['nooutput']:
            with self.subTest(CMD=cmd):
                T = subprocess.run(cmd.split())
                self.assertEqual(T.returncode,NOOUTPUT,msg="Wrong return code.")

    def test_square_mode(self):
        "{p} int 5 a55.txt b55.txt {out}"
        cmd=self.shortDescription()
        outp = "square_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        T = subprocess.run(cmd.split())
        res = numpy.loadtxt(outp,dtype=int)
        myremove(outp)


        self.assertEqual(T.returncode,0,msg="Wrong return code.")
        self.assertTrue(numpy.array_equal(res,C5),msg="Incorrect multiply")


    def test_MNL_mode_5(self):
        "{p} int 5 5 5 a55.txt b55.txt {out}"
        cmd=self.shortDescription()
        outp = "mnl_555_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        T = subprocess.run(cmd.split())
        self.assertEqual(T.returncode,0,msg="Non-zero return code. Input was valid.")

        res = numpy.loadtxt(outp,dtype=int)
        myremove(outp)

        self.assertTrue(numpy.array_equal(res,C5),msg="Incorrect multiply")


    def test_MNL_mode_23(self):
        "{p} double 2 3 2 a23.txt b32.txt {out}"
        cmd=self.shortDescription()
        outp = "mnl_232_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        T = subprocess.run(cmd.split())
        self.assertEqual(T.returncode,0,msg="Non-zero return code. Input was valid.")

        res = numpy.loadtxt(outp,dtype=float)
        
        myremove(outp)        

        self.assertTrue(numpy.allclose(res,C22),msg="Incorrect multiply")

    def test_MNL_mode_vector(self):
        "{p} double 1 10 1 av.txt bv.txt {out}"
        cmd=self.shortDescription()
        outp = "mnl_vect_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        T = subprocess.run(cmd.split())
        self.assertEqual(T.returncode,0,msg="Non-zero return code. Input was valid.")

        res = numpy.loadtxt(outp,dtype=float,ndmin=2)
        myremove(outp)

        self.assertTrue(numpy.allclose(res,Cv),msg="Incorrect multiply")

    def test_MNL_mode_10(self):
        "{p} int 10 1 10 avt.txt bvt.txt {out}"
        cmd=self.shortDescription()
        outp = "mnl_vect_trans_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        T = subprocess.run(cmd.split())
        self.assertEqual(T.returncode,0,msg="Non-zero return code. Input was valid.")

        res = numpy.loadtxt(outp,dtype=int,ndmin=2)
        myremove(outp)

        self.assertTrue(numpy.array_equal(res,Cvt),msg="Incorrect multiply")




class efficient_multiplyTestCase(unittest.TestCase):
    def test_200_200(self):
        "{p} int 200 aCC.txt bCC.txt {out}"
        cmd=self.shortDescription()
        outp = "mnl_CC_test_{}".format(randint(1,2000))
        cmd=cmd.format(p=progname,out=outp)
        st = time.time()
        T = subprocess.run(cmd.split())
        self.assertEqual(T.returncode,0,msg="Non-zero return code. Input was valid.")
        en = time.time()
        res = numpy.loadtxt(outp,dtype=int)
        myremove(outp)

        self.assertTrue(numpy.array_equal(res,CC),msg="Incorrect multiply")
        self.assertLess(en-st,TIMELIMIT,msg="Too slow.")



    
if __name__ == '__main__':
    unittest.main()
