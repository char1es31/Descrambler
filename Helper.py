import os
import re


def get_words(directory_name: str, language: str) -> list:
    """Returns a list of words found in the file"""

    file_name = directory_name + '/word-list.' + language + '.txt'

    word_list_file = open(file_name, 'r', encoding='utf8')

    word_list = []

    for line in word_list_file:
        word_list.append(str(line).replace("\n", ""))

    return word_list


def get_language_list(directory_name: str) -> list:
    """Returns a list of all availible languages in the LanguageAssets folder"""

    language_list = []

    file_list = [
        f for f in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, f))]

    # scan for word-list file
    for file_name in file_list:
        lang = re.match('word-list.(\w{2}).txt', file_name)

        if lang:
            language_list.append(str(lang.group(1)))

    return language_list


def get_language(language_list: list) -> str:
    """Asks the user which language they would like to use"""

    print("Available languages: ")
    print(language_list)

    language = ''

    while True:
        language = input("Please enter a langauge: ")
        if language in language_list:
            break
        else:
            print("Not a valid language")

    return language
