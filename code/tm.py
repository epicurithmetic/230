# Code for simulating a turing machine.

def read_tm_input_tape(inputTape):

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

def read_tm_code(turingMachine):

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

def tm_state_names(instructions):

    """
        This function takes in the list of instructions (already formatted from the
        text file into a list) for a Turing Machine and returns the set of state names.

    """

    state_names_set = set()

    for instruction in instructions:

        format_instructions = instruction.split(",")
        state_names_set.add(format_instructions[0])

    return state_names_set

def tm_compile_dictionary(turingMachineCode):

    """
        Input: Raw turingMachineCode .txt file.

        Output: Dictionary representation of machine code.


        Idea is that this dictionary is to be used as

        dict[state][read_value] = [print,move,new_state]


        So, this dictionary has each state name "qxyz" as a key. Each state has a dictionary
        whoses keys are the characters of the alphabet in use. For each character there is a
        list of instructions for the Turing Machine.

    """
    # This dictionary will have the state names as keys.
    tm_code_dictionary = {}

    # Read in the code from the file.
    raw_instructions = read_tm_code(turingMachineCode)

    # Collect the names of the states
    tm_states = tm_state_names(raw_instructions)

    for state in tm_states:

        # This dictionary will be the value of the output dictionary for the state key.
        # The keys for this dictionary are the read values of the head.
        # The values for this dictionary are lists of instructions [print,move,new_state].
        state_instruction_dictionary = {}

        for instruction in raw_instructions:

            format_instruction = instruction.split(",")

            if format_instruction[0] == state:

                state_instruction_dictionary[format_instruction[1]] = format_instruction[2:]

            else:
                pass

        tm_code_dictionary[state] = state_instruction_dictionary

    return tm_code_dictionary

def tm_move_instruction(direction):

    """
        This function maps the move instructions "L/R/N" to -1,1,0
        Outputs an INT.
    """

    if direction == "L":
        return -1
    elif direction == "R":
        return + 1
    else:
        return 0

# Start the computations...
turingMachineInput = read_tm_input_tape("tm-tape-unaryAddition.txt")
print(turingMachineInput)
turingMachineDictionary = tm_compile_dictionary("tm-code-unaryEqual.txt")


state = "q0"
head_read = "@"
head_position = 0

steps = 1

while state != "HALT":

    # Update the state until it gets to HALT

    # Retrieve the current instruction set.
    current_instructions = turingMachineDictionary[state][head_read]

    # Print the appropriate value to the tape.
    print_value = current_instructions[0]
    turingMachineInput[head_position] = print_value

    # Find the move direction and update the head position
    move_direction = current_instructions[1]
    head_position += tm_move_instruction(move_direction)

    # Update the state according to the instructions.
    state = current_instructions[2]

    # Update the value being read to the value in the new position
    head_read = turingMachineInput[head_position]

    print(turingMachineInput)
    # Print the number of steps
    steps += 1

print(steps)
