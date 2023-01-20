import unittest
# Requires gradescope_utils
from gradescope_utils.autograder_utils.decorators import number, weight
import subprocess
from time import sleep
from re import sub
# utils.py
from utils import *
import signal
import re
import textwrap

# Series of functions that handle extra lines when comparing output with 
# reference files
# Thanks Eliza Sorber
def nonEmptyLine(s):
    return len(s.strip()) != 0
    
def stripstr(s):
    return s.strip()

def removeEmptyLines(text):
    lst = filter(nonEmptyLine, list(map(stripstr, text.split("\n"))))
    return "\n".join(list(lst))

# Series of exception classes that allow raising runtime exceptions
# All of these kill the process that runs the student's program,
# then fails the test with a pre-defined message
class RuntimeAbort(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

class RuntimeSegFault(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

class RuntimeFPE(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

class RuntimeBusError(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

class RuntimeIllegalInstruction(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

class MakefileError(Exception):
    def __init__(self, proc, utest, msg):
        proc.kill()
        utest.longMessage = False
        utest.assertTrue(False, wrap(msg, 75))

# Function to check subprocess process for common runtime error signals
# Raises exceptions with custom messages for test failures
def checkRuntimeErrors(proc, utest, stdout, stderr):
    if ((proc.returncode % 128) == int(signal.SIGABRT)):
        raise RuntimeAbort(proc, utest, 'Your program triggered runtime error SIGABRT. Check for compilation warnings, use GDB to track down the cause of this error, or Google this error for more information.')
    elif ((proc.returncode % 128) == int(signal.SIGSEGV)):
        raise RuntimeSegFault(proc, utest, 'Your program encountered a segmentation fault. Check for compilation warnings, use GDB to track down the cause of this error, or Google this error for more information.')
    elif ((proc.returncode % 128) == int(signal.SIGFPE)):
        raise RuntimeFPE(proc, utest, 'Your program triggered runtime error SIGFPE (typically caused by dividing by zero). Check for compilation warnings, use GDB to track down the cause of this error, or Google this error for more information.')
    elif ((proc.returncode % 128) == int(signal.SIGBUS)):
        raise RuntimeBusError(proc, utest, 'Your program triggered runtime error SIGBUS. Check for compilation warnings, use GDB to track down the cause of this error, or Google this error for more information.')
    elif ((proc.returncode % 128) == int(signal.SIGILL)):
        raise RuntimeIllegalInstruction(proc, utest, 'Your program triggered runtime error SIGILL (typically caused by stack smashing). Check for compilation warnings, use GDB to track down the cause of this error, or Google this error for more information.')
    elif ((proc.returncode % 128) == int(signal.SIGINT)):
        raise MakefileError(proc, utest, (stderr.strip().decode('utf-8') + '\n' + stdout.strip().decode('utf-8')))

# Function to wrap strings for cleaner output in Gradescope
def wrap(string, width):
    return textwrap.fill(string, width)

# Main unit test class
class TestDiff(unittest.TestCase):
    # Set maxDiff to None to allow large diff checks
    maxDiff = None
    
    # Array of all the expected file names
    files = ['main.c']
    
    # This has to exist for some reason
    def setUp(self):
        pass

    # Associated test number within Gradescope
    @number("1")
    # Associated point value within Gradescope
    @weight(2.5)
    def test_checkFiles(self):
        """Ensure all required files are present"""
        
        checkFiles(self.files)
        sleep(1)
    
    # Associated test number within Gradescope
    @number("2")
    # Associated point value within Gradescope
    @weight(7.5)
    def test_Compile(self):
        # Title used by Gradescope 
        """Clean compile"""

        # Create a subprocess to run the students make file to ensure it compiles
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message
        self.longMessage = False
        self.assertTrue(output == "", msg=output)
        test.terminate()

    # Associated test number within Gradescope
    @number("3")
    # Associated point value within Gradescope
    @weight(15)
    def test_Stdout(self):
        # Title used by Gradescope 
        """Check that stdout output is correct without input"""

        # Create a subprocess to run the students code to obtain an output
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
                self.assertEqual(stdout, reference, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()

    # Associated test number within Gradescope
    @number("4")
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput1(self):
        # Title used by Gradescope 
        """Check that input "1" results in correct stdout output"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/1.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["make -s run"], shell=True, stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cat.kill()
        cat.terminate()
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
                self.assertEqual(stdout, reference, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("5")
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput2(self):
        # Title used by Gradescope 
        """Check that input "2" results in correct stdout output"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/2.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["make -s run"], shell=True, stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cat.kill()
        cat.terminate()
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
                self.assertEqual(stdout, reference, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("6")
    # Associated point value within Gradescope
    @weight(15)
    def test_StdoutInput3(self):
        # Title used by Gradescope 
        """Check that input "3" results in correct stdout output"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/3.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["make -s run"], shell=True, stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cat.kill()
        cat.terminate()
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
                self.assertEqual(stdout, reference, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("7")
    # Associated point value within Gradescope
    @weight(15)
    def test_StderrInvalidInput(self):
        # Title used by Gradescope 
        """Check that invalid input results in correct stderr output"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/invalid.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["make -s run"], shell=True, stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cat.kill()
        cat.terminate()
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
                self.assertEqual(stderr, reference, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
    
    # Associated test number within Gradescope
    @number("8")
    # Associated point value within Gradescope
    @weight(15)
    def test_MixedStdoutStderrOutput(self):
        # Title used by Gradescope 
        """Check that program outputs to both stdout and stderr"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/invalid.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        test = subprocess.Popen(["make -s run"], shell=True, stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cat.kill()
        cat.terminate()
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
                    self.assertEqual(stderr, reference_stderr, msg='Program output does not match expected output.')
                # If stderr is not usable for comparison, test with stdout
                else:
                    # Check that stdout and reference are equal
                    self.assertEqual(stdout, reference_stdout, msg='Program output does not match expected output.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                test.kill()
                self.longMessage = False
                self.assertTrue(False, wrap('Your program printed a character that the autograder cannot decode. Ensure your program prints valid characters.', 75))
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()