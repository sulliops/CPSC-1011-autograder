COMPILER = gcc
WARNING_OPTION = -Wall
OUTPUT_OPTION = -o
PROGRAM = lab4.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM)

$(PROGRAM): lab4.c
	$(COMPILER) $(STD_OPTION) $(WARNING_OPTION) lab4.c -lm $(OUTPUT_OPTION) $(PROGRAM) 

clean:
	rm *.out
	rm *.c
