# Guess The Word!
#### Video Demo:  [Guess The Word!](https://youtu.be/OPTvq_HIdF8)
### Description:
A combination of the famous word games hangman and wordle, ***Guess The Word!*** is a spin off that allows for a satisfying experience where you can practice your skills at filling in incomplete words. By playing this game, not only will you shore up your vocabulary, but you can also gain entertainment and joy from finally guessing a 15 letter word in hell difficulty.

The game starts off with a title screen after which you may choose one of four difficulties. As you progress through the difficulties, the words get longer and longer, going from a simple 3 letter word to 15 letter nightmares. After the difficulty is chosen, you can start entering your guesses. They can be of any length, and any letters in the guess that are also in the correct word will be filled in, the rest being replaced by underscores. Once you successfully guess the word, you may choose to play again or exit.
### Implementation:
First, I procured a dataset of about 5000 common english words from the internet. I then used the [pandas](https://pandas.pydata.org/) library to convert the csv into python lists. Then, I had to filter out some unnecessary words that appeared far too commonly in everyday language or were too short in length. Following that, I filtered the words once again based on the difficulty the user had chosen. The program also checks for the user entering difficulty options aside from the 4 choices provided.

I also used the [pyFiglet](https://pypi.org/project/pyfiglet/) library to prooduce a visually appealing title and win screen for the game.

### Challenges:
A big challenge I faced was creating an algorithm for replacing the correct word with underscores except for letters that the user had guessed correctly and also have correctly guess letters carry over from previous guesses. I ended up creating a list that would contain all the unqiue letters in the guess which would be added to every time the user made a new guess. Then, it was a simple matter of replacing all letters aside from those with underscores.

### How to Run:
First run `pip install -r requirements.txt`

Then, simply navigate to the project folder in your terminal and type `python project.py`
