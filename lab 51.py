#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 27 2022
#loop 0-100 by 10 mips
ADDI $s0,$zero,0
ADDI $s1,$zero,10
ADDI $s2,$zero,100
AGAIN: ADD $s0,$s0,$s1
BEQ $s0,$s2,DONE
J AGAIN
DONE:
