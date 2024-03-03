import pandas

data=pandas.read_csv("E:/Python/Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
    


#TODO 1. Create a dictionary in this format:
# words_dictionary=data.to_dict()
words_dataframe=pandas.DataFrame(data)
# print(words_dataframe)
dict={row.letter: row.code for index,row in words_dataframe.iterrows()}
# for index,row in words_dataframe.iterrows():
#  print(row[0]) 
# print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userInput=input("Enter a word : ").upper()
resultlist=[dict[letter] for letter in userInput]
# resultlist=[value for key,value in dict.items() if key in userInput.upper()]
print(resultlist)
