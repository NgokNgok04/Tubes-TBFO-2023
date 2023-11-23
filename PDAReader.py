def split_komen(string):
    for i in range (len(string)):
        if (string[i] == '#'):
            string = string[:i]
            break
    return string

def read_PDA(PDA_Path):
    # input path ke file .txt
    states_set = []
    input_alphabet = []
    stack_alphabet = []
    Transition_Functions = []
    final_states = []
    with open(PDA_Path, 'r') as PDA_file:
        line = PDA_file.readline()
        phase = 0
        while (line != ""): # kosong artinya end of file
            if (line[0] == '#'): phase += 1
            line = split_komen(line).split()
            if (phase == 1): # baca transition function
                if (len(line) > 4):
                    Trans_Function = line[:4] + [line[4]]
                    Trans_Function[4] = Trans_Function[4].split('_')
                    if (Trans_Function[4] == ['e']):
                        Trans_Function[4] = []
                    Trans_Function = tuple(Trans_Function)
                    Transition_Functions.append(Trans_Function)
            elif (phase == 2): # baca input alphabet
                input_alphabet += line
            elif (phase == 3): # baca states
                states_set += line
            elif (phase == 4): # baca stack alphabet
                stack_alphabet += line
            elif (phase == 5): # baca start state
                if (len(line) > 0):
                    start_state = line[0]
            elif (phase == 6): # baca start stack
                if (len(line) > 0):
                    start_stack = line[0].split('_')
            else: # baca final states
                final_states += line
            line = PDA_file.readline()
    return states_set, input_alphabet, stack_alphabet, start_state, start_stack, final_states, Transition_Functions

"""Format PDA
##### State-Input-TOP-NextState-ContentStack ######
State Input TOP NextState ContentStack # ganti
State Input TOP NextState Content_Stack # push (dipisahkan dengan '_')
State Input TOP NextState e # pop

#####   Deskripsi input   #####
a
b
c

#####   Deskripsi state   #####
A
B
C

#### Deskripsi stack #####
X
Y
Z

##### Start State #####
A

##### Start Stack #####
Z

##### Final States #####
B
C

"""
