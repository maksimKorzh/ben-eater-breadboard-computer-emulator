start:
    LDI 0
printup:
    OUT
up:
    ADD increment
    JC down
    JMP printup
down:
    SUB increment
printdown:
    OUT
    JZ up
    JMP down
increment:
    3
