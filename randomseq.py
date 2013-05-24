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
    print "\"output\" directory created."

if os.path.exists(os.path.join(os.curdir, 'cleanup.sh')):
    os.system("./cleanup.sh")
else:
    print "cleanup.sh was not found in the working directory.",
    print "Enter 'q' to exit or any another key to continue without",
    print "wiping previous output files."
    val = ''
    while not val:
        val = raw_input()
if val is 'q':
    exit(0)

start_time = time.time()

for seq_number in seq_list:
    print "Writing sequence file number", seq_number,
    print "of", args.number_of_seqs

    filename = "s" + str(seq_number) + ".fasta"
    seqfile = open(os.path.join(outputDir, filename), 'w')
    seqfile.write('>\n')
    file_start_time = time.time()

    for line in range(1, lines_per_seq + 1):
        for index in range(1, chars_per_line + 1):
            nt = random.randint(1, 4)
            if(nt == 1):
                seqfile.write('a')
            elif(nt == 2):
                seqfile.write('c')
            elif(nt == 3):
                seqfile.write('t')
            elif(nt == 4):
                seqfile.write('g')
            else:
                seqfile.write('ERR')

        seqfile.write('\n')

    #write last line in file
    for index in range(1, chars_in_last_line + 1):
        nt = random.randint(1, 4)
        if(nt == 1):
            seqfile.write('a')
        elif(nt == 2):
            seqfile.write('c')
        elif(nt == 3):
            seqfile.write('t')
        elif(nt == 4):
            seqfile.write('g')
        else:
            seqfile.write('ERR')
        seqfile.write('\n')

    time_per_file = time.time() - file_start_time
    files_rem = args.number_of_seqs - seq_number
    time_rem = int(time_per_file * files_rem)
    min_rem = int(time_rem / 60)
    sec_rem = int(time_rem % 60)
    os.system('clear')

    if min_rem > 60:
        hours_rem = min_rem / 60
        min_rem = min_rem % 60
        if hours_rem > 24:
            days_rem = int(hours_rem / 24)
            hours_rem = int(hours_rem % 24)
            print "Estimated time remaining:", days_rem, "days",
            print hours_rem, "hours\n"
        else:
            print "Estimated time remaining:", hours_rem, "hours",
            print min_rem, "minutes\n"
    else:
        print "Estimated time remaining:", min_rem, "minutes",
        print sec_rem, "seconds\n"

end_time = time.time()
run_time = end_time - start_time

print ('\a')  # terminal bell
print "\nDone"
print("Execution time: %.2f seconds." % runTime)
