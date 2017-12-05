''' Count Valid passphrases '''

def validate_passphrs(passphrs):
    ''' Validate Passphrase '''

    words = passphrs.split()
    anagram_count = 0
    for word in words:
        letters = list(word)
        anagram_count = 0
        for comp_word in words:
            comp_letters = list(comp_word)
            if sorted(letters) == sorted(comp_letters):
                anagram_count += 1

        if anagram_count > 1:
            return False
    return True

def main():
    ''' Count Valid passphrases '''

    with open("../input.txt") as file:
        valid_count = 0
        for passphrs in file:
            if validate_passphrs(passphrs):
                valid_count += 1

        print("Valid Passphrases: %s" % valid_count)

if __name__ == '__main__':
    main()
    