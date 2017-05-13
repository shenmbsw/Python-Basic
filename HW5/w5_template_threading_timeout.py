import unittest
import importlib
import glob
import json
import w5_testpoly
import io
import sys
import threading

def do_poly_test(loader,results,file_name):
    "run the tester on Polynomial class"
    module_tested = importlib.import_module(file_name[:-3])
    w5_testpoly.Polynomial = module_tested.Polynomial
    tests = loader.loadTestsFromTestCase(w5_testpoly.PolynomialTestCase)
    tests.run(results)


def check_all_files():
    passed,failed = [],[]
    Trials = glob.glob('poly*.py')
    for file_name in Trials:
        loader = unittest.loader.TestLoader()
        results = unittest.result.TestResult()
        try:
            s = io.StringIO()
            sys.stdout = s
            loader = unittest.loader.TestLoader()
            results = unittest.result.TestResult()
            T = threading.Thread(target=do_poly_test,args=(loader,results,file_name))
            T.start()
            T.join(0.04)
            if T.is_alive():
                raise TimeoutError()
            if results.wasSuccessful():
                passed.append(file_name)
            else:
                failed.append(file_name)   
            sys.stdout = sys.__stdout__
    
        except Exception as e:
            sys.stdout = sys.__stdout__
            print(e)
            failed.append(file_name)

    return passed,failed

if __name__ == "__main__":
    passed,failed = check_all_files()
    Results={'authors':w5_testpoly.authors,'failed':failed,'passed':passed}
    with open('week5_results.json','w') as f:
        json.dump(Results,f,indent=4)
