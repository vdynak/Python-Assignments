#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 27 2022
#I use MIPS!

ADDI $sp, $sp, -12
ADDI $t0, $zero,73 #i
SB $t0, 0($sp)
ADDI $t0, $zero,32 #space
SB $t0, 1($sp)
ADDI $t0, $zero,117 #u
SB $t0, 2($sp)
ADDI $t0, $zero,115 #s
SB $t0, 3($sp)
ADDI $t0, $zero,101 #e
SB $t0, 4($sp)
ADDI $t0, $zero,32 #space
SB $t0, 5($sp)
ADDI $t0, $zero,77 #M
SB $t0, 6($sp)
ADDI $t0, $zero,73 #I
SB $t0, 7($sp)
ADDI $t0, $zero,80 #P
SB $t0, 8($sp)
ADDI $t0, $zero,83 #S
SB $t0, 9($sp)
ADDI $t0, $zero,33 #!
SB $t0, 10($sp)
ADDI $t0, $zero,0 #null
SB $t0, 11($sp)

ADDI $v0, $zero, 4 #print
ADDI $a0, $sp, 0
syscall
