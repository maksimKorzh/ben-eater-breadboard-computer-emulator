####################################
#
#    Disassembler for Ben Eater's
#        breadboard computer
#
####################################

# packages
import sys

# binary program
program_bin = []

# extract filename
try: filename = sys.argv[1]
except: print('Usage: python3 disasm.py ./path/to/file.bin'); sys.exit(1)

# instruction set
opcodes = [ 'NOP', 'LDA', 'ADD', 'SUB', 'STA', 'LDI', 'JMP', 'JC', 'JZ', '', '', '', '', '', 'OUT', 'HLT']

# instruction descriptions
description = [
    'No operation',
    'A register equals to the value at RAM[XXXX]',
    'A register equals A + B (which is the value at RAM[XXXX])',
    'A register equals A - B (which is the value at RAM[XXXX])',
    'Value at RAM[XXXX] equals to register A',
    'A register equals to the immediate value of XXXX',
    'sets program counter to XXXX and executes from there',
    'sets program counter to XXXX if carry flag is set',
    'sets program counter to XXXX if zero flag is set',
    '',
    '',
    '',
    '',
    '',
    'Output contents of A register',
    'Halts the execution'
]

# open binary file
with open(filename, 'rb') as f:
    program_bin = [int(i) for i in f.read()]

# loop over program bytes
for addr in range(len(program_bin)):      
    # extract opcode
    opcode = (program_bin[addr] & 0xF0) >> 4
    
    # extract argument
    argument = (program_bin[addr] & 0x0F)
    
    try:
        print(hex(addr) + ':    ', end='')
        if opcodes[opcode] == 'JC' or opcodes[opcode] == 'JZ': print(' ', end='')
        print(opcodes[opcode], hex(argument), '    ; ' + description[opcode].replace('XXXX', hex(argument)))
    except: print('ERROR: Unknown opcode', hex(opcode))






















