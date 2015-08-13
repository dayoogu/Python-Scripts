# coding: utf-8

from scene import *
import random

choices = '🌚', '✋', '✂️'

class rps(Scene):
    def __init__(self):
        self.player = self.computer = None

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

    def stop(self):
        print('stop: {}, {}'.format(self.player, self.computer))

    def draw(self):
        background(0, 0.05, 0.2)
        self.root_layer.update(self.dt)
        self.root_layer.draw()

    def rock_action(self):
        self.button.background = Color(0,0,0,0)
        self.player = '🌚'
        self.computer = random.choice(choices)

    def paper_action(self):
        self.button1.background = Color(0,0,0,0)
        self.player = '📄'
        self.computer = random.choice(choices)

    def scissors_action(self):
        self.button2.background = Color(0,0,0,0)
        self.player = '✂️'
        self.computer = random.choice(choices)

print('=' * 10)
run(rps())
