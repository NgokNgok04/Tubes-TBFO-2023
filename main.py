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

PDA = PDAReader.read_PDA(file_PDA)

# python3 main.py pda.txt