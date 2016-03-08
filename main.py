import Helper
import Descrambler

spacer = "\n-------------------------\n"
exit_message = "Goodbye!!!"
query_message = "Enter your characters: "
language = "en"

language_assets_folder = "./LanguageAssets"

words = Helper.get_words(
    language_assets_folder + '/word-list.' + language + '.txt')

alphabet = Helper.get_alphabet(
    language_assets_folder + '/alphabet.' + language + '.txt')

# Main Program

while True:
    print(spacer)

    characters = input(query_message)

    if len(characters) == 0:
        x = input("Press <ENTER> again to quit \n")
        if len(x) == 0:
            print(exit_message + spacer)
            break
        else:
            continue

    print(Descrambler.descramble(characters, words, alphabet))
