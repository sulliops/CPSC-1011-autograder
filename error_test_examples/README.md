# error\_test\_examples
This autograder example contains a series of tests that simulate test failure and error handling.

----

### Requirements:
* unicodeDecodeError.c
* input.c
* loop.c
* SIGABRT.c
* SIGBUS.c
* SIGFPE.c
* SIGILL.c
* SIGSEGV.c

----

## Tests:
1. **Demonstrate UnicodeDecodeError handling** (labeled test #3 on Gradescope) runs `./unicodeDecodeError input.c`, which triggers the `UnicodeDecodeError` exception handler.
2. **Demonstrate program timeout handling** (labeled test #4 on Gradescope) runs `./loop.out`, which triggers the `@timeout.timeout(seconds, exception_message)` decorator.
3. **Demonstrate SIGABRT handling** (labeled test #5 on Gradescope) runs `./SIGABRT.out`, which triggers the `RuntimeAbort` exception handler.
4. **Demonstrate SIGBUS handling** (labeled test #6 on Gradescope) runs `./SIGBUS.out`, which triggers the `RuntimeBusError` exception handler.
5. **Demonstrate SIGFPE handling** (labeled test #7 on Gradescope) runs `./SIGFPE.out`, which triggers the `RuntimeFPE` exception handler.
6. **Demonstrate SIGILL handling** (labeled test #8 on Gradescope) runs `./SIGILL.out`, which triggers the `RuntimeIllegalInstruction` exception handler.
7. **Demonstrate SIGSEGV handling** (labeled test #9 on Gradescope) runs `./SIGSEGV.out`, which triggers the `RuntimeSegFault` exception handler.
8. **Demonstrate Makefile error handling** (labeled test #10 on Gradescope) runs `make -s run`, which triggers the `MakefileError` exception handler.