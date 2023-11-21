def split_komen(string):
    for i in range (len(string)):
        if (string[i] == '#'):
            string = string[:i]
            break
    return string

def read_PDA(PDA_Path):
    # input path ke file .txt
    with open(PDA_Path, 'r') as PDA_file:
        states_set = split_komen(PDA_file.readline()).split()       # array of states
        input_alphabet = split_komen(PDA_file.readline()).split()   # array of alphabets
        stack_alphabet = split_komen(PDA_file.readline()).split()   # array of stack symbols
        start_state = split_komen(PDA_file.readline()).split()[0]   # start state string
        start_stack = split_komen(PDA_file.readline()).split()[0]   # start stack string
        final_states = split_komen(PDA_file.readline()).split()     # array of final states
        isEmptyStack = split_komen(PDA_file.readline()).split()[0]  # Kalau 'E' juga accepts kalau empty stack
        Transition_Functions = []
        line = PDA_file.readline()
        while (line != ""): # kosong artinya end of file
            line = split_komen(line).split()
            Trans_Function = line[:4] + [line[4]]
            Trans_Function[4] = Trans_Function[4].split('_')
            if (Trans_Function[4] == ['e']):
                Trans_Function[4] = []
            Trans_Function = tuple(Trans_Function)
            Transition_Functions.append(Trans_Function)
            line = PDA_file.readline()
    return states_set, input_alphabet, stack_alphabet, start_state, start_stack, final_states, isEmptyStack, Transition_Functions