#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, list, int, list, list]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        # There have to be at least 3 fields. bed10 and 11 are not appropriate file types
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            print(f"Line {i} appears malformed.", file=sys.stderr)
            continue
         
                
                 
        
        try:
            for j in range(min(len(field_types), len(fields))):    
                # split field 9, 11, and 12 by comma
                if j == 8 or j == 10 or j == 11:
                    fields[j] = field_types[j](fields[j].rstrip(',').split(','))
                else:
                    fields[j] = field_types[j](fields[j])
                    # IF blockCount and blockSizes are not equal
                if fields[9] != len(fields[10]):
                         print(f"blockSizes doesn't equal blockCount in line {i}", file=sys.stderr)
                         print(fields[9])
                         print(len(fields[10]))
                 
                # IF blockCount and blockStarts are not equal
                if fields[9] != len(fields[11]):
                    print(f"blockStarts doesn't equal blockCount in line {i}", file=sys.stderr)
                if j == 10 or j == 11:
                    fields[j].rstrip(",")
                if j == 8 and len(fields[j]) != 3:
                    print("itemRgb doesn't have the correct number of entries", file=sys.stderr)       
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    for z in range(2):
        # print entry i
        print(bed[z])
