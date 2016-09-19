
open_file = open("sentence.txt")
sentence = open_file.read()
open_file.close()

sentence = sentence.lower()
exclude = "aeiou"

# for letter in exclude:
#     sentence = sentence.replace(letter, "")

sentence = [sentence.replace(letter, "") for letter in exclude]

print(sentence)
