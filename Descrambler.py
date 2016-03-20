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
