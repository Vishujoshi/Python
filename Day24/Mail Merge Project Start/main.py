#TODO: Create a letter using starting_letter.txt 
PLACEHOLDER="[name]"
# with open("E:/Python/Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    
#     content=file.read()
#     # ls=content.split("\n")
#     print(content)

# newls=list(content.split(" ",))

# print(newls)
       
    
#for each name in invited_names.txt
with open("E:/Python/Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    
    names=file.readlines()
   
#Replace the [name] placeholder with the actual name.
with open("E:/Python/Day24/Mail Merge Project Start/Output/ReadyToSend/one.txt" ,mode="r") as file:
    content=file.read()
    for name in names:
        striped_name=name.strip()
        newletter=content.replace(PLACEHOLDER,striped_name)
        with open(f"E:/Python/Day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{striped_name}.txt" ,mode="w") as file:
            file.write(newletter)
        # ls=content.split("\n") 
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp