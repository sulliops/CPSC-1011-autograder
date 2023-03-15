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
    # Array of all the expected file names
    files = ['unicodeDecodeError.c', 'input.c', 'loop.c', 'SIGABRT.c', 'SIGBUS.c', 'SIGFPE.c', 'SIGILL.c', 'SIGSEGV.c']
    # Names of expected executables
    executables = ['unicodeDecodeError.out', 'loop.out', 'SIGABRT.out', 'SIGBUS.out', 'SIGFPE.out', 'SIGILL.out', 'SIGSEGV.out']
    
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
    @weight(11.25)
    def test_UnicodeDecodeError(self):
        # Title used by Gradescope 
        """Demonstrate UnicodeDecodeError handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./unicodeDecodeError.out input.c"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
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
    @weight(11.25)
    def test_Timeout(self):
        # Title used by Gradescope 
        """Demonstrate program timeout handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./loop.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
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
    @weight(11.25)
    def test_SIGABRT(self):
        # Title used by Gradescope 
        """Demonstrate SIGABRT handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./SIGABRT.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
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
    @weight(11.25)
    def test_SIGBUS(self):
        # Title used by Gradescope 
        """Demonstrate SIGBUS handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./SIGBUS.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
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
    @weight(11.25)
    def test_SIGFPE(self):
        # Title used by Gradescope 
        """Demonstrate SIGFPE handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./SIGFPE.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
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
    @weight(11.25)
    def test_SIGILL(self):
        # Title used by Gradescope 
        """Demonstrate SIGILL handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./SIGILL.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()

    # Associated test number within Gradescope
    @number("9")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(11.25)
    def test_SIGSEGV(self):
        # Title used by Gradescope 
        """Demonstrate SIGSEGV handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["./SIGSEGV.out"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()

    # Associated test number within Gradescope
    @number("10")
    # Test visibility
    @visibility("visible")
    # Individual test case timeout (in seconds)
    @timeout.timeout(10, exception_message=wrap(timeoutErrorMessage, 65), use_signals=False)
    # Associated point value within Gradescope
    @weight(11.25)
    def test_SIGSEGV(self):
        # Title used by Gradescope 
        """Demonstrate Makefile error handling"""
        
        checkExecutables(self, self.executables)

        # Create a subprocess to run the student's code to obtain an output
        test = subprocess.Popen(["make -s run"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = test.communicate()
        
        try:
            checkRuntimeErrors(test, self, stdout, stderr)
            
            # Try to decode stdout
            try:
                stdout = checkForUninitializedChars(stdout.strip().decode('utf-8'))
                test.kill()
                
                self.assertTrue(True, msg='Passed.')
            
            # Catch exception for decode error
            except (UnicodeDecodeError):
                kill_fail(test, self, decodeErrorMessage)
                
            # Catch exception for uninitialized characters
            except (UninitializedCharError):
                kill_fail(test, self, uninitializedCharacterMessage)
        
        # Catch runtime error exceptions
        except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
            pass
        
        test.terminate()
