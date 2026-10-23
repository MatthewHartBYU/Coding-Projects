import random
def isGood(userWord):
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    for letter in userWord:
        if letter in nums:
            return False
    return True
def validateCommand(prompt):
    userWord = input(prompt)
    while not isGood(userWord):
        userWord = input("Oops! Invalid word. Make sure you don't type in numbers.")
    return userWord
def main():
    userWord = validateCommand("Enter a word, and I will encrypt it below!")
    characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    encryptedWord = ""
    for letter in userWord:
        randomLetter = random.choice(characters)
        if letter == " ":
            encryptedWord += " "
        encryptedWord += randomLetter
        characters.remove(randomLetter)
    print(encryptedWord)

main()
