quote = input("Enter a famous quote: ")
word = ""

for character in quote:
    if character.isalpha() == True:
        word += character
    elif word.lower() >= "h":
        print(word.upper())
        word = ""
    else:
        word = ""
if word.lower() >= 'h':
    print(word.upper())