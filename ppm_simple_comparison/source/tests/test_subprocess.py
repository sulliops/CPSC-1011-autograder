import unittest
# Requires gradescope_utils
from gradescope_utils.autograder_utils.decorators import number, weight
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