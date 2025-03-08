from mynyt import WordGuess

game = WordGuess()

game.play('hello')

game.play() # random word

game.play('12345') # is not valid so defaults to a random word

game.play('aaaaa')  # is not valid so defaults to a random word

game.play('magazine')  # is not valid so defaults to a random word