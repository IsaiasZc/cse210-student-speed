import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """The responsibility of this class is to store the words typed by the user 
    and show them. Also restes the word to rewrite a new one.

    Stereotype:
        Information Holder

    Attributes: 
        _word (string): The word typed by the user.
    """
    

    def __init__(self):
        """The class constructor
        Args:
            self (Buffer): an instance of Buffer.        
        """
        super().__init__()
        self._word = ""
        position = Point(1,constants.MAX_Y) # this is to print this line at the bottom
        self.set_position(position)
        self.reset_word()
    
    def add_letter(self,letter):
        """Show a letter that is typed by the user.
        """
        self._word += letter
        self.set_text(f"Buffer: {self._word}")

    def reset_word(self):
        """Resets the word space for rewrite a new word.
        """
        self._word = ""
        self.set_text(f"Buffer: {self._word}")

    def get_word(self):
        """Gets a word.
        """
        return self._word

    