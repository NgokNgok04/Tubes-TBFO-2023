import sys
import PDAReader
from HTMLreader import get_remainding_input

# 
def displayRes(result): 
    if result:
        print()
        print("\033[92m      .o.                                                    .                   .o8  \033[0m")
        print("\033[92m     .888.                                                 .o8                  \"888  \033[0m")
        print("\033[92m    .8\"888.      .ooooo.   .ooooo.   .ooooo.  oo.ooooo.  .o888oo  .ooooo.   .oooo888  \033[0m")
        print("\033[92m   .8' `888.    d88' `\"Y8 d88' `\"Y8 d88' `88b  888' `88b   888   d88' `88b d88' `888  \033[0m")
        print("\033[92m  .88ooo8888.   888       888       888ooo888  888   888   888   888ooo888 888   888  \033[0m")
        print("\033[92m .8'     `888.  888   .o8 888   .o8 888    .o  888   888   888 . 888    .o 888   888  \033[0m")
        print("\033[92mo88o     o8888o `Y8bod8P' `Y8bod8P' `Y8bod8P'  888bod8P'   \"888\" `Y8bod8P' `Y8bod88P\" \033[0m")
        print("\033[92m                                               888                                    \033[0m")
        print("\033[92m                                              o888o                                   \033[0m")
                                                                                      
    else:
        print()
        print("\033[91m .oooooo..o                             .                             oooooooooooo                                      \033[0m")
        print("\033[91md8P'    `Y8                           .o8                             `888'     `8                                      \033[0m")
        print("\033[91mY88bo.      oooo    ooo ooo. .oo.   .o888oo  .oooo.   oooo    ooo      888         oooo d8b oooo d8b  .ooooo.  oooo d8b \033[0m")
        print("\033[91m `\"Y8888o.   `88.  .8'  `888P\"Y88b    888   `P  )88b   `88b..8P'       888oooo8    `888\"\"8P `888\"\"8P d88' `88b `888\"\"8P \033[0m")
        print("\033[91m     `\"Y88b   `88..8'    888   888    888    .oP\"888     Y888'         888    \"     888      888     888   888  888     \033[0m")
        print("\033[91moo     .d8P    `888'     888   888    888 . d8(  888   .o8\"'88b        888       o  888      888     888   888  888     \033[0m")
        print("\033[91m8\"\"88888P'      .8'     o888o o888o   \"888\" `Y888\"\"8o o88'   888o     o888ooooood8 d888b    d888b    `Y8bod8P' d888b    \033[0m")
        print("\033[91m            .o..P'                                                                                                      \033[0m")
        print("\033[91m            `Y8P'                                                                                                       \033[0m")

# Ubah state dan stack sesuai fungsi transisi
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
            remaining_input = remaining_input[1:]
            break
    if (not found): # cari input epsilon
        for i in range(len(Transition_Functions)):
            if((Transition_Functions[i][0] == state) and (Transition_Functions[i][1] == 'e') and ((Transition_Functions[i][2] == stack[0]) or (Transition_Functions[i][2] == '$'))):
                found = True
                state, stack = Modify(stack, Transition_Functions[i])
                break
    if (not found): break
if (not found):
    displayRes(False)
elif state in final_states:
    displayRes(True)
else:
    while(found):
        found = False
        for i in range(len(Transition_Functions)):
            if((Transition_Functions[i][0] == state) and (Transition_Functions[i][1] == 'e') and ((Transition_Functions[i][2] == stack[0]) or (Transition_Functions[i][2] == '$'))):
                found = True
                state, stack = Modify(stack, Transition_Functions[i])
                if state in final_states: found = False
                break
    if state in final_states: 
        displayRes(True)
    else: 
        displayRes(False)

# python3 main.py pda.txt htmlPath.html