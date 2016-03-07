def get_words(word_list_file_name: str) -> list:
    """Returns a list of words found in the file"""

    word_list_file = open(word_list_file_name, 'r')

    word_list = []

    for line in word_list_file:
        word_list.append(str(line).replace("\n", ""))

    return word_list


def get_alphabet(alphabet_file_name: str) -> list:
    """Returns list of characters found in file"""

    alphabet_file = open(alphabet_file_name, 'r', encoding='utf8')

    alphabet = []

    while True:
        c = alphabet_file.read(1)
        if not c:
            break
        alphabet.append(c)

    return alphabet
