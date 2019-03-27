def main():
    #Set up some initial values
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    #Play the game
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the pegs are moved!')

#The moveDiscs func displays a dics move in towers of hanoi game
#The parameters are:
#   num: number of disc to move
#   from_peg: the peg to move from
#   to peg: the peg to move to
#   temp_peg: the temporary peg
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num -1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

main()
