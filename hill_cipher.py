import math
from sympy import *
# input
pt = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()
#adding redundant values to make square matrix
if len(pt) < len(key):
    pt+=(len(key) - len(pt))*"X"
else:
    pt = pt[:len(key)]
#finding length of square matrix
pt_mat_L = (math.sqrt(len(key)))
key_mat_L = (math.sqrt(len(pt)))
#Original key matrix
Key_Matrix = [[0 for j in range(0, int(pt_mat_L))]
            for i in range(0, int(pt_mat_L))]
j = 0
i = 0
#initializing key matrix with given input
for k in key:
    if j >= pt_mat_L:
        j = 0
        i += 1
    Key_Matrix[i][j] = ord(k) % 65
    j += 1
#Original Plaintext Matrix
PT_Matrix = [[0 for j in range(0, int(key_mat_L))]
                  for i in range(0, int(key_mat_L))]

j = 0
i = 0
#Initializing plaintext matrix with given input
for k in pt:
    if j >= key_mat_L:
        j = 0
        i += 1
    PT_Matrix[i][j] = ord(k) % 65
    j += 1
#Final output matrix
Ans = [[0 for j in range(0, int(key_mat_L))]
          for i in range(0, int(pt_mat_L))]
#matrix multiplication
for j in range(len(PT_Matrix)):
    for i in range(len(Key_Matrix)):
        sum = 0
        for k in range(len(Key_Matrix[i])):
            sum += (Key_Matrix[i][k]*PT_Matrix[j][k])
            Ans[j][i] = sum % 26
encryptedStr = ""

for i in range(len(Ans)):
    for j in range(len(Ans[0])):
        encryptedStr += (chr(Ans[i][j] + 65))
        
print()
print(f"Encryption: {encryptedStr}")
tempMatrix = [[0 for i in range(0,len(Key_Matrix))] for j in range(0,len(PT_Matrix))]

for i in range(len(Key_Matrix)):
    for j in range(len(Key_Matrix[0])):
        tempMatrix[j][i] = Key_Matrix[i][j]

A = Matrix(tempMatrix)
tempMatrix = A.adjugate().T.tolist()        # adjoin calculation using library
determinant = A.det()%26
Inv = 0
for i in range(1,27):                                   #finding inverse
    if (determinant*i)%26 == 1:
        Inv = i
        break
else:
    print("No Possible Multiplcative Inverse")      # in case no multiplicative inverse is found
    exit()

for i in range(len(tempMatrix)):
    for j in range(len(tempMatrix[0])):
        tempMatrix[i][j] = Inv*tempMatrix[i][j]%26          # finding modulo 26 and adding to temporary matrix

j = 0
i = 0
for k in encryptedStr:
    if j >= pt_mat_L:
        j = 0
        i += 1
    PT_Matrix[i][j] = ord(k) % 65               #converting to characters
    j += 1                              

for j in range(len(PT_Matrix)):
    for i in range(len(tempMatrix)):
        sum = 0
        for k in range(len(tempMatrix[i])):
            sum += (tempMatrix[i][k]*PT_Matrix[j][k])
            Ans[j][i] = sum % 26                                # adding output to encrypted string (numeric)


#Decryption
decryptedText = ""
for i in range(len(Ans)):
    for j in range(len(Ans[0])):
        decryptedText += (chr(Ans[i][j] + 65))          # converting back to characters
print(f"Decryption: {decryptedText}")