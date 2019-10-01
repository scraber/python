from random import choice
import input_params

import answer
import colors


class Mastermind:

    def __init__(self):
        self.length = int()
        self.chars = tuple()
        self.tries = int()
        self.passphrase = tuple()
        self.answer = tuple()
        self.game_finished = False

    def parameters_prompt(self):
        self.length = input_params.length()
        self.chars = input_params.chars()
        self.tries = input_params.attempts()

    def prepare_passphrase(self):
        randomized = list()
        for i in range(self.length):
            randomized.extend(choice(self.chars))
        self.passphrase = tuple(randomized)

    def tries_available(self):
        return True if 0 < self.tries else False

    def input_validate(self):
        self.answer = tuple(input("Password length is {}: \n".format(self.length)))
        if self.length != (len(self.answer)):
            raise ValueError
        if False is all(i in self.chars for i in self.answer):
            raise TypeError

    def correct_answer(self):
        print("You've won!", end='\n')
        self.game_finished = True
        for elem in self.answer:
            colors.print_green(elem)
        print("\n")

    def mark_characters(self):
        for index, elem in enumerate(self.answer):
            if True is answer.correct_char_correct_pos(elem, index, self.passphrase):
                colors.print_green(elem)
            elif True is answer.correct_char_wrong_pos(elem, self.passphrase):
                colors.print_yellow(elem)
            else:
                colors.print_red(elem)

    def check_input(self):
        if self.answer == self.passphrase:
            self.correct_answer()

        else:
            self.mark_characters()
            self.tries -= 1
            print('\n {} atempts left \n'.format(self.tries))

    def single_sequence(self):
        try:
            self.input_validate()
        except ValueError:
            print("Invalid input length, expected {} characters, passed {}".format(self.length, len(self.answer), ))
            self.single_sequence()
        except TypeError:
            print("Invalid input arguments, available chars are {}".format(self.chars))
            self.single_sequence()
        else:
            self.check_input()

    def play(self):
        self.parameters_prompt()
        self.prepare_passphrase()
        # print(self.passphrase)
        while False is self.game_finished and True is self.tries_available():
            self.single_sequence()
        else:
            if False is self.tries_available():
                print("You lost, password was {}".format(self.passphrase))
            if True is self.retry():
                self.play()

    def retry(self):
        retry = input("Wanna play again? [yes/no]: ")
        if "yes" == retry:
            self.game_finished = False
            return True
        elif "no" == retry:
            return False
        else:
            print("Unknown command")
            return self.retry()
