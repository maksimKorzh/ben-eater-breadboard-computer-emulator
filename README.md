# ben-eater-breadboard-computer-emulator
Ben Eater's 8-bit breadboard computer emulator

# YouTube tutorials
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/NiJ-_Xt9KRo/0.jpg)](https://www.youtube.com/watch?v=NiJ-_Xt9KRo&list=PLLfIBXQeu3ab2vTdu0aFoTUojsPWFSU3p)

# Instruction set
| Opcode | Mnemonic | Description
|--------|----------|------------
| 0000   | NOP      | No Operation
| 0001   | LDA      | Load contents of a memory address XXXX into A register
| 0010   | ADD      | Load contents of a memory address XXXX into B register, then performs A+B and stores the result in A register
| 0011   | SUB      | Load contents of a memory address XXXX into B register, then performs A-B and stores the result in A register
| 0100   | STA      | Store contents of A register at memory address XXXX
| 0101   | LDI      | Load 4 bit immediate value into A register
| 0110   | JMP      | Unconditional jump: sets program counter to XXXX and executes from there
| 0111   | JC       | Jump if carry: sets program counter to XXXX when carry flag is set and executes from there
| 1000   | JZ       | Jump if zero: sets program counter to XXXX when zero flag is set and executes from there
| 1110   | OUT      | Output contents of A register to 7 segment display, in our case, we'll print it on console
| 1111   | HLT      | Halts the execution
