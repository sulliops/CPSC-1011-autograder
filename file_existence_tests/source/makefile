COMPILER = gcc
WARNING_OPTION = -Wall
OUTPUT_OPTION = -o
PROGRAM = test.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM)

$(PROGRAM): createFiles.c
	$(COMPILER) $(STD_OPTION) $(WARNING_OPTION) createFiles.c $(OUTPUT_OPTION) $(PROGRAM) 

clean:
	rm *.out
