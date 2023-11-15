import random
import copy


def guessing(num):
    guess = []
    number = input(f"Guess {num} digits number 😎: ")
    while len(number) != num:
        print(f"Please enter a number {num} digits")
        number = input(f"Guess {num} digits number 😎: ")
    for i in str(number):
        guess.append(int(i))
    return guess


class Setup:
    def __init__(self):
        """
        This game always allows duplicate.
        """
        self.cnum = 1  # x color
        self.rnum = 1  # y position
        self.color_goal = []

    def new_game(self):
        """
        New game for users.
        :return:
        """
        self.set_num()
        option = ''
        while option != 'q':
            start_game.goal()
            print(start_game.color_goal)
            tries = 1
            guess = guessing(self.rnum)
            while guess != self.color_goal:
                self.color_check(guess)
                print("Wrong!!! 😭 try again")
                guess = guessing(self.rnum)
                tries += 1
            if tries > 1:
                print(f"You guessed it after {tries} tries. 🐵")
            else:
                print("You guessed it first tries!!! 🎉")
            option = str(input("Type 'q' to quit: "))

    def set_num(self):
        self.cnum = int(input("Select number of color between 1-8: "))
        self.rnum = int(input("Select row number 4/6/8: "))
        while self.rnum not in [4, 6, 8] or 1 > self.cnum > 8:
            if 1 > self.cnum > 8:
                print("Please choose new color number")
                self.cnum = int(input("Select number of color between 1-8: "))
            if self.rnum not in [4, 6, 8]:
                print("Please choose new row number")
                self.rnum = int(input("Select row number 4/6/8: "))
        print(f"You choose {self.cnum} for number of color and {self.rnum} "
              f"for number of row")
        return self.cnum, self.rnum

    def goal(self):
        self.color_goal = []
        for i in range(self.rnum):
            self.color_goal.append(random.randint(1, self.cnum))
        return self.color_goal

    def color_check(self, _input: list):
        correct = ''
        _input_copy = copy.deepcopy(_input)
        check = copy.deepcopy(self.color_goal)
        for i in range(len(_input)):
            if _input_copy[i] == check[i]:
                correct += '*'
                _input_copy[i] = -99
                check[i] = -99
        for i in _input_copy:
            if i != -99 and i in check:
                correct += 'o'
        print(correct)
        print()


start_game = Setup()
start_game.new_game()

