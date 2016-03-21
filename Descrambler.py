class Descrambler:

    def __init__(self, word_list: list):
        self.word_list = word_list

    def descramble(self, characters: str)-> list:

        words = []
        new_word_list = []

        # Reduces word list by length of words
        for word in self.word_list:
            if len(word) <= len(characters):
                new_word_list.append(word)

        # compare characters between word-list and input
        for word in new_word_list:
            add = True
            for char in word:
                if char not in characters or word.count(char) > characters.count(char):
                    add = False
            if add:
                words.append(word)

        # return a copy of the list
        return list(words)

    def descramble_rec(self, characters: str) -> list:

        words = []
        new_word_list = []

        # Reduces word list by length of words
        for word in self.word_list:
            if len(word) <= len(characters):
                new_word_list.append(word)

        # compare characters between word-list and input
        for word in new_word_list:
            add = True
            for char in word:
                if char not in characters or word.count(char) > characters.count(char):
                    add = False

            if add:
                new_characters = characters

                for letter in word:
                    new_characters = new_characters.replace(letter, '', 1)

                if len(new_characters) > 0:
                    secondary_words = self.descramble_rec(new_characters)

                    if len(secondary_words) > 0:
                        for secondary_word in secondary_words:
                            words.append(word + ' ' + secondary_word)
                    else:
                        words.append(word)
                else:
                    words.append(word)

        return list(words)
