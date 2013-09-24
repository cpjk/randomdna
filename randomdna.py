# Generates FASTA-formatted files of randomly-generated nucleotide sequences.
# Number and length of sequence files are chosen by the user.

import argparse
import os
import random
import time


parser = argparse.ArgumentParser()
parser.add_argument("number_of_seqs", type=int,
                    help="the number of sequence files to be created")
parser.add_argument("length_of_seqs", type=int,
                    help="the length of each sequence file")
args = parser.parse_args()

def write_line(length, outfile, alphabet):
    for index in range(1, length + 1):
       outfile.write(random.choice(alphabet))
    outfile.write('\n')
    
def write_sequences(args):
    dna = ['a', 'c', 't', 'g']
    line_length = 50
    seq_list = range(1, args.number_of_seqs + 1)
    lines_per_seq = int(args.length_of_seqs / line_length)
    endline_length = int(args.length_of_seqs % line_length)

    output_dir = os.path.join(os.curdir, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = "sequences.fasta"
    outfile = open(os.path.join(output_dir, filename), 'w')    
    
    start_time = time.time()
    for seq_number in seq_list:
        print "Writing sequence file number", seq_number,"of", args.number_of_seqs
        outfile.write('>\n')
        for line in range(1, lines_per_seq + 1):
            write_line(line_length, outfile, dna)
        write_line(endline_length, outfile, dna)
    run_time = time.time() - start_time
    print ('\b\nDone. Execution time: %.2f seconds.' % run_time)
    
if __name__ == "__main__":
    write_sequences(args)
