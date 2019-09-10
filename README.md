# DNAtoSLC-Python
A program to simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease.

The program has two versions.

The first program uses a function called ‘translate’ that, when given a DNA sequence of arbitrary length, the program identifies and returns the amino acid sequence of the DNA using the amino acid SLC code found in that table. E.g DNA Input: ATTATTATT Output: III (representing: Isoleucine, Isoleucine, Isoleucine )

Only the first five Amino Acids (i.e I, L, V, F M) are used for now and any other codon is printed as the amino acid 'X' .

The second program (SickleCellDisease_Mutated.py) add's another function to the program called 'mutate'. This function reads the contents of the text file and identifies the first occurrence of the lowercase letter 'a'.

It also now has two output files, i.e. normalDNA, and mutatedDNA. 

normalDNA.txt simply finds the 'a' and changes it to an 'A'.

mutatedDNA.txt finds the 'a' and changes it to a 'T'.
