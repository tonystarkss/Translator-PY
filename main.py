
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + "j"
        else:
            translation = translation + letter
    return translation
# Check letter in phrases for lower/upper case and to check for vowels aeiou and replace them with the letter j & return


print(translate(input("Enter a phrase: ")))
# Print statement with an input for a phrase 



