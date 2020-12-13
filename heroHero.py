# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    _health = 100
    _attack = 50
    _experience = 0
    def attack(self, target):
        target._health -= self._attack
    def is_alive(self):
        return self._health > 0
    def __init__(self, name):
        self.name = name