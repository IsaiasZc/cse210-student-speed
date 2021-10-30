import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    
    

    def __init__(self):
        """The class constructor"""
        super().__init__()
        self._word = ""
        position = Point(1,constants.MAX_Y) # this is to print this line at the bottom
        self.set_position(position)
        self.reset_word()
    
    def add_letter(self,letter):
        self._word += letter
        self.set_text(f"Buffer: {self._word}")

    def reset_word(self):
        self._word = ""
        self.set_text(f"Buffer: {self._word}")

    def get_word(self):
        return self._word

    