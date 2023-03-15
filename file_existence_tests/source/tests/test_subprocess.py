import unittest
# timeout.py
import timeout
# Requires gradescope_utils
from gradescope_utils.autograder_utils.decorators import number, weight, visibility
import subprocess
from time import sleep
from re import sub
# utils.py
from utils import *
from pathlib import Path
import os

# Main unit test class
class TestDiff(unittest.TestCase):
    # Array of all the expected file names
    files = ['main.c']
    # Names of expected executables
    executables = ['main.out']
    
    # Set up unittest environment
    def setUp(self):
        self.maxDiff = None
        self.longMessage = False
        self.addTypeEqualityFunc(str, self.customCompare)
        
    # Define custom TypeEquality function that calls function from utils.py
    def customCompare(self, first, second, msg=None):
        customAssertMultiLineEqual(self, first, second, msg)

    # Associated test number within Gradescope
    @number("1")
    # Test visibility
    @visibility("visible")
    # Associated point value within Gradescope
    @weight(0)
    def test_checkFiles(self):
        """Ensure all required files are present"""
        
        checkFiles(self.files)
        sleep(1)
    
    # Associated test number within Gradescope
    @number("2")
    # Test visibility
    @visibility("visible")
    # Associated point value within Gradescope
    @weight(10)
    def test_Compile(self):
        # Title used by Gradescope 
        """Clean compile"""

        checkSourceFiles(self, self.files)

        # Create a subprocess to run the student's Makefile to ensure it compiles
        test = subprocess.Popen(["make"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        # Try to decode stderr
        try:
            stderr = stderr.strip().decode('utf-8')
            test.kill()
            
            self.assertTrue(stderr == "", msg=("See compiler output:\n" + stderr))
            
        # Catch exception for decode error
        except (UnicodeDecodeError):
            kill_fail(test, self, compileDecodeErrorMessage)
        
        test.terminate()

    # Associated test number within Gradescope
    @number("3")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(30)
    def test_FileExistsWithoutProgramRun(self):
        # Title used by Gradescope 
        """Check that "test1.txt" file exists"""
        
        file = "test1.txt"
        if Path(file).is_file():
            self.assertTrue(True)
        else:
            self.assertTrue(False, wrap("\"" + file + "\" does not exist.", 65))

    # Associated test number within Gradescope
    @number("4")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(30)
    def test_IsExecutable(self):
        # Title used by Gradescope 
        """Check that "main.out" executable exists"""
        
        file = "main.out"
        if Path(file).is_file():
            if os.access(Path(file), os.X_OK):
                self.assertTrue(True)
            else:
                self.assertTrue(False, wrap("\"" + file + "\" is not an executable.", 65))
        else:
            self.assertTrue(False, wrap("\"" + file + "\" does not exist.", 65))

    # Associated test number within Gradescope
    @number("5")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(30)
    def test_FileExistsWithProgramRun(self):
        # Title used by Gradescope 
        """Check that "test2.txt" file exists"""
        
        checkExecutables(self, self.executables)
        
        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./main.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            file = "test2.txt"
            if Path(file).is_file():
                self.assertTrue(True)
            else:
                self.assertTrue(False, wrap("\"" + file + "\" does not exist.", 65))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
