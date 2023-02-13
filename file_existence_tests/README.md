# file\_existence\_tests
This autograder example contains a series of tests that test whether files and/or executables exist.

These tests can also be adapted to test Makefile functionalities, such as the `make` or `make clean` targets.

----

### Requirements:
* createFiles.c

----

## Tests:
1. **Check that "test1.txt" file exists** (labeled test #3 on Gradescope) checks for the existence of a file called `test1.txt`, which is created by the program compiled into `test.out`. This test intentionally fails the first time it's tested (or after removal of the `test.txt` file) to demonstrate what happens when the file is not found.
2. **Check that "test.out" executable exists** (labeled test #4 on Gradescope) checks for the existence of a file called `test.out`, which is compiled from `checkFiles.c` (submission). The test makes sure the file exists, then checks to ensure it's an executable.
3. **Check that "test2.txt" file exists** (labeled test #5 on Gradescope) checks for the existence of a file called `test2.txt`, which is created by the program compiled into `test.out`. This test actually runs the submitted program, meaning the test should pass as long as `checkFiles.c` is configured to create the file `test2.txt`.