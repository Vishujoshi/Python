# file = open("E:/Python/Day24/text.docx")
# content = file.read()
# print(content)
# file.close()

# 2.  file is automattically cosed using with 
# 3. mode is used what operation we woul like to perform
with open("E:/Python/Day24/text.docx",mode="a") as file:
    
    file.write("hi")
    


