"""

    script file: lcs_length.py

    author: Richard Asiamah (10937891)

    date: 8/03/22

    course: Data Structures and Algorithms (CSCD 603)

"""




def LCS_LENGTH(X,Y):
    """
     This function takes two strings an
     argument and returns the longest common subsequence (LCS)
    """
    
    global m , n
    m, n = len(X), len(Y)  # assign the length of the two strings to m and n
    
    
    
    # create tables c and b
    # m rows and n columns
    # fill the two tables created with zeroes
    b = [[0 for i in range(0, n+1)] for j in range(0, m+1)]
    c = [[0 for i in range(0, n +1)] for j in range(0, m +1)]

    
    # loop throught the tables and update accordingly
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

                
    return b, c, c[m][n]    # the function table b, c and maximum value in table c


# provide the two string here
# Example of strings: ABRACADABRA and CASABLANCA
X = ""
Y = ""


# assigned the return value b, c and c[m][n] to variables b, c and maxLCS
b, c, maxLCS = LCS_LENGTH(X, Y)



def PRINT_LCS(b, X, i, j):
    """
     This function returns table b used for backtracking
     to find the LCS strings
     
    """

    global result

    if i == len(X):
        result = []   # create an empty list to hold the strings

    if i == 0 or j == 0:   # this section serves the base to break the recursion
        return result
   
    if b[i][j] == chr(92):
        result.append(X[i-1])   
        PRINT_LCS(b, X, i -1, j - 1)
    elif b[i][j] == "^":
        PRINT_LCS(b, X, i -1, j)
    else:
        PRINT_LCS(b, X, i, j - 1)


    

PRINT_LCS(b, X, i = m, j = n)


print("Backtrack substring is " + "".join(result))
print("The substring is " + "".join(result[::-1]))
print()
print(f"The LCS of {X} and {Y} = {maxLCS}")
print(b)
print(c)



