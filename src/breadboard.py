######################################
#
#            Ben Eater's
#     8-bit breadboard computer
#             emulator
#
######################################

# packages
import sys
import time

# 8-bit breadboard computer class
class BreadboardComputer:
    # init constructor
    def __init__(self):
        # call reset CPU
        self.reset()
    
    # load program to RAM
    def load(self, filename):
        if filename == '':
            print('No file specified, running triangular numbers program by default')
            print('Usage: python3 breadboard.py ./programs/fib.bin 0.05')
            
            # load program into RAM (prints triangular numbers)
            self.RAM[0x0] = 0x1F    # LDA 0x0F
            self.RAM[0x1] = 0x2E    # ADD 0x0E
            self.RAM[0x2] = 0x79    # JC  0x09
            self.RAM[0x3] = 0xE0    # OUT
            self.RAM[0x4] = 0x4F    # STA 0x0F
            self.RAM[0x5] = 0x1E    # LDA 0x0E
            self.RAM[0x6] = 0x2D    # ADD 0x0D
            self.RAM[0x7] = 0x4E    # STA 0x0E
            self.RAM[0x8] = 0x60    # JMP 0x00
            self.RAM[0x9] = 0x50    # LDI 0x00
            self.RAM[0xA] = 0x4F    # STA 0x0F
            self.RAM[0xB] = 0x1D    # LDA 0x0D
            self.RAM[0xC] = 0x4E    # STA 0x0E
            self.RAM[0xD] = 1       # DATA 1
            self.RAM[0xE] = 1       # DATA 1
            self.RAM[0xF] = 0       # DATA 0
        
        # read data from binary file
        else:
            try:
                with open(filename, 'rb') as f:
                    # read program bytes
                    program = [int(i) for i in f.read()]

                    # check program length
                    if len(program) > 16:
                        print('ERROR: Program length should be no more than 16 bytes')
                        sys.exit(1)
                    
                    # init RAM with program bytes
                    for i in range(len(program)): self.RAM[i] = program[i]
            
            except:
                print('File not found:', filename)
                sys.exit(1)

    # reset CPU
    def reset(self):
        # register A (8-bit)
        self.A = 0
        
        # register B (8-bit)
        self.B = 0
        
        # output register
        self.OUT = 0
        
        # instruction register (8-bit)
        self.IR = 0
        
        # program counter (4-bit)
        self.PC = 0
        
        # zero flag (1-bit)
        self.ZF = False
        
        # carry flag (1-bit)
        self.CF = False
        
        # halt flag
        self.HALT = False
        
        # RAM memory (16 bytes)
        self.RAM = [0] * 16
    
    # print debug info
    def debug(self):
        print('Register A:', hex(self.A))
        print('Register B:', hex(self.B))
        print('Register OUT:', hex(self.OUT))
        print('Register IR:', hex(self.IR))
        print('Register PC:', hex(self.PC))
        print('Register ZF:', bin(self.ZF))
        print('Register CF:', bin(self.CF))
        print('Register HALT:', bin(self.HALT))
        print('RAM:', [hex(i) for i in self.RAM])
    
    # execute opcode
    def execute(self):  
        # extract opcode IR FORMAT (opcode:argument)
        opcode = (self.IR & 0xF0) >> 4
        
        # extract argument
        argument = self.IR & 0x0F
        
        # handle opcodes
        if opcode == 0x00:
            # NOP instruction
            pass
        
        elif opcode == 0x01:
            # LDA instruction
            self.A = self.RAM[argument]
        
        elif opcode == 0x02:
            # ADD instruction
            self.B = self.RAM[argument]
            self.CF = (self.A + self.B) > 0xFF
            self.A = (self.A + self.B) & 0xFF
            self.ZF = self.A == 0

        elif opcode == 0x03:
            # SUB instruction
            self.B = self.RAM[argument]
            self.CF = (self.A - self.B) < 0x00
            self.A = (self.A - self.B) & 0xFF
            self.ZF = self.A == 0
        
        elif opcode == 0x04:
            # STA instruction
            self.RAM[argument] = self.A
        
        elif opcode == 0x05:
            # LDI instruction
            self.A = argument
        
        elif opcode == 0x06:
            # JMP instruction
            self.PC = argument - 1
        
        elif opcode == 0x07:
            # JC instruction
            if self.CF: self.PC = argument - 1
        
        elif opcode == 0x08:
            # ZF instruction
            if self.ZF: self.PC = argument - 1
        
        elif opcode == 0x0E:
            # OUT instruction
            self.OUT = self.A
            print('OUT:', self.OUT)
        
        elif opcode == 0x0F:
            # HLT instruction
            self.HALT = True
        
        #print('Opcode:', hex(opcode), ' Argument:', hex(argument), ' PC:', self.PC)
        #computer.debug()
        
    
    # main loop
    def run(self, filename, speed):
        # init CPU
        computer.reset()
        
        # load program
        computer.load(filename)
        
        # print extras
        if filename: print('Filename:', filename, end='')
        print (' running at', speed, 'ms')

        try:
            # run program from RAM
            while not self.HALT:
                # init instruction register
                self.IR = self.RAM[self.PC]
                
                # execute current instruction
                self.execute()
                
                # increment program counter
                self.PC += 1
                
                # clock delay
                time.sleep(float(speed))
        except:
            pass

        print('All done!')

# run only if invoked directly
if __name__ == '__main__':
    # create 8-bit breadboard computer instance
    computer = BreadboardComputer()

    # extract filename & speed from command line args
    try: filename = sys.argv[1]
    except: filename = ''
    try: speed = sys.argv[2]
    except: speed = '0.05'

    # run computer
    computer.run(filename, speed)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
