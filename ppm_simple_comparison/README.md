# ppm\_simple\_comparison
This autograder example contains a series of tests that compare the header and pixel contents of a PPM image against a reference/sample.

----

### Requirements:
* main.c

----

## Tests:
1. **Check that PPM header information is correct with width 15** (labeled test #3 on Gradescope) runs `make -s run` passing the contents of input/15.txt as stdin, then compares program output against an array of expected PPM header values.
2. **Check that PPM image is correct with width 15** (labeled test #4 on Gradescope) runs `make -s run` passing the contents of input/15.txt as stdin, then compares program output against the contents of reference/15.ppm.
3. **Check that PPM header information is correct with width 42** (labeled test #3 on Gradescope) runs `make -s run` passing the contents of input/42.txt as stdin, then compares program output against an array of expected PPM header values.
4. **Check that PPM image is correct with width 42** (labeled test #4 on Gradescope) runs `make -s run` passing the contents of input/42.txt as stdin, then compares program output against the contents of reference/42.ppm.