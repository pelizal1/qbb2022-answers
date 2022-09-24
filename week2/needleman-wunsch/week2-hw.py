#!/usr/bin/env python
# USAGE: ./week2-hw.py <file.fasta> <scoring_matrix.txt> <gap_penalty>

from fasta import readFASTA
import numpy as np
import sys

# read in parameters
input_sequences = readFASTA(open(sys.argv[1]))
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
gap_penalty = -int(sys.argv[3])

scoring = sys.argv[2]
fs = open(f"{scoring}")

scoring_list = []

for i,line in enumerate(fs):
    row = []
    row = line.split()
    if i == 0:
        row.insert(0,0)
    scoring_list.append(row)

scoring_matrix = np.array(scoring_list)

# initialize F- and traceback matrices
len_1 = len(sequence1) + 1
len_2 = len(sequence2) + 1

F_matrix = np.zeros((len_1, len_2))
traceback_matrix = np.empty((len_1, len_2), dtype=str)

# fill in the first col
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty
    traceback_matrix[i,0] = "v"
# fill in the first row
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penalty
    traceback_matrix[0,j] = "h"


# searching the scoring matrix - make a dictionary with letters as keys
mat_list = scoring_matrix.tolist()
score_dict = {}
for i, item in enumerate(mat_list[0]):
    if i == 0:
        continue
    else:
        score_dict[f"{item}"] = i
   
# populate the F-matrix
for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        seq1 = sequence1[i-1]
        seq2 = sequence2[j-1]
        match_score = scoring_matrix[score_dict[seq1],score_dict[seq2]]
        d = F_matrix[i-1,j-1] + int(match_score)
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        F_matrix[i,j] = max(d,h,v)
        
        if max(d,h,v) == d:
            traceback_matrix[i,j] = "d"
        elif max(d,h,v) == h:
            traceback_matrix[i,j] = "h"
        else:
            traceback_matrix[i,j] = "v"
        


# find the optimal alignment
seq1_align = ""
seq2_align = ""

i = len(sequence1)
j = len(sequence2)

traceback_matrix[0,0] = "e"
score = 0
gap_seq1 = 0
gap_seq2 = 0

while traceback_matrix[i,j] != "e":
    if traceback_matrix[i,j] == "d":
        seq1_align += sequence1[i-1]
        seq2_align += sequence2[j-1]
        score += F_matrix[i,j]
        i -= 1
        j -= 1
    elif traceback_matrix[i,j] == "h":
        seq1_align += "-"
        seq2_align += sequence2[j-1]
        score += F_matrix[i,j]
        gap_seq1 += 1
        j -= 1
    elif traceback_matrix[i,j] == "v": 
        seq1_align += sequence1[i-1]
        seq2_align += "-"
        score += F_matrix[i,j]
        gap_seq2 += 1
        i -= 1

print(f"Alignment score: {score}")
print(f"No. of gaps in sequence 1: {gap_seq1}")
print(f"No. of gaps in sequence 2: {gap_seq2}")
print(f"Sequence 1 alignment: {seq1_align[::-1]}")
print(f"Sequence 2 alignment: {seq2_align[::-1]}")


