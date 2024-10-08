import pandas

# Creating a dictionary using .iterrows()

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)

# Creating a list of words using the phonetic_dict for each letter of the user_input

def phonetic():
    user_input = input("Enter a word\n").upper()
    try:
        list_words = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Illegal Record was entered")
        phonetic()
    else:
        print(list_words)

phonetic()