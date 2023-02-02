import numpy as np
import math
# An historical use of the Route Cipher was the Union Route Cipher used by the Union forces during the American Civil War. Rather than transposing letters by the given route, it moved whole words around. Some words, of vital importance were not protected in this way, so they were first encoded using a codeword. Sometimes, the cipher clerks would even add whole null words to the ciphertext, often making the message humorous.

def rough():
  pass

message = "want to have fun with you"
a = []

# Conerted message string to a list  
for x in message:
  if x == " ":
    pass
  else:a.append(x)


size = len(a) 
safe = () #matrix size tuple 

# Loop to find the best size for matrix
for x in range(5,10):
  for y in range(3,10):
    product = x * y
    if product >= size:
      safe = safe + (x,)
      safe = safe + (y,)      
      break
  break

# Filled extra spaces in the matrix with X
for x in range(abs(math.prod(safe) - size)): a.append("x")

# Matrix obtained
mArr = np.array(a).reshape(safe)

# Converted matrix to string form
str = ""
for col in range(mArr.shape[1]): 
  print(str.join((mArr[:, col])).upper(), end=" ")
