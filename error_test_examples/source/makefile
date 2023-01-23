all: compile

compile: unicodeDecodeError.c SIGABRT.c SIGBUS.c SIGFPE.c SIGILL.c SIGSEGV.c loop.c
	gcc -Wall unicodeDecodeError.c -o unicodeDecodeError.out
	gcc -Wall SIGABRT.c -o SIGABRT.out
	gcc -Wall SIGBUS.c -o SIGBUS.out
	gcc -Wall SIGFPE.c -o SIGFPE.out
	gcc -Wall SIGILL.c -o SIGILL.out
	gcc -Wall SIGSEGV.c -o SIGSEGV.out
	gcc -Wall loop.c -o loop.out

run: compile
	./SIGSEGV.out

clean:
	rm *.out
