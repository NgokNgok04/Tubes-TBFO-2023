import sys
import PDAReader

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
remaining_input = [] # ganti dengan hasil parse HTML, misal ['a', 'b', 'dfvsdfvdfvadfv']

while (len(remaining_input) > 0):
    # proses
    break

# python3 main.py pda.txt