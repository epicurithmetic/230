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

        self.tape = []                      # Tape initially empty.
        self.mconfig = "q_1"                # Initial state always called q_1.
        self.head = 0                       # Head always starts at the left-most cell.
        self.alphabet = [" ", "0", "1"]     # Default alphabet for the machine.
        self.symbol = ""                    # This stores the cell last read by the machine head.
