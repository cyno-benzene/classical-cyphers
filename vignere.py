def mod(x):
    return x%26

def keyGen(key, message):
    diff = len(message) - len(key)
    if len(message) > len(key):
        for i in range(diff):
            key += key[i]
    return key


def listizer(text, mode):
    if mode == 0:
        text = text.lower()
        n = []
        for i in text:
            i = ord(i) - 97
            n.append(i)
        return n
    elif mode == 1:
        n = []
        str = ""
        for i in text:
            i += 97
            i = chr(i)
            n.append(i)
        return str.join(n).upper()
        
            
def virginere(key, message):
    key = keyGen(key, message)
    kList = listizer(key, 0)
    mList = listizer(message, 0)
    n = []
    j = 0 #Counter for looping through other list
    for i in kList:
        i = mod(i + mList[j])
        n.append(i)
        j += 1
    del kList, mList, j
    return listizer(n, 1)
    
    
print("\n******************\nVIRGINERE CIPHER\n******************\n")
key = input("Enter key: ")
message = input("Enter the message to be encrypted(without spaces!): ")
print("\n\nCipher test: ", virginere(key, message))