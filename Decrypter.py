keys = {
    "!":"a",
    "@":"b",
    "#":"c",
    "$":"d",
    "%":"e",
    "^":"f",
    "&":"g",
    "*":"h",
    "(":"i",
    ")":"j",
    "-":"K",
    "_":"l",
    "+":"m",
    "=":"n",
    "{":"o",
    "[":"p",
    "}":"q",
    "]":"r",
    "|":"s",
    ":":"t",
    ";":"u",
    "<":"v",
    ">":"w",
    ",":"x",
    ".":"y",
    "?":"z",
    " ":" "
}
def decryptePhrase(phrase):
    decryptedPhrase = ""
    for letter in phrase:
        decryptedPhrase += keys[letter]
    print(decryptedPhrase)
def main():
    decryptePhrase("*%__{ +!::*%>")
main()