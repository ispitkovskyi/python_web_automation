import unittest

from HTMLReport import TestRunner

suite = unittest.TestSuite()
class ExecuteTestSuite:
    testmodules = [
        'test.test_login',
        'test.new_test',
    ]

    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))


if __name__ == "__main__":
    test_runner = TestRunner(
        report_file_name="index",
        output_path="report",
        title="A simple test report",
        description="describe at will",
        sequential_execution=True,
        lang="en"
    )
    #Run tests via test_runner function to have report generated
    test_runner.run(suite)

    #If you run like below - there will be no HTML report
    #unittest.TextTestRunner().run(suite)