import Helper
import Descrambler


class Driver:

    def __init__(self):
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

        # Main program loop

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

            print(self.descrambler.descramble())


if __name__ == '__main__':
    driver = Driver()
    driver.main()
