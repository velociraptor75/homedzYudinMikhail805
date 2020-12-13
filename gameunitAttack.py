class Attacker:
    _health = None
    _attack = None
    def is_alive(self):
        return self._health > 0
    def attack(self, target):
        target._health -= self._attack

    
    