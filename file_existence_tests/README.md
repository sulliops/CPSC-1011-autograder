# file\_existence\_tests
This autograder example contains a series of tests that test whether files and/or executables exist.

These tests can also be adapted to test Makefile functionalities, such as the `make` or `make clean` targets.

----

### Requirements:
* createFiles.c

----

## Tests:
1. **Check that "test1.txt" file exists** (labeled test #3 on Gradescope) checks for the existence of a file called `test1.txt`, which is created by the program compiled into `main.out`. This test intentionally fails the first time it's tested (or after removal of the `test1.txt` file) to demonstrate what happens when the file is not found.
2. **Check that "main.out" executable exists** (labeled test #4 on Gradescope) checks for the existence of a file called `main.out`, which is compiled from `main.c` (submission). The test makes sure the file exists, then checks to ensure it's an executable.
3. **Check that "test2.txt" file exists** (labeled test #5 on Gradescope) checks for the existence of a file called `test2.txt`, which is created by the program compiled into `main.out`. This test actually runs the submitted program, meaning the test should pass as long as `main.c` is configured to create the file `test2.txt`.

----

## Notes:
1. If any of these tests will be used to test a Makefile's `clean` target, wrap the existing test code in the following:

```
try:
    checkRuntimeErrors(test, self, stdout, stderr)
    
    // Test code
    
except (RuntimeAbort, RuntimeSegFault, RuntimeFPE, RuntimeBusError, RuntimeIllegalInstruction, MakefileError):
    pass
```