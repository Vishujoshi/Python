alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# print(alphabet.index("i"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(t, s):
    string=""
    for i in t:
        if i not in alphabet:
            string+=i
        else:
            index=alphabet.index(i)
            
            newindex=index+s
            if newindex>25:
                newindex=newindex-26
            string+=alphabet[newindex]
    print(string)     

# encrypt(t=text,s=shift)
 

    
def decrypt(t, s):
    string=""
    for i in t:
        if i not in alphabet:
            string+=i
        else:
            index=alphabet.index(i)
            
            newindex=index-s
            if newindex<0:
                newindex=newindex+26
            string+=alphabet[newindex]
    print(string)     

if direction=="encode":
    encrypt(t=text,s=shift)
else: 
    decrypt(t=text,s=shift)
