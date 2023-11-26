import sys
import PDAReader
from HTMLreader import get_remainding_input

def Modify(Stack, Trans_Func):
    State = Trans_Func[3]
    if (Trans_Func[4] == []):
        NStack = Stack[1:]
    elif(Trans_Func[4][len(Trans_Func[4]) - 1] == '$'):
        tempstack = Trans_Func[4] + []
        if (tempstack[len(tempstack) - 1] == '$'): tempstack[len(tempstack) - 1] = Stack[0]
        NStack = tempstack + Stack[1:]
    else: NStack = Trans_Func[4] + Stack[1:]
    return State, NStack

#input
if (len(sys.argv) == 1):
    file_PDA = input()
    file_HTML = input()
elif (len(sys.argv) == 2):
    file_PDA = sys.argv[1]
    file_HTML = input()
else:
    file_PDA = sys.argv[1]
    file_HTML = sys.argv[2]

states_set, input_alphabet, stack_alphabet, state, stack, final_states, Transition_Functions = PDAReader.read_PDA(file_PDA)
remaining_input = get_remainding_input(file_HTML)

found = True
while (len(remaining_input) > 0):
    found = False
    for i in range(len(Transition_Functions)): # cari input
        if((Transition_Functions[i][0] == state) and ((Transition_Functions[i][1] == remaining_input[0]) or ((remaining_input[0] not in input_alphabet) and ( Transition_Functions[i][1] == '%'))) and ((Transition_Functions[i][2] == stack[0]) or (Transition_Functions[i][2] == '$'))):
            found = True
            state, stack = Modify(stack, Transition_Functions[i])
            print(stack, "  ", Transition_Functions[i] , "  ", remaining_input[0])
            remaining_input = remaining_input[1:]
            break
    if (not found): # cari input epsilon
        for i in range(len(Transition_Functions)):
            if((Transition_Functions[i][0] == state) and (Transition_Functions[i][1] == 'e') and ((Transition_Functions[i][2] == stack[0]) or (Transition_Functions[i][2] == '$'))):
                found = True
                state, stack = Modify(stack, Transition_Functions[i])
                break
    if (not found): break
if (not found): print("Syntax Error")
elif state in final_states:
    print("Accepted")
else:
    while(found):
        found = False
        for i in range(len(Transition_Functions)):
            if((Transition_Functions[i][0] == state) and (Transition_Functions[i][1] == 'e') and ((Transition_Functions[i][2] == stack[0]) or (Transition_Functions[i][2] == '$'))):
                found = True
                state, stack = Modify(stack, Transition_Functions[i])
                if state in final_states: found = False
                break
    if state in final_states: print("Accepted")
    else: print("Syntax Error")

# python3 main.py pda.txt