# createing a dictionary usint key value pair
program_dictionary={
    "bug " : " Anything that caused to break the prpgram",
    "Function" : "Commands that help user to do something",
    "Loop" : "used to repeat a set of instructions"
}

# print Dictionary
print(program_dictionary)

# adding new key value pair to dictionary
program_dictionary["new entry"]="THis is new entry"
print(program_dictionary)

# Editing a entry in dictionay
program_dictionary["Loop"]=" this is edited version"
print(program_dictionary)
print(program_dictionary["Loop"])

# deleting a dictionary
# program_dictionary={}
# print(program_dictionary)

# looping through dictinory
for i in program_dictionary:
    print(i)
    # Note i(loop variable) only print keys in dictinary
    print(program_dictionary[i])