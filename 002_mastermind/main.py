import argparse
from game import Mastermind

parser = argparse.ArgumentParser()
parser.add_argument("--filename",
                    help="I/O filename, if file exists read answers to game, otherwise play and save given answers",
                    type=str, default="score")
parser.add_argument("--mode", help="Game mode, if set to easy, colors answers", type=str, default="easy")
args = parser.parse_args()

game = Mastermind(args.filename, args.mode)
game.play()