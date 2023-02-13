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

# Main unit test class
class TestDiff(unittest.TestCase):
    # Set maxDiff to None to allow large diff checks
    maxDiff = None
    
    # Array of all the expected file names
    files = ['main.c']
    
    # Set up unittest environment
    def setUp(self):
        self.addTypeEqualityFunc(str, self.customCompare)
        
    # Define custom TypeEquality function that calls function from utils.py
    def customCompare(self, first, second, msg=None):
        customAssertMultiLineEqual(self, first, second, msg)

    # Associated test number within Gradescope
    @number("1")
    # Test visibility
    @visibility("visible")
    # Associated point value within Gradescope
    @weight(2.5)
    def test_checkFiles(self):
        """Ensure all required files are present"""
        
        checkFiles(self.files)
        sleep(1)
    
    # Associated test number within Gradescope
    @number("2")
    # Test visibility
    @visibility("visible")
    # Associated point value within Gradescope
    @weight(7.5)
    def test_Compile(self):
        # Title used by Gradescope 
        """Clean compile"""

        # Create a subprocess to run the student's Makefile to ensure it compiles
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        # Try to decode stderr
        try:
            stderr = stderr.strip().decode('utf-8')
            test.kill()
            
            self.assertTrue(stderr == "", msg=stderr)
            
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
    @weight(15)
    def test_Stdout(self):
        # Title used by Gradescope 
        """Check that stdout output is correct without input"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s noinput"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = stdout.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference = open('reference/noinput.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stdout = removeEmptyLines(stdout)
                reference = removeEmptyLines(reference)
                
                # Check the contents of stdout against reference
                self.customCompare(stdout, reference, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()

    # Associated test number within Gradescope
    @number("4")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput1(self):
        # Title used by Gradescope 
        """Check that input "1" results in correct stdout output"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run < input/1.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = stdout.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference = open('reference/1.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stdout = removeEmptyLines(stdout)
                reference = removeEmptyLines(reference)
                
                # Check the contents of stdout against reference
                self.customCompare(stdout, reference, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("5")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput2(self):
        # Title used by Gradescope 
        """Check that input "2" results in correct stdout output"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run < input/2.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = stdout.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference = open('reference/2.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stdout = removeEmptyLines(stdout)
                reference = removeEmptyLines(reference)
                
                # Check the contents of stdout against reference
                self.customCompare(stdout, reference, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("6")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput3(self):
        # Title used by Gradescope 
        """Check that input "3" results in correct stdout output"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run < input/3.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = stdout.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference = open('reference/3.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stdout = removeEmptyLines(stdout)
                reference = removeEmptyLines(reference)
                
                # Check the contents of stdout against reference
                self.customCompare(stdout, reference, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("7")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(15)
    def test_StderrInvalidInput(self):
        # Title used by Gradescope 
        """Check that invalid input results in correct stderr output"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run < input/invalid.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stderr
            try:
                stderr = stderr.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference = open('reference/invalid_stderr.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stderr = removeEmptyLines(stderr)
                reference = removeEmptyLines(reference)
                
                # Check the contents of stdout against reference
                self.customCompare(stdout, reference, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("8")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(15)
    def test_MixedStdoutStderrOutput(self):
        # Title used by Gradescope 
        """Check that program outputs to both stdout and stderr"""

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run < input/invalid.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout and stderr
            try:
                stdout = stdout.strip().decode('utf-8')
                stderr = stderr.strip().decode('utf-8')
                test.kill()
                
                # Open reference output and decode
                reference_stdout = open('reference/invalid_stdout.txt', 'rb').read().strip().decode('utf-8')
                reference_stderr = open('reference/invalid_stderr.txt', 'rb').read().strip().decode('utf-8')
                
                # Remove empty lines from both output and reference
                stdout = removeEmptyLines(stdout)
                stderr = removeEmptyLines(stderr)
                reference_stdout = removeEmptyLines(reference_stdout)
                reference_stderr = removeEmptyLines(reference_stderr)
                
                # Check if stdout is empty but stderr has content
                if not stdout and stderr:
                    # Check that stderr and reference are equal
                    self.customCompare(stderr, reference_stderr, msg='Program output does not match expected output')
                # If stderr is not usable for comparison, test with stdout
                else:
                    # Check that stdout and reference are equal
                    self.customCompare(stdout, reference_stdout, msg='Program output does not match expected output')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()