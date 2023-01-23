# input\_output\_comparison
This autograder example contains a series of tests that simulate program input (from stdin) and compare output (either stdout or stderr) against a reference/sample.

----

### Requirements:
* main.c

----

## Tests:
1. **Check that stdout output is correct without input** (labeled test #3 on Gradescope) runs `make -s noinput` (which passes a command-line argument to `main.out` indicating no input is required), then compares program output against [reference/noinput.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/noinput.txt).
2. **Check that input `1` results in correct stdout output** (labeled test #4 on Gradescope) runs `make -s run` passing the contents of [input/1.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/input/1.txt) as stdin, then compares program output against [reference/1.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/1.txt).
3. **Check that input `2` results in correct stdout output** (labeled test #5 on Gradescope) runs `make -s run` passing the contents of [input/2.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/input/2.txt) as stdin, then compares program output against [reference/2.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/2.txt).
4. **Check that input `3` results in correct stdout output** (labeled test #6 on Gradescope) runs `make -s run` passing the contents of [input/3.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/input/3.txt) as stdin, then compares program output against [reference/3.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/3.txt).
5. **Check that invalid input results in correct stderr output** (labeled test #7 on Gradescope) runs `make -s run` passing the contents of [input/invalid.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/input/invalid.txt) as stdin, then compares program output against [reference/invalid\_stderr.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/invalid_stderr.txt).
6. **Check that program outputs to both stdout and stderr** (labeled test #8 on Gradescope) runs `make -s run` passing the contents of [input/invalid.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/input/invalid.txt) as stdin, then determines whether to check against stdout or stderr. If only stderr is present, it will be compared against [reference/invalid\_stderr.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/invalid_stderr.txt); if stdout is present, it will be compared by default against [reference/invalid\_stdout.txt](https://github.com/sulliops/python-Gradescope-autograder/blob/main/input_output_comparison/source/reference/invalid_stdout.txt).
