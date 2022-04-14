# Code for simulating a turing machine.
import re

def read_tm_input(inputTape):

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
    code_raw = code_file.read()
    # This regex sub allows for comments in the code between angle brackets on a single line.
    code_raw = re.sub("\<.*?\>\n","",code_raw)
    code_raw = code_raw.split(";\n")[:-1]
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


#### ------------------------------------------------------------------
#### Code for writing the computations to a file in a readable manner
#### ------------------------------------------------------------------

def tape_top(tape):

    """


    """
    # How long is the tape?
    number_cells = len(tape)

    top = "|" + "|---"*number_cells + "|"

    return top

def tape_characters(tape):

    # How long is the tape?
    number_cells = len(tape)

    tape_output = "|"

    for character in tape:

        if character == "b":

            cell = "|" + " "*3
            tape_output += cell

        else:

            cell = "|" + " " + character + " "
            tape_output += cell



    return tape_output + "|"

def tm_read_head(tm_position,tm_state,tm_print,tm_move,tm_updateState):

    """

          | |       two spaces + | + space + | + two spaces
        /     \     / + three spaces + \
        |C: q0 |    |C: + space + tm_state + space + |
        |P: @  |    |P: + space + tm_print + space + |
        |M: R  |    |M: + space + tm_move + space + |
        |U: q0 |    |U: + space + tm_updateState + space + |
        --------

    """

    # This will determine how far along the head should read.
    shift = (tm_position)*4

    line_1 = " "*shift + " "*2 + "|" + " " + "|" + " "*2 + "\n"
    line_2 = " "*shift + " /   \\" + "\n"
    line_3 = " "*shift + "|C: " + tm_state + "|" + "\n"
    line_4 = " "*shift + "|P: " + tm_print + " |" + "\n"
    line_5 = " "*shift + "|M: " + tm_move + " |" + "\n"
    line_6 = " "*shift + "|U: " + tm_updateState + "|" + "\n"
    line_7 = " "*shift + "-"*7

    # Output string
    head_output = ""

    lines_head = [line_1,line_2,line_3,line_4,line_5,line_6,line_7]
    for line in lines_head:
        head_output += line

    return head_output


# Start the computations...
turingMachineInput = read_tm_input("tm-tape.txt")
turingMachineDictionary = tm_compile_dictionary("tm-code-unaryAddition.txt")
turingMachineOutput = open("tm-output.txt","w")
turingMachineOutput.close()

# NOTE!!! This should be refactored into a function/functions.
state = "q0"
head_read = "@"
head_position = 0

steps = 1

while (state != "HALT") and (steps < 1000) and len(turingMachineInput) < 100:

    # Retrieve the current instruction set.
    current_instructions = turingMachineDictionary[state][head_read]

    # Find the value to print to the tape.
    print_value = current_instructions[0]

    # Find the move direction and update the head position
    move_direction = current_instructions[1]

    # Find the state to update to.
    next_state = current_instructions[2]
    next_state_print = ""
    if next_state == "HALT":
        next_state_print = "H "
    else:
        next_state_print = next_state

    # Write the current state to file.
    tape_upper_lower = tape_top(turingMachineInput)
    tape_cells = tape_characters(turingMachineInput)
    tm_tape = tape_upper_lower + "\n" + tape_cells + "\n" + tape_upper_lower + "\n"

    head_instructions = tm_read_head(head_position,state,print_value,move_direction,next_state_print)


    turingMachineOutput = open("tm-output.txt","a")
    turingMachineOutput.write(tm_tape)
    turingMachineOutput.write(head_instructions)
    turingMachineOutput.write("\n")
    turingMachineOutput.close()



    # Update the state and tape according to the instructions.

    # Print the appropriate value to the tape.
    turingMachineInput[head_position] = print_value

    # Move the head of the Turing Machine.
    head_position += tm_move_instruction(move_direction)

    # Update the state according to the instructions.
    state = next_state

    # Update the value being read to the value in the new position
    head_read = turingMachineInput[head_position]

    # If the head gets within' 2 spaces of the end, then we append a blank cell. This Gives the Turing Machine it's potentially infinite tape.
    if (len(turingMachineInput) - head_position) <=2:
        turingMachineInput.append("b")

    # Print the number of steps
    steps += 1

print(steps)
turingMachineOutput = open("tm-output.txt","a")
turingMachineOutput.write("\n" + "HALT!")
turingMachineOutput.close()
