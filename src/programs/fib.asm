start:
    LDI 1
    STA 14
    LDI 0
loop:
    STA 15
    OUT
    LDA 14
    ADD 15
    STA 14
    OUT
    LDA 15
    ADD 14
    JC end
    JMP loop
end:
    HLT
    0
    1