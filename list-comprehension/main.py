import pandas


# student_dict = {"student": ["Angela","Johan", "Lily"], "score": [100, 50, 60]}


# print(student_data_frames)

#loop through a dataframe
# for(key,value) in student_data_frames.items():
#     print(value)

#loop through the rows of a dataframe
# for (index,row) in student_data_frames.iterrows():
#     print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

