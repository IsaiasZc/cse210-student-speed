from time import sleep
from game import constants
from game.score import Score
from game.writer import Writer
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        writer (Writer): an instance of Writer.
        writer (Buffer): an instance of Buffer.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._writer = Writer()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the words written by the user.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        if letter == "*":
            self._buffer.reset_word()
        else:
            self._buffer.add_letter(letter)
        self._writer.move_words()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means showing the random words and update the score
        of the right words.

        Args:
            self (Director): An instance of Director.
        """
        self._handle_match_word()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the user reach a score of 10 to 
        declare him winner.

        Args:
            self (Director): An instance of Director.
        """
        
        self._output_service.clear_screen()
        if self._score.get_points() < constants.WIN_SCORE:
            self._output_service.draw_actors(self._writer.get_random_words())
        else: 
            self._output_service.draw_actors(self._writer.get_bye_text())
            self._writer.move_bye_text()
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()
        
    def _handle_match_word(self):
        """Handles the proccess of the random words to be shown on the screen
        and keeps track of the score. 

        Args:
            self (Director): An instance of Director.
        """
        word = self._buffer.get_word()
        words = self._writer.get_random_words()

        for idx,random_word in enumerate(words):
            print(random_word)
            text = random_word.get_text()
            if word == text:
                self._score.add_points(1)
                words.pop(idx)

        if not words:
            self._writer.reset()
       
       

