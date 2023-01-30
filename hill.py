import numpy as np

def hillCip(plain, keyString):
    a = plainMatrix(plain)
    keyMat = keyMatrix(keyString)
    res = mult(a, keyMat)
    return res

# Convert string to corresponding triplets matrix
def plainMatrix(plain):
    plain = plain.lower()
    a = []
    for x in plain:
        a.append(ord(x) - 97)
    return a

# Convert string key to matrix
def keyMatrix(keyString):
    n = []
    for x in keyString:
        n.append(ord(x) - 97)
    mat = np.array(n).reshape(3,3)
    return mat

# Calculate modulus
def mod(r):
    return r%26

# Multiply 1 x 3 matrix with key and mod
def mult(a, keyMat):
    result = np.dot(a,keyMat)
    result[0] = mod(result[0])
    result[1] = mod(result[1])
    result[2] = mod(result[2])
    stringer(result)


def stringer(result):
    print(chr(result[0] + 97).upper() + chr(result[1] + 97).upper() + chr(result[2] + 97).upper())
    


# keyString = input("Enter key string[size 9]: ") 
keyString = "HILLMAGIC"
# while len(keyString) != 9:
#     length = len(keyString)
#     keyString = input(f"You have entered {length} letters. Please enter a '9' letter key! ")
# plain = input("Enter messege: ")
plain = "saveyeear"
hillCip(plain, keyString.lower())



