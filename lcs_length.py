"""

script file: lcs_length.py

author: Richard Asiamah (10937891)

date: 8/03/22

"""




def LCS_LENGTH(X,Y):
    global m , n
    m, n = len(X), len(Y)
    
    
    
    # create tables c and b
    # m rows and n columns
    b = [[0 for i in range(0, n+1)] for j in range(0, m+1)]
    c = [[0 for i in range(0, n +1)] for j in range(0, m +1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = chr(92)
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "^"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "<"

                
    return b, c, c[m][n]

# provide the two string here
X = "ABRACADABRA"
Y = "YABBADABBADOO"

b, c, maxLCS = LCS_LENGTH(X, Y)


def PRINT_LCS(b, X, i, j):

    if i == 0 or j == 0: return
   
    if b[i][j] == chr(92):
        print(X[i-1], end ="")   # the result here is reversed because the indexing was done on the highest value of i
        PRINT_LCS(b, X, i -1, j - 1)
    elif b[i][j] == "^":
        PRINT_LCS(b, X, i -1, j)
    else:
        PRINT_LCS(b, X, i, j - 1)
    
print("The LCS is in reverse order, read backward to obtain it")
PRINT_LCS(b, X, i = m, j = n)  # the function return the reverse of the LCS
                                # to find the LCS, read the character backwards
print()
print(f"The LCS of {X} and {Y} = {maxLCS}")
print(b)
print(c)
