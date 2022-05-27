#
# Write a warships game with field 5x5
import numpy as np
from random import randint

class Warships:
    
    def __init__(self, size_x: int, size_y: int) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.board = np.zeros((size_x, size_y), dtype=bool)
        self.ship = (randint(0, size_x), randint(0, size_y))

    def print_board(self):
        
        print('   ', end='')
        print(*list(range(len(self.board))))
        print('  ', end='')
        print('__'*len(self.board))
        
        for i, x in enumerate(self.board):
            print(f'{i} |', end='')
            for y in x:
                print('x' if y else 'o', end='')
                print(' ', end='')
            print('')
        print('')
        
def main():
    game = Warships(5,5)
    running = True
    
    while running:
        game.print_board()
        guess = tuple(map(int, input('What is your guess? \n').split()))
        while not (len(guess) == 2 and 
                   guess[0] in set(range(0, game.size_x)) and 
                   guess[1] in set(range(0, game.size_y))):
            guess = tuple(map(int, input('Incorrect input. What is your guess? \n').split()))

            

        if guess == game.ship:
            print('You won!')
            running = False
        else:
            game.board[guess[0]][guess[1]] = True
            print('Try again!\n')

if __name__ == '__main__':
    main()