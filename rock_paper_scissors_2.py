# coding: utf-8
from scene import *
import random

choices = '🌚', '📄', '✂️'

def get_ruling(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return "Draw"
    elif player_choice == '🌚':
        return 'Win' if opponent_choice == '✂️' else 'Lose'
    elif player_choice == '📄':
        return 'Win' if opponent_choice == '🌚' else 'Lose'
    else: # player_choice == '✂️'
        return 'Win' if opponent_choice == '📄' else 'Lose'

class rps(Scene):
    def __init__(self):
        self.player = None
        self.computer = None

    def setup(self):
        self.button = Button(Rect(self.size.w/2-60, self.size.h/1-150, 125, 125))
        self.button.background = Color(0,0,0,0)
        self.button.stroke = Color(0,0,0,0)
        self.button.image = 'Moon_2'
        self.button.action = self.rock_action
        self.add_layer(self.button)

        self.button1 = Button(Rect(self.size.w/2-60, self.size.h/1-290, 125, 125))
        self.button1.background = Color(0,0,0,0)
        self.button1.stroke = Color(0,0,0,0)
        self.button1.image = 'Page_Facing_Up'
        self.button1.action = self.paper_action
        self.add_layer(self.button1)

        self.button2 = Button(Rect(self.size.w/2-60, self.size.h/1-450, 125, 125))
        self.button2.background = Color(0,0,0,0)
        self.button2.stroke = Color(0,0,0,0)
        self.button2.image = 'Scissors'
        self.button2.action = self.scissors_action
        self.add_layer(self.button2)

    def rock_action(self):
        self.button.background = Color(0,0,0,0)
        self.player = '🌚'
        self.computer = random.choice(choices)
        run(ending(self.player, self.computer))

    def paper_action(self):
        self.button1.background = Color(0,0,0,0)
        self.player = '📄'
        self.computer = random.choice(choices)
        run(ending(self.player, self.computer))

    def scissors_action(self):
        self.button2.background = Color(0,0,0,0)
        self.player = '✂️'
        self.computer = random.choice(choices)
        run(ending(self.player, self.computer))

    def draw(self):
        background(0, 0.05, 0.2)
        self.root_layer.update(self.dt)
        self.root_layer.draw()


class ending(Scene):
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.ruling = get_ruling(player, computer)

    def setup(self):
        self.next = Button(Rect(self.size.w/2+77, self.size.h/1-480, 80, 40), 'Next')
        self.next.background = Color(1,1,1)
        self.next.stroke = Color(1,1,1)
        self.next.action = self.next_action
        self.add_layer(self.next)

    def next_action(self):
        self.next.background = Color(1,1,1)
        run(rps(), PORTRAIT)

    def draw(self):
        background(0,0.05,0.2)
        self.root_layer.update(self.dt)
        self.root_layer.draw()
        tint(1,1,1)
        msg = '\nYou {}!\n\n\n\n'.format(self.ruling)
        text(msg, x=self.size.w/3+50, y=self.size.h/5*3+20, font_size=60)
        msg = '\n\n\n\nYou chose:\n{}\n\nComputer chose:\n{}'.format(self.player, self.computer)
        text(msg, x=self.size.w/3+29, y=self.size.h/5*3, font_size=35)

run(rps(), PORTRAIT)
