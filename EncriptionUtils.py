def main():
    a =raw_input("Choose encrypt or decrypt!")
    s= raw_input("Input desired string")
    if a== "encrypt":
        print(encrpyt(s))
    if a == "decrypt":
        print(decrypt(s))
def encrpyt(str):
    e = ""
    for c in str:
        # CR Print a warning!
        # We only encrypt simple strings with characters and digit, No fancy characters!
        if c in ascii_letters or c in digits:
            new_c = chr(ord(c) + 1)
            e += new_c
    return e # returns e
def decrypt(str):
    d = ""
    for c in str:
        # We only decrypt simple strings with characters and digit, No fancy characters!
        if c in ascii_letters or c in digits:
            new_c = chr(ord(c) - 1)
            d += new_c
    return d #returns d


if __name__ == "__main__":
    main()