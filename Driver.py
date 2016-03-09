import Helper
import Descrambler


class Driver:
    """Drives the descrambling process"""

    def __init__(self):
        """Initialize all variables, uses the Helper module"""

        self.spacer = "\n-------------------------\n"
        self.exit_message = "Goodbye!!!"
        self.query_message = "Enter your characters: "

        self.language_assets_folder = "./LanguageAssets"

        self.descrambler = None

        self.language_list = Helper.get_languages(self.language_assets_folder)

        self.language = Helper.get_language(self.language_list)

        self.words = Helper.get_words(
            self.language_assets_folder +
            '/word-list.' +
            self.language +
            '.txt')

        self.alphabet = Helper.get_alphabet(
            self.language_assets_folder +
            '/alphabet.' +
            self.language +
            '.txt')

    def main(self):
        """loops through the descrambling process, asking
        the user for new characters after every descrambling"""

        while True:
            print(self.spacer)

            characters = input(self.query_message)

            if len(characters) == 0:
                x = input("Press <ENTER> again to quit \n")
                if len(x) == 0:
                    print(self.exit_message + self.spacer)
                    quit()
                else:
                    continue

            self.descrambler = Descrambler.Descrambler(
                characters, self.words, self.alphabet)

            words = self.descrambler.descramble()

            print(self.spacer)
            print(len(words), "words found:\n")

            for word in words:
                print(" - ", word)


if __name__ == '__main__':
    driver = Driver()
    driver.main()
