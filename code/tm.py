# Code for simulating a turing machine.


# Read the input tape from file.
input_file = open("tm-tape-unaryAddition.txt","r")
input_raw = input_file.read()

# Remove the format from the file.
for character in [",",";","\n"," "]:
    input_raw = [x for x in input_raw if (x != character)]
input_file.close()

# Read the Turing machine code from file.
code_file = open("tm-code-unaryAddition.txt","r")
code_raw = code_file.read().split(";\n")[:-1]
# At this point code_raw is a list of states in "standard form"
code_file.close()
