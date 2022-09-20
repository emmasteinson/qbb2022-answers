#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA

gap_penalty = float(sys.argv[1])
dna_score = sys.argv[2] #scoring matrix file (also AA score matrix input here)
fasta_file = sys.argv[3]
file_path = sys.argv[4] #file path to write the alignment to 

input_sequences = readFASTA(open(fasta_file)) 
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]



dic = {} #initialize dictionary
hoxd = np.loadtxt(open(dna_score), object, skiprows=1)
letter = np.array(hoxd[:,0]) #makes array with just letters
score = np.array(hoxd[:,1:]).astype(int) #makes array wiith just the scores
for i, letter in enumerate(letter): #i is the index numebr j is the letter
    dic[letter] = i

   

#This populates the F-matrix stores scores as you go thorugh alignment. filling out score for every possible event that could happen as you algin these sequences
F_matrix = np.zeros((len(sequence1) +1, len(sequence2) +1))
trace_matrix = np.zeros((len(sequence1) +1, len(sequence2) +1)) #stores most optimal path
for i in range(len(sequence1)+1): #want to fill in first column with gap penalty. range gives us indices. want to loop through indices in first row. 
	F_matrix[i,0] = i*gap_penalty #set equal to i times gap penatly. filing in first row. 
for j in range(len(sequence2)+1):
	F_matrix[0,j] = j*gap_penalty #set equal to j times gap penatly. filling in first column
#this is where yhou are actually filling in the matrix i is row j is column
for i in range(1, len(sequence1)+1): # loop through rows starting with second row.
    for j in range(1, len(sequence2)+1): # loop through columns. within reach row want to loop through each column
        row = dic[sequence1[i-1]]
        column = dic[sequence2[j-1]]
        the_score = score[row,column]
        d = F_matrix[i-1, j-1] + the_score
        h = F_matrix[i,j-1] + gap_penalty 
        v = F_matrix[i-1,j] + gap_penalty 

        F_matrix[i,j] = max(d,h,v) #fill matrix with whichever one was the best (highest)
        if F_matrix[i,j] ==d:
            trace_matrix[i,j] =0 #populate trace matrix with 0 for choosing d
        elif F_matrix[i,j] ==h:
            trace_matrix[i,j] =1 #populate trace matrix with 1 for choosing h
        else:
            trace_matrix[i,j] =2 #populated trace matrix with 2 for choosing v

#create empty strings to add nucleotides to based on our tracebackk matrix
seq1 = ""
seq2 = ""
#this is telling us to start in bottom right corner
i = len(sequence1) 
j = len(sequence2) 
#while loop for trace back matrix 
while i != 0 and j != 0: #while i doesn't equal and j doesn't equal 0,0 (top left corner position)
#look in box [i,j] and see what instruction are
    direction = trace_matrix[i,j] #set variable direction as whatever is in the matrix
#If diag: take sequence 1 nucleotide at position i take sequnce 2 nucleotide at position j and add both nucleotides to sequences (they are aligned), next position is i-1 j-1 (move diagonally)
    if direction == 0: #if diagonal
        seq1nuc=sequence1[i-1] #take sequence 1 nucleotide at position i from our sequence we read in do i-1 becuase indexing at python starts at 0
        seq2nuc=sequence2[j-1]
        seq1 = seq1nuc + seq1 #adds seq 1 nuc at this positino to seq 1 (going backwards need to add nuc to front)
        seq2 = seq2nuc + seq2 #adds seq2nuc at this positino to seq2
        i = i-1 #setting new i for one row back
        j = j-1 #setting new j for one column back
    elif direction == 1: #if horizontal
        seq1nuc = "-" #seq 1 nuc should be a dash
        sec2nuc = sequence2[j-1]
        seq1 = seq1nuc + seq1
        seq2 = seq2nuc + seq2
        i = i
        j = j-1 #represents horizontal movement
    else: #
        seq1nuc = sequence1[i-1]
        seq2nuc = "-"
        seq1 = seq1nuc + seq1
        seq2 = seq2nuc + seq2
        i = i-1
        j = j
f = open(file_path, "w")
f.write(seq1)
f.write("\n")
f.write(seq2)
f.close()
#print(seq1)
#print(seq2)
#number of occurences of gaps
print('Number of gaps:', seq1.count('-'), seq2.count('-'))   
print(F_matrix[len(sequence1), len(sequence2)]) #print final score