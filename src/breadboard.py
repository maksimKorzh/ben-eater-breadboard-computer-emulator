######################################
#
#            Ben Eater's
#     8-bit breadboard computer
#             emulator
#
######################################

# 8-bit breadboard computer class
class BreadboardComputer:
    # init constructor
    def __init__(self):
        # call reset CPU
        self.reset()
    
    # load program to RAM
    def load(self):
        # load program into RAM
        self.RAM[0] = 0x54  # LDI 0x04
        self.RAM[1] = 0xe0  # OUT
        self.RAM[2] = 0xf0  # stop execution
        self.RAM[0x0E] = 0x00
        self.RAM[0x0F] = 0x00
    
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
    def run(self):
        try:
            # run program from RAM
            while not self.HALT:
                # init instruction register
                self.IR = self.RAM[self.PC]
                
                # execute current instruction
                self.execute()
                
                # increment program counter
                self.PC += 1
        except:
            pass

        print('All done!')

# create 8-bit breadboard computer instance
computer = BreadboardComputer()
computer.reset()
computer.load()
computer.run()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
