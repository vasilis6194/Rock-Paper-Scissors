import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


def print_pause(string):
    print(string)
    time.sleep(1.5)


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AmebaPlayer(Player):
    def move(self):
        move = "rock"
        return move


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        move = input("Choose your move.Write 'rock', 'paper' or 'scissors':\n")
        while move.lower() not in moves:
            move = input("Please choose between 'rock',"
                         "'paper' or 'scissors':\n")
        return move.lower()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        else:
            self.my_move = 'rock'
        return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.last_game_mode = None

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        winner = beats(move1, move2)

        print_pause(f"Player 1: {move1}  Player 2: {move2}")

        if winner is True:
            print_pause("The winner of this round is Player 1.")
            self.score1 += 1
        elif winner is False and move1 == move2:
            print_pause("There is no winner.It's a tie!")
        else:
            print_pause("The winner of this round is Player 2.")
            self.score2 += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_again(self):
        restart = input("Would you like to play again?Type 'y'"
                        "for yes or 'n' for no:\n")
        while restart != 'y' and restart != 'n':
            restart = input("Please type only 'y' or 'n':\n")
        if restart == 'y':
            self.score1 = 0
            self.score2 = 0
            if self.last_game_mode == "single_round":
                self.single_round()
            elif self.last_game_mode == "play_game":
                self.play_game()
        elif restart == 'n':
            print("Thank you for playing!")

    def single_round(self):
        self.last_game_mode = "single_round"
        print("Game start!\n")
        print(f"Single Round Game.Win it or Lose it!")
        self.play_round()
        print(f"The final score is {self.score1} - {self.score2}!")
        if self.score1 > self.score2:
            print("Player 1 is the winner.Congratulations!!!")
        elif self.score2 > self.score1:
            print("Player 2 is the winner.Congratulations!!!")
        else:
            print("There is no winner.It's a tie!")
        print("Game Over!")
        self.play_again()

    def play_game(self):
        self.last_game_mode = 'play_game'
        print("Game start!\n")
        for round in range(3):
            print(f"\nRound {round}:")
            self.play_round()
            print(f"Score {self.score1} : {self.score2}")
        print(f"The final score is {self.score1} - {self.score2}!")
        if self.score1 > self.score2:
            print("Player 1 is the winner.Congratulations!!!")
        elif self.score2 > self.score1:
            print("Player 2 is the winner.Congratulations!!!")
        else:
            print("There is no winner.It's a tie!")
        print("Game over!")
        self.play_again()


if __name__ == '__main__':
    players = {
        '1': AmebaPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }
    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")
    while (p1 := input("Choose player 1: ")) not in players.keys():
        print("Invalid choice, please select player 1 from the list.")
    while (p2 := input("Choose player 2: ")) not in players.keys():
        print("Invalid choice, please select player 2 from the list.")

    game = Game(players[p1](), players[p2]())
    game.play_game()
