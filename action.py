from button import Button

class Action():
    def __init__(self, button: Button, attackType = None, statusEffect = None):
        self.attackType = attackType
        self.statusEffect = statusEffect
        self.button = button 