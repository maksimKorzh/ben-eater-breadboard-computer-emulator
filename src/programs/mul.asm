; perform a multiplication function by looping through the range
; defined by one of the factors (defined at address 13)
; and adding the second factor onto the product in each loop.
; the loop ends when the subtraction of the first factor by the 
; loop counter value reaches -1
start:
    LDA factor1
    SUB decrement  ; example of direct addressing working
    JC  end
    STA factor1
    LDA product
    ADD factor2
    STA product
    JMP start   ; example of direct addressing working.
end:
    LDA product
    OUT
    HLT
; these are in effect data labels.
product:
    0
factor1:
    7
factor2:
    6
decrement:
    1       ; loop counter value