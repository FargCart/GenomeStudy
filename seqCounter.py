import os

seq = open('SOD1_seq_NCBI.txt', 'r')

modSeq = str(seq.read())

print(modSeq[113:124])

# Take the sequence in the file and compare it to every cell in the excel sheet

# Take first letter in reference sequence and see if matches, anywhere in sequence, if

