with open("E:/Python/text.txt" ,mode="r") as file:
    content=file.read()
    print(content)
    
with open("E:/Python/texts.txt" ,mode="w") as file:
    newc=content.replace("Vishal","Abhi")
    file.write(newc)
    
   