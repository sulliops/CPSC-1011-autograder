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

# Function that kills the process that runs the student's program,
# then fails the test with a pre-defined message
def kill_fail(proc, utest, msg):
    proc.kill()
    utest.longMessage = False
    utest.assertTrue(False, wrap(msg, 75))

# Series of exception classes that allow raising runtime exceptions
# All of these just call kill_fail function
class RuntimeAbort(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

class RuntimeSegFault(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

class RuntimeFPE(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

class RuntimeBusError(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

class RuntimeIllegalInstruction(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

class MakefileError(Exception):
    def __init__(self, proc, utest, msg):
        kill_fail(proc, utest, msg)

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
    @weight(5)
    def test_checkFiles(self):
        """Ensure all required files are present"""
        
        checkFiles(self.files)
        sleep(1)
    
    # Associated test number within Gradescope
    @number("2")
    # Associated point value within Gradescope
    @weight(10)
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
    @weight(10)
    def test_PPMWidth15Header(self):
        # Title used by Gradescope 
        """Check that PPM header information is correct with width 15"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/15.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                
                # Array of expected lines of output, line by line in expected order
                expected = ['P3', '15', '7', '255']
                
                # Split output by lines
                header = stdout.split()
                
                # Check if header information is correct
                try:
                    if header[0] != expected[0]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s header label is incorrect. Your header laber: {header[0]}, expected header label: {expected[0]}', 75))
                    elif header[1] != expected[1]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s width is incorrect. Your width: {header[1]}, expected width: {expected[1]}', 75))
                    elif header[2] != expected[2]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s height is incorrect. Your height: {header[2]}, expected height: {expected[2]}', 75))
                    elif header[3] != expected[3]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s maximum pixel value is incorrect. Your value: {header[3]}, expected value: {expected[3]}', 75))
                    else:
                        self.assertTrue(True, '')
                
                # Catch exception for array out of bounds
                except (IndexError):
                    self.longMessage = False
                    self.assertTrue(False, wrap('Your PPM image\'s header is too short, and cannot be used in autograder comparisons. Ensure your program prints the correct header information.', 75))
                
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
    @weight(32.5)
    def test_PPMWidth15Image(self):
        # Title used by Gradescope 
        """Check that PPM image is correct with width 15"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/15.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                reference = open('reference/15.ppm', 'rb').read().strip().decode('utf-8')
                
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
    @weight(10)
    def test_PPMWidth42Header(self):
        # Title used by Gradescope 
        """Check that PPM header information is correct with width 42"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/42.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                
                # Set msg to blank string, in case test passes
                msg = ''
                
                # Array of expected lines of output, line by line in expected order
                expected = ['P3', '42', '21', '255']
                
                # Split output by lines
                header = stdout.split()
                
                # Check if header information is correct
                try:
                    if header[0] != expected[0]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s header label is incorrect. Your header laber: {header[0]}, expected header label: {expected[0]}', 75))
                    elif header[1] != expected[1]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s width is incorrect. Your width: {header[1]}, expected width: {expected[1]}', 75))
                    elif header[2] != expected[2]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s height is incorrect. Your height: {header[2]}, expected height: {expected[2]}', 75))
                    elif header[3] != expected[3]:
                        self.longMessage = False
                        self.assertTrue(False, wrap(f'Your PPM image\'s maximum pixel value is incorrect. Your value: {header[3]}, expected value: {expected[3]}', 75))
                    else:
                        self.assertTrue(True, '')
                
                # Catch exception for array out of bounds
                except (IndexError):
                    self.longMessage = False
                    self.assertTrue(False, wrap('Your PPM image\'s header is too short, and cannot be used in autograder comparisons. Ensure your program prints the correct header information.', 75))
                
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
    @weight(32.5)
    def test_PPMWidth42Image(self):
        # Title used by Gradescope 
        """Check that PPM image is correct with width 42"""

        # Create a subprocess to run the students code to obtain an output
        cat = subprocess.Popen(["cat", "input/42.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                reference = open('reference/42.ppm', 'rb').read().strip().decode('utf-8')
                
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