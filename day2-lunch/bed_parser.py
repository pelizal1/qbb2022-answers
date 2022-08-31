#!/usr/bin/env python3

import sys

def parse_bed(fname):
    # does the file exist
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    # initialize variables
    bed = []
    field_types = [str, int, int, str, float, str, int, int, list, int, list, list]
    malformed = 0
    # read file line by line
    for i, line in enumerate(fs):
        # skip the header
        if line.startswith("#"):
            continue
        # strip the whitespace at the end and separate the fields by tab and put them into the list fields
        fields = line.rstrip().split("\t")
        # set the length of the fields-list
        fieldN = len(fields)
        # There have to be at least 3 fields. bed10 and 11 are not appropriate file types
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed. There are {fieldsN} fields in this line.", file=sys.stderr)
            malformed += 1
            continue
 
        try:
            for j in range(min(len(field_types), len(fields))):    
                # split field 9, 11, and 12 by comma
                if j == 8 or j == 10 or j == 11:
                    fields[j] = field_types[j](fields[j].rstrip(',').split(','))
                    for k in range(len(fields[j])):
                        fields[j][k] = int(fields[j][k])
                else:
                    fields[j] = field_types[j](fields[j])
            # IF blockCount and blockSizes are not equal
            if fields[9] != len(fields[10]):
                print(f"blockSizes doesn't equal blockCount in line {i}", file=sys.stderr)
                print(fields)
                malformed += 1
            # IF blockCount and blockStarts are not equal
            elif fields[9] != len(fields[11]):
                print(f"blockStarts doesn't equal blockCount in line {i}", file=sys.stderr)
                print(fields)
                malformed += 1
            elif j == 8 and len(fields[j]) != 3:
                print("itemRGB doesn't have the correct number of entries", file=sys.stderr) 
                print(fields) 
                malformed += 1
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
            print(fields)
            malformed += 1
    #print out if there are malformed lines
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)        
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    # for z in range(2):
    #     # print entry i
    #     print(bed[z])
        
# Need to add annotations
# Add malformed count
