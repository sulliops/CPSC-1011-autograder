COMPILER = gcc
WARNING_OPTION = -Wall
OUTPUT_OPTION = -o
PROGRAM = lab2.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM)

$(PROGRAM): lab2.c
	$(COMPILER) $(STD_OPTION) $(WARNING_OPTION) lab2.c $(OUTPUT_OPTION) $(PROGRAM) 

clean:
	rm *.out
	rm *.c
