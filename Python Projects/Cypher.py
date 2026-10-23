import sys
def change_message(phrase:str, cipher: dict[str,str]):
    mystery_word = []
    for letter in phrase:
        if letter in cipher:
            letter = cipher[letter]
        elif letter.lower() in cipher:
            letter = cipher[letter.lower()]
        mystery_word.append(letter)
    return "".join(mystery_word)



def main(cipher: dict[str,str], phrase: str):
    phrase = change_message(phrase,cipher)
    print(phrase)

if __name__ == "__main__":
    simpleCipher = {}
    main(simpleCipher, sys.argv[1])
