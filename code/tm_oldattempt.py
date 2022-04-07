# Turing Machine

# Idea is to define a class turingMachine() which can be initialized with: (i) alphabet (e.g. blank, 0,1,scwha) (ii) set
# of instructions m-configurations used to define what the machine does at each step (iii) the ability to input
# the tape on which the machine acts by reading and writing.

class turingMachine():

    """


        Each m-configurations is to be expressed in the notation of Turing's paper:

            e.g. [q_i, S_j, S_k, R/L, q_m]

        Which is to be read as: in state q_i, while reading symbol S_j,
        print S_k, move right/left and change the machine to state q_m.

    """

    def __init__(self):

        """

        """

        self.tape = ["0"]*10                # Tape initially empty.
        self.mconfig = "q_1"                # Initial state always called q_1.
        self.head = 0                       # Head always starts at the left-most cell.
        self.alphabet = ["b", "0", "1"]     # Default alphabet for the machine.
                                            # Note: "b" is BLANK.
        self.states = {}
        self.define_mconfigs()

    def define_mconfigs(self):

        """
            This method prompts the user to enter the m-configurations of the Turing Machine.
            This class assumes the user will adhere to Turing's notation as outlined
            in the doc-string for this class.

        """

        number_of_mconfigs = len(self.states)

        if number_of_mconfigs == 0:
            print("Define the m-configurations for when the Machine is in the initial state q1: ")

            # This will store all possible moves when in q_1.
            # Each of which depends only on the symbol read.
            m_configurations_all = []

            # By looping over each symbol, we can be sure to get every m-config required.
            for symbol in self.alphabet:
                S_j = symbol
                print(f"If the Turing Machine is in state q_1 and the head reads {S_j}")
                S_k = input("then the Turing Machine should print symbol [0,1,b] S_k = ")
                move_instruction = input("then move the head [L/R] = ")
                q_m = input("and finish in state: ")

                m_configurations_all.append([S_j,S_k,move_instruction,q_m])

            # Add this m-configuration to the dictionary.
            self.states["q_1"] = m_configurations_all

        else:

            updating_Turing_Machine = True
            while updating_Turing_Machine == True:

                print("Define an m-configuration of the Turing Machine: ")
                q_i = input("Initial state = ")

                # This will store all possible moves when in q_i.
                # Each of which depends only on the symbol read.
                m_configurations_all = []

                # By looping over each symbol, we can be sure to get every m-config required.
                for symbol in self.alphabet:
                    S_j = symbol
                    print(f"If the Turing Machine is in state {q_i} and the head reads {S_j}")
                    S_k = input("then the Turing Machine should print symbol [0,1,b] S_k = ")
                    move_instruction = input("then move the head [L/R] = ")
                    q_m = input("and finish in state: ")

                    m_configurations_all.append([S_j,S_k,move_instruction,q_m])

                # Add this m-configuration to the dictionary.
                self.states[q_i] = m_configurations_all


                print("|||" + "-"*10 + "|||")
                print(self.states)

                more_instructions = input("Would you like to add further m-configurations to the Machine? [Y/n]: ")

                if more_instructions == "n":
                    updating_Turing_Machine = False
                else:
                    pass

    def progress_TM(self):

        """
            This method performs the action of the current state:

                Updating the tape
                Moving the head
                Putting the machine in the next state

        """

        # This stores the value currently read by the head of the Machine.
        S_j = self.tape[self.head]

        # Given the current state and the value being read, we need to access the relevant
        # m-configuration so that the Turing Machine can update.
        update_rules = []
        if S_j == "b":
            update_rules = self.states[self.mconfig][0][1:]
        elif S_j == "0":
            update_rules = self.states[self.mconfig][1][1:]
        else:
            update_rules = self.states[self.mconfig][2][1:]

        # Print the new value on the tape:
        self.tape[self.head] = update_rules[0]

        # Move the head accordingly:
        if update_rules[1] == "R":
            self.head += 1
        else:
            self.head -= 1

        # Finally, the m-configuration should be updated:
        self.mconfig = update_rules[-1]

    def print_tape(self):

        """
            If the head is near the start of the tape, then this method prints the first
            five cells of the tape. Otherwise it prints the two cells either side of the
            current state.

        """

        i = self.head

        if i >= 2:

            print("="*30)
            print("| " + self.tape[i-2] + " |" + "| " + self.tape[i-1] + " |" + "| " + self.tape[i] + " |" + "| " + self.tape[i+1] + " |" + "| " + self.tape[i+2] + " |")
            print("="*30)

        elif i == 1:
            print("="*30)
            print("||||| " + self.tape[i-1] + " |" + "| " + self.tape[i] + " |" + "| " + self.tape[i+1] + " |" + "| " + self.tape[i+2] + " |" + "| " + self.tape[i+3] + " |")
            print("="*30)

        else:
            print("="*30)
            print("||||| " + self.tape[i-1] + " |" + "| " + self.tape[i] + " |" + "| " + self.tape[i+1] + " |" + "| " + self.tape[i+2] + " |" + "| " + self.tape[i+3] + " |")
            print("="*30)



test = turingMachine()
test.print_tape()
test.progress_TM()
test.print_tape()
print(test.mconfig)
