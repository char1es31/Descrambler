from os import listdir
from os.path import isfile, join
import re


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


def get_languages(directory_name: str) -> list:
    """Returns a list of all availible languages in the LanguageAssets folder"""

    language_list = []

    file_list = [
        f for f in listdir(directory_name) if isfile(join(directory_name, f))]

    lang1, lang2 = "", ""

    # scan for alphabet file
    for file_name1 in file_list:
        if re.match('alphabet.\w{2}.txt', file_name1):
            # if found, scan for word-list file of the same language
            lang1 = file_name1.replace('alphabet.', '').replace('.txt', '')

            for file_name2 in file_list:
                if re.match('word-list.' + lang1 + '.txt', file_name2):
                    lang2 = file_name1.replace('alphabet.', '').replace('.txt', '')

                    if lang1 == lang2:
                        language_list.append(lang1)

    return language_list
