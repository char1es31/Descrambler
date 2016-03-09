def scrape(file_name: str) -> list:
    """Scrapes each unique character from a text file, removes \n"""

    alphabet = []
    sorted_alphabet = []

    # read file char by char, and generate alphabet
    with open(file_name, 'r', encoding='UTF-8') as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c not in alphabet:
                alphabet.append(c)

    alphabet.remove('\n')
    sorted_alphabet = sorted(alphabet)

    return sorted_alphabet


def main():
    """asks user for input/output files, and scrapes and saves respectivly"""

    character_count = 0

    input_file = str(input("path of file to be scraped?: "))

    output_file = str(input("path of file to be saved?: "))

    alphabet = scrape(input_file)

    with open(output_file, mode='w', encoding="UTF-8") as f:
        for c in alphabet:
            f.write(c)
            character_count += 1

    print(character_count, "characters scraped")


if __name__ == '__main__':
    main()
