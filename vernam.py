def xorer(x,y): return x ^ y

def listizer(text, mode):
  if mode == 0:
    text = text.lower()
    n = []
    for i in text:
      i = ord(i) - 97
      n.append(i)
    return n
  if mode == 1:
    n = []
    str = ""
    for i in text:
      i = i + 97
      i = chr(i)
      n.append(i)
    return str.join(n).upper()
  

def vernam(key, mess):
  kList = listizer(key,0)
  mList = listizer(mess,0)
  n = []
  i = 0
  for x in mList:
    if i == len(kList):
      i = 0
    x = xorer(x,kList[i])
    n.append(x)
    i += 1
  del i
  c = listizer(n, 1)
  return c

def decrypt(key, mess):
  return vernam(key, vernam(key,mess))


print("\n******************\nVERNAM CIPHER\n******************\n") 
key=input("Enter key: ")
mess=input("Enter message to be encrypted ")
print("\n\nCipher text: ", vernam(key,mess))
print("Decryption: ", decrypt(key,mess))