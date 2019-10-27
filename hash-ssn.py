import hashlib
import sys
inputfile = input("Enter input file:")
outputfile = input("Enter output file:")
ssn_file = open(inputfile, "r")
hash_file = open(outputfile, "w")
for line in ssn_file:
    line = line.strip('\n')
    print(hashlib.sha512(line.encode('utf-8')).hexdigest())
    hash_file.write(hashlib.sha512(line.encode('utf-8')).hexdigest())
    hash_file.write('\n')
ssn_file.close()
hash_file.close()
