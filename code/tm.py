# Code for simulating a turing machine.




def read_TM_Input_Tape(inputTape):

    """
        This function reads a .txt file with a single line which should be of the following form:

            @,1,1,1,b,1,1;

        Which represents the input tape for the Turing Machine.

        Note: This function should have an optional input which can be used to pad the
              input tape with the desired number of blank cells to the right. This will allow
              the Machine to go past the inputs in its working - if that is needed.


        Output: List containing each cell on the tape as an entry. All strings.

    """

    # Read the input tape from file.
    input_file = open(inputTape,"r")
    input_raw = input_file.read()
    input_file.close()

    # Remove the format from the file.
    for character in [",",";","\n"," "]:
        input_raw = [x for x in input_raw if (x != character)]

    return input_raw

print(read_TM_Input_Tape("tm-tape-unaryAddition.txt"))


def read_TM_Code(turingMachine):

    """
        Input: turingMachine is assumed to be a .txt file with the following format

            q0,@,@,R,q1;
            q1,1,1,R,q1;
            q1,b,b,R,q2;
            ...

        Each of the lines corresponds to an instruction in standard form.

        Output: List of states in standard form. That is, a list of the lines in the
                turingMachine input .txt file. 

    """


    # Read the Turing machine code from file.
    code_file = open(turingMachine,"r")
    code_raw = code_file.read().split(";\n")[:-1]
    # At this point code_raw is a list of states in "standard form"
    code_file.close()

    return code_raw

<<<<<<< HEAD
test = turingMachine()

for i in range(0,3):

    print(test.tape)
    #test.print_tape()
    test.progress_TM()
    #test.print_tape()
print(test.mconfig)
=======
print(read_TM_Code("tm-code-unaryAddition.txt"))
>>>>>>> a11e377bcde20169df75e2226d695a547975bf4d
