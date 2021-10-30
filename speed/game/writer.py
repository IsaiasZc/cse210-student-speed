import random
from game import constants
from game.actor import Actor
from game.point import Point

class Writer(Actor):
    
    
    def __init__(self):
        """The class constructor."""
        super().__init__()
        self._random_words = []
        self.reset()

    def reset(self):
        self._random_words.clear()
        for _ in range(constants.STARTING_WORDS):
            text = random.choice(constants.LIBRARY)
            x = random.randint(1,constants.MAX_X-1)
            y = random.randint(1,constants.MAX_Y-1)
            position = Point(x,y)
            vel_x = random.randint(-1,1)
            vel_y = random.randint(-1,1)
            while vel_x == 0 and vel_y == 0:
                vel_y = random.randint(-1,1)
            velocity = Point(vel_x, vel_y)
            self._add_words(text, position, velocity)
    
    def _add_words(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._random_words.append(segment)
    
    def get_random_words(self):
        return self._random_words


    def move_words(self):
        count = len(self._random_words) - 1
        for n in range(count, -1, -1):
            word = self._random_words[n]
            velocity = word.get_velocity()
            word.set_velocity(velocity)
            word.move_next()