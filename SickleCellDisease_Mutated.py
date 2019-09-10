dnaFile = open('DNA.txt', 'r')                                                                  # Opens Text file
dnaString = dnaFile.read()                                                                      # Reads all data from text files and assigns to a variable

userInput = str(input("Enter DNA sequence: "))                                                  # Requests string input from user.
inputList = []                                                                                  # Creates an empty list 
comboList = []                                                                                  # Creates an empty list 
comboString = ""                                                                                # Assigns variable with empty string value
remainder = []                                                                                  # Creates an empty list 
stringInput = ""                                                                                # Assigns variable with empty string value

def split3(stringInput):                                                                        # Defines a function with an argument
    while stringInput:                                                                          # Starts a while loop to loop through the users input
        inputList.append(stringInput[:3])                                                       # Splits every 3 charachters into strings and appends to a list
        stringInput = stringInput[3:]

def translate():                                                                                # Defines a function
    for codon in inputList:                                                                     # starts a for loop that loops through a list
        if len(codon) % 3 == 0:                                                                 # Tests conditions lengh. If divisable by 3 then,
            if codon in {"ATT", "ATC", "ATA"}:                                                  # Tests condition and if true,
                comboList.append('I ')                                                          # adds string to list
            elif codon in {"CTT", "CTC", "CTA", "CTG", "TTA", "TTG"}:                           # Tests condition and if true,
                comboList.append('L ')                                                          # adds string to list
            elif codon in {"GTT", "GTC", "GTA", "GTG"}:                                         # Tests condition and if true,
                comboList.append('V ')                                                          # adds string to list
            elif codon in {"TTT", "TTC"}:                                                       # Tests condition and if true,
                comboList.append('F ')                                                          # adds string to list
            elif codon in {"ATG"}:                                                              # Tests condition and if true,
                comboList.append('M ')                                                          # adds string to list
            else:                                                                    
                comboList.append('"Amino Acid X" ')                                             # Else, appends list with a string value
                #comboList.append('# ')
        elif len(codon) % 2 == 0 or len(codon) % 1 == 0:                                        # tests conditions lengh. If divisable by 1 & 2 then,
            remainder.append(codon)                                                             # adds string to list
        else:                                                                                   # Else, prints message
            print("ERROR")
    return codon                                                                                # Returns string left after all conditions have been tested

def mutate():                                                                                   # Defines a function
    findInDNA = dnaString.replace("\n", "")                                                     # Removes all page breaks from open text document
    aString = findInDNA.find('a')                                                               # Searches for the first occurance of a lowercase "a"
    return int(aString)                                                                         # Returns variable value

def txtTranslate(toSplit):                                                                      # Defines a function
    split3(toSplit)                                                                             # Calls function and provides argument
    translate()                                                                                 # Calls another function

def printSLC(x):
    print("\n" + x)
    print("Anamino acid sequence of the DNA using SLC codes: \n" + comboString)
    if len(remainder) > 0:                                                                      # if list length is more than 0, prints message and variable
        print("\nList of incomplete Amino Acids within sequence: ") 
        print(output)

#User Input

stringInput = userInput                                                                         # Assigns new value to variable
split3(userInput)                                                                               # Calls function and provides argument

output = "".join(str(translate()))                                                              # Joins list items together into a string
comboString = "".join(comboList)                                                                # Joins list items together into a string

printSLC("User Input")                                                                          # Calls function and gives argument to print results 


#Normal DNA

inputList = []                                                                                  # Creates an empty list 
comboList = []                                                                                  # Creates an empty list 
comboString = ""                                                                                # Assigns variable with empty string value
remainder = []                                                                                  # Creates an empty list 
stringInput = ""                                                                                # Assigns variable with empty string value

normalDNACreate = open('normalDNA.txt', 'w')                                                    # Opens Text file
index = mutate()                                                                                # Calls function and assigns result to variable
dnaNormalString = dnaString.replace(dnaString[index], 'A')                                      # Replaces string value at index by calling a function
normalDNACreate.write(dnaNormalString)                                                          # Writes string value to opened text file
normalDNACreate.close()                                                                         # Closes open text document

normalDNARead = open('normalDNA.txt', 'r')                                                      # Opens Text file
normalText = normalDNARead.read()                                                               # Reads all data from text files and assigns to a variable
txtTranslate(normalText.replace("\n", ""))                                                      # Calls function and provides argument
stringInput = normalText                                                                        # Assigns new value to variable
output = "".join(str(translate()))                                                              # Joins list items together into a string
comboString = "".join(comboList)                                                                # Joins list items together into a string
normalDNARead.close()                                                                           # Closes open text document

printSLC("Normal DNA")                                                                          # Calls function and gives argument to print results 


#Mutated DNA

inputList = []                                                                                  # Creates an empty list 
comboList = []                                                                                  # Creates an empty list 
comboString = ""                                                                                # Assigns variable with empty string value
remainder = []                                                                                  # Creates an empty list 
stringInput = ""                                                                                # Assigns variable with empty string value

mutatedDNACreate = open('mutatedDNA.txt', 'w')                                                  # Opens Text file
index = mutate()                                                                                # Calls function and assigns result to variable
dnaMutatedString = dnaString.replace(dnaString[index], 'T')                                     # Replaces string value at index by calling a function
mutatedDNACreate.write(dnaMutatedString)                                                        # Writes string value to opened text file
mutatedDNACreate.close()                                                                        # Closes open text document

mutatedDNARead = open('mutatedDNA.txt', 'r')                                                    # Opens Text file
mutatedText = mutatedDNARead.read()                                                             # Reads all data from text files and assigns to a variable
txtTranslate(mutatedText.replace("\n", ""))                                                     # Calls function and provides argument
stringInput = mutatedText                                                                       # Assigns new value to variable
output = "".join(str(translate()))                                                              # Joins list items together into a string
comboString = "".join(comboList)                                                                # Joins list items together into a string
mutatedDNARead.close()                                                                          # Closes open text document

printSLC("Mutated DNA")                                                                         # Calls function and gives argument to print results 

