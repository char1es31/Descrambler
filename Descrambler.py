def descramble(characters: str, word_list: list, alphabet: list) -> list:
    """returns list of words matching given characters"""
    words = []
    new_word_list = []
    newer_word_list = []
    inverse_alphabet = []

    # gets alphabet minus characters
    for letter in alphabet:
        for char in characters:
            if letter not in characters and letter not in inverse_alphabet:
                inverse_alphabet.append(letter)

    # Reduces word list by length of words
    for word in word_list:
        if len(word) == len(characters):
            new_word_list.append(word)

    # Reduces word list using the inverse alphabet
    for word in new_word_list:
        add = True

        for letter in inverse_alphabet:
            if letter not in word:
                continue
            else:
                add = False
                break

        if add:
            newer_word_list.append(word)

    # match agaisnt the character count
    for word in newer_word_list:
        add = True

        for char in characters:
            if characters.count(char) != word.count(char):
                add = False

        if add:
            words.append(word)

    # print('newer word list:', newer_word_list)
    # print('new alphabet:', new_alphabet)

    return words
