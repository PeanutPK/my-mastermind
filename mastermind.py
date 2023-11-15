import random
import copy


def guessing(num):
    guess = []
    number = input(f"Guess {num} digits number 😎: ")
    while len(number) != num:
        print(f"Please enter a number {num} digits")
        number = input(f"Guess {num} digits number 😎: ")
    print(f"Your guess is {number}")
    for i in str(number):
        guess.append(int(i))
    return guess


class Setup:
    def __init__(self):
        """
        This game always allows duplicate.
        """
        self.__cnum = 1  # x color
        self.__rnum = 1  # y position
        self.__color_goal = []

    def new_game(self):
        """
        New game for users.
        :return:
        """
        self.set_num()
        option = ''
        while option != 'q':
            hint_count = 0
            start_game.goal()
            # Enable the line below to test with answer.
            # print(start_game.color_goal)
            tries = 1
            guess = guessing(self.rnum)
            while guess != self.color_goal:
                self.color_check(guess)
                print("Wrong!!! 😭 try again")
                if tries % 3 == 0:
                    hint_count = self.hint(hint_count)
                guess = guessing(self.rnum)
                tries += 1
            print(f"\nThe answer is {self.color_goal}")
            if tries > 1:
                print(f"You guessed it after {tries} tries. 🐵")
            else:
                print("You guessed it first tries!!! 🎉")
            print()
            print(f"You used {hint_count} hint/s to guess the answer.")
            option = str(input("Type 'q' to quit: "))
        print("See you again next time.")

    def set_num(self):
        self.__cnum = int(input("Select number of color between 1-8: "))
        self.__rnum = int(input("Select row number 4/6/8: "))
        while self.rnum not in [4, 6, 8] or 1 > self.cnum > 8:
            if 1 > self.cnum > 8:
                print("Please choose new color number")
                self.__cnum = int(
                    input("Select number of color between 1-8: "))
            if self.rnum not in [4, 6, 8]:
                print("Please choose new row number")
                self.__rnum = int(input("Select row number 4/6/8: "))
        print(f"Playing Mastermind with {self.cnum} colors "
              f"and {self.rnum} positions")
        return self.cnum, self.rnum

    @property
    def cnum(self):
        return self.__cnum

    @property
    def rnum(self):
        return self.__rnum

    @property
    def color_goal(self):
        return self.__color_goal

    def goal(self):
        self.__color_goal = []
        for i in range(self.__rnum):
            self.color_goal.append(random.randint(1, self.__cnum))
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

    def hint(self, num_hint):
        print(f"You have used hint {num_hint} times.")
        choice = str(input("Do you want a hint y/n? "))
        if choice == 'y':
            num_hint += 1
            print("The hint is : ", end='')
            for i in range(num_hint):
                print(self.color_goal[i], end='')
            print()
        print("Good luck.")
        return num_hint


start_game = Setup()
start_game.new_game()
