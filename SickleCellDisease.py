userInput = str(input("Enter DNA sequence: "))                                      # Requests string input from user.
inputList = []                                                                      # Creates an empty list 
comboList = []                                                                      # Creates an empty list 
remainder = []                                                                      # Creates an empty list 


while userInput:                                                                    # Starts a while loop to loop through the users input
    inputList.append(userInput[:3])                                                 # Splits every 3 charachters into strings and appends to a list
    userInput = userInput[3:]                                                        

def translate():                                                                    # defines a function
    for codon in inputList:                                                         # starts a for loop that loops through a list
        if len(codon) % 3 == 0:
            if codon in {"ATT", "ATC", "ATA"}:                                      # Tests condition and if true,
                comboList.append('I ')                                              # adds string to list
            elif codon in {"CTT", "CTC", "CTA", "CTG", "TTA", "TTG"}:               # Tests condition and if true,
                comboList.append('L ')                                              # adds string to list
            elif codon in {"GTT", "GTC", "GTA", "GTG"}:                             # Tests condition and if true,
                comboList.append('V ')                                              # adds string to list
            elif codon in {"TTT", "TTC"}:                                           # Tests condition and if true,
                comboList.append('F ')                                              # adds string to list
            elif codon in {"ATG"}:                                                  # Tests condition and if true,
                comboList.append('M ')                                              # adds string to list
            else:
                comboList.append('"Amino Acid X" ')
        elif len(codon) % 2 == 0 or len(codon) % 1 == 0:                            # tests conditions lengh. If divisable with 2 then,
            remainder.append(codon)                                                 # adds string to list
        else:
            print("ERROR")
    return codon                                                                    # Returns string left after all conditions have been tested


output = "".join(str(translate()))                                                  # Joins list items together into a string
comboList = "".join(comboList)                                                      # Joins list items together into a string

print("\nAnamino acid sequence of the DNA using SLC codes: \n" + comboList)

if len(remainder) > 0:                                                              # if list length is more than 0, prints message and variable
    print("\nList of incomplete Amino Acids within sequence: ") 
    print(output)


