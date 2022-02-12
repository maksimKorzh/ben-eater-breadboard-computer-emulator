####################################
#
#    Assembler for Ben Eater's
#      breadboard computer
#
####################################

# packages
import sys

# extract filenames
try:
    read_file = sys.argv[1]
    write_file = sys.argv[2]

except:
    print('Usage: python3 asm.py ./path/to/file.asm ./path/to/file.bin')
    sys.exit(1)


# instruction set
opcodes = {
    'NOP': 0x00,
    'LDA': 0x01,
    'ADD': 0x02,
    'SUB': 0x03,
    'STA': 0x04,
    'LDI': 0x05,
    'JMP': 0x06,
    'JC' : 0x07,
    'JZ' : 0x08,
    'OUT': 0x0E,
    'HLT': 0x0F,
    'DAT': 0x00
}

# binary program
program_bin = []

# open source code file
try:
    with open(read_file, 'r') as f:
        # loop over source lines
        for line in f.read().split('\n'):
            if line != '':
                # strip the comments
                instr = line.split(';')[0]
                
                # get instruction length
                instr_len = len(instr.split())
                
                # extract opcode
                opcode = opcodes[instr.split(' ')[0]] << 4
                if instr.split(' ')[0] == 'DAT': opcode >> 4

                # extract argument
                if instr_len == 2: argument = int(instr.split(' ')[1], 16)
                else: argument = 0
                
                # encode instruction
                program_byte = (opcode) | argument
                
                # append instruction to a binary program
                program_bin.append(program_byte)

except:
    print('ERROR: file', read_file, 'not found')
    sys.exit(1)

# write binary program to file
with open(write_file, 'wb') as f:
    f.write(bytes(program_bin))
    print([hex(i) for i in program_bin])
    print(len(program_bin), 'bytes written to', write_file)
    


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
