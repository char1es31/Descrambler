# coding = ascii

from Helper import get_words
from Helper import get_alphabet

import Descrambler

words = get_words("francais.txt")

alphabet = get_alphabet('alphabet.fr.txt')

characters = input("Enter your characters: ")

print(Descrambler.descramble(characters, words, alphabet))
