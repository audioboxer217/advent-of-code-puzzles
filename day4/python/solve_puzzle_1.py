''' Count Valid passphrases '''

def validate_passphrs(passphrs):
    ''' Validate Passphrase '''

    words = passphrs.split()

    for word in words:
        word_count = words.count(word)
        if word_count > 1:
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
    