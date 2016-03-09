class Descrambler:

    def __init__(self, characters: str, word_list: list, alphabet: list):
        self.alphabet = alphabet
        self.characters = characters
        self.word_list = word_list

        self.words = []
        self.new_word_list = []
        self.newer_word_list = []
        self.inverse_alphabet = []

    def descramble(self) -> list:
        """returns list of words matching given characters"""

        # gets alphabet minus characters
        for letter in self.alphabet:
            for char in self.characters:
                if letter not in self.characters and letter not in self.inverse_alphabet:
                    self.inverse_alphabet.append(letter)

        # Reduces word list by length of words
        for word in self.word_list:
            if len(word) == len(self.characters):
                self.new_word_list.append(word)

        # Reduces word list using the inverse alphabet
        for word in self.new_word_list:
            add = True

            for letter in self.inverse_alphabet:
                if letter not in word:
                    continue
                else:
                    add = False
                    break

            if add:
                self.newer_word_list.append(word)

        # match agaisnt the character count
        for word in self.newer_word_list:
            add = True

            for char in self.characters:
                if self.characters.count(char) != word.count(char):
                    add = False

            if add:
                self.words.append(word)

        return self.words
