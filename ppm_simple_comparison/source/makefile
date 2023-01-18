COMPILER = gcc
WARNING_OPTION = -Wall
OUTPUT_OPTION = -o
PROGRAM = main.out

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM)

$(PROGRAM): main.c
	$(COMPILER) $(STD_OPTION) $(WARNING_OPTION) main.c $(OUTPUT_OPTION) $(PROGRAM) 

clean:
	rm *.out
