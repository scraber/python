from random import choice
import json
import input_params

import answer
import colors


class Mastermind:

    def __init__(self, filename: str, mode: str):
        self.length = int()
        self.chars = tuple()
        self.tries = int()
        self.passphrase = tuple()
        self.answer = tuple()
        self.game_finished = False
        self.file = open(filename + ".txt", "w+")
        self.mode = mode
        self.json_params = dict()

    def parameters_prompt(self):
        """Input prompt for game parameters"""
        self.length = input_params.length()
        self.chars = input_params.chars()
        self.tries = input_params.attempts()
        self.json_params = {"length": self.length, "chars": self.chars, "tries": self.tries, "rounds": []}


    def prepare_passphrase(self):
        """Randomly picks elements from available characters to create passphrase"""
        randomized = list()
        for i in range(self.length):
            randomized.extend(choice(self.chars))
        self.passphrase = tuple(randomized)

    def tries_available(self):
        return True if 0 < self.tries else False

    def write_answer_to_file(self):
        """Writes answer to text file"""
        # for elem in self.answer:
        #     self.file.write("{} ".format(elem))
        # self.file.write('\n')
        self.json_params["rounds"].append(list(self.answer))

    def input_validate(self):
        """Gets input and validate the correctness"""
        self.answer = tuple(input("Password length is {}: \n".format(self.length)))
        self.write_answer_to_file()
        if self.length != (len(self.answer)):
            raise ValueError
        if False is all(i in self.chars for i in self.answer):
            raise TypeError

    def correct_answer(self):
        """Method finishing game and printing answer"""
        print("You've won!", end='\n')
        self.game_finished = True
        for elem in self.answer:
            colors.print_green(elem)
        print("\n")

    def mark_characters(self):
        """Method coloring each element of answer depending if it matches with passphrase"""
        for index, elem in enumerate(self.answer):
            if True is answer.correct_char_correct_pos(elem, index, self.passphrase):
                colors.print_green(elem)
            elif True is answer.correct_char_wrong_pos(elem, self.passphrase):
                colors.print_yellow(elem)
            else:
                colors.print_red(elem)

    def dec_tries(self):
        """Method decreasing and printing available attempts"""
        self.tries -= 1
        print('\n {} attempts left \n'.format(self.tries))

    def check_input(self):
        """Method comparing answer with passphrase"""
        if self.answer == self.passphrase:
            self.correct_answer()

        else:
            self.mark_characters()
            self.dec_tries()

    def single_sequence(self):
        """Single game sequence, give input and check it's correctness"""
        if True is self.tries_available():
            try:
                self.input_validate()
            except ValueError:
                print("Invalid input length, expected {} characters, passed {}".format(self.length, len(self.answer), ))
                self.dec_tries()
                self.single_sequence()
            except TypeError:
                print("Invalid input arguments, available chars are {}".format(self.chars))
                self.dec_tries()
                self.single_sequence()
            else:
                self.check_input()

    def play(self):
        """Main game loop, work until game is finished or run out of tries"""
        self.parameters_prompt()
        self.prepare_passphrase()
        # print(self.passphrase)
        while False is self.game_finished and True is self.tries_available():
            self.single_sequence()
        else:
            json.dump(self.json_params, self.file, sort_keys=True, indent=4)
            if False is self.tries_available():
                print("You lost, password was {}".format(self.passphrase))
            if True is self.retry():
                self.play()

    def retry(self):
        """Input prompt for retrying game"""
        retry = input("Wanna play again? [yes/no]: ")
        if "yes" == retry:
            self.game_finished = False
            return True
        elif "no" == retry:
            return False
        else:
            print("Unknown command")
            return self.retry()
