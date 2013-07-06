# Generates FASTA-formatted files of randomly-generated nucleotide sequences.
# Number and length of sequence files are chosen by the user.

import random
import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number_of_seqs", type=int,
                    help="the number of sequence files to be created")
parser.add_argument("length_of_seqs", type=int,
                    help="the length of each sequence file")
args = parser.parse_args()

chars_per_line = 50
seq_list = range(1, args.number_of_seqs + 1)
lines_per_seq = int(args.length_of_seqs / chars_per_line)

#last line may have less than 50 characters
chars_in_last_line = int(args.length_of_seqs % chars_per_line)
outputDir = os.path.join(os.curdir, 'output')

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

start_time = time.time()
alphabet = ['a', 'c', 't', 'g']
filename = "sequences.fasta"
seqfile = open(os.path.join(outputDir, filename), 'w')

for seq_number in seq_list:
    print "Writing sequence file number", seq_number,
    print "of", args.number_of_seqs
    seqfile.write('>\n')
    file_start_time = time.time()

    for line in range(1, lines_per_seq + 1):
        for index in range(1, chars_per_line + 1):
           seqfile.write(random.choice(alphabet))
        seqfile.write('\n')

    for index in range(1, chars_in_last_line + 1):
        # Write the last line in the sequence
        seqfile.write(random.choice(alphabet))

run_time = time.time() - start_time

print ('\b')
print "\nDone"
print("Execution time: %.2f seconds." % run_time)
