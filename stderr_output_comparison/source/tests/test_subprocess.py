import unittest
from gradescope_utils.autograder_utils.decorators import number, weight
import subprocess

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    # Associated test number within Gradescope
    @number("0")
    # Associated point value within Gradescope
    @weight(10)
    def test_Compile(self):
        # Title used by Gradescope 
        """Clean Compile"""

        # Create a subprocess to run the students make file to ensure it compiles
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message
        self.assertTrue(output == "", msg=output)
        test.terminate()

    # Associated test number within Gradescope
    @number("1")
    # Associated point value within Gradescope
    @weight(20)
    def test_Stderr(self):
        # Title used by Gradescope 
        """Check that program prints correct output to stderr"""

        # Create a subprocess to run the students code to obtain an output
        test = subprocess.Popen(["./lab4.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Change output variable to read stderr instead of stdout
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()
        
        # Boolean to hold value for test pass/fail (updated procedurally)
        correct = True
        
        # Array of expected lines of output, line by line in expected order
        expected = ['This is printed to stderr.']
        
        # Create array of lines of submission output by splitting at new lines
        linesPrinted = output.split("\n")
        
        # Check for correct number of lines in output (to help narrow down test failures for students)
        if len(linesPrinted) < len(expected):
            # If too few lines, set test failure status and update message appropriately
            correct = False
            msg = ['Your program\'s output has fewer lines than expected. Check the lab instructions and try again.', f'Your output: {output}', f'Expected output: {expected}']
        elif len(linesPrinted) > len(expected):
            # If too many lines, set test failure status and update message appropriately
            correct = False
            msg = ['Your program\'s output has more lines than expected. Check the lab instructions and try again.', f'Your output: {output}', f'Expected output: {expected}']
        else:
            # If correct number of lines, check content of each line
            currentLine = 0
            for line in linesPrinted:
                # Compare each line of expected array to current line from output
                if expected[currentLine] not in line:
                    # When output does not match expected, set test failure status
                    correct = False
                currentLine += 1
            # Update message appropriately
            msg = ['Your program\'s output does not match the expected output. Check the lab instructions and try again.', f'Your output: {output}', f'Expected output: {expected}']
        
        # Pass test pass/fail status and message to test run output
        self.assertTrue(correct, msg)
        test.terminate()