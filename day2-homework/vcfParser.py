#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0

    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):
        if line.startswith("#"):
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                                elif name == "Type":
                                    Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: # not looking at the header
            try:
                fields = line.rstrip().split("\t") # strip whitespace and split columns of vcf by tab - everything in fields is a string
                fields[1] = int(fields[1]) # make chromosome position an integer
                if fields[5] != ".": # make number a float if it isn't a period
                    fields[5] = float(fields[5])
                info = {} # initializing dictionary to store info
                for entry in fields[7].split(";"): # separate info by semicolon to make a list of strings
                    temp = entry.split("=") # separate the entry by the equal sign to make a list of strings
                    if len(temp) == 1: # IF there's only one item in the list
                        info[temp[0]] = None # give the key a value of none
                    else: # adding the info to info dictionary and converting to the proper data type
                        name, value = temp
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
                fields[7] = info # adding info dictionary to INFO in fields
                if len(fields) > 8: # IF there is a format column
                    fields[8] = fields[8].split(":") # separate format column by colon into a list of strings and overwrite
                    if len(fields[8]) > 1: # IF length is more than 1
                        for i in range(9, len(fields)): 
                            fields[i] = fields[i].split(':') # separate starting in field 9 and up since stuff is already in indeces before that replacing with lists - looking at the format of the human samples
                    else: # format column is only one string entry
                        fields[8] = fields[8][0]
                vcf.append(fields) 
            except: # if any of the code from 70 on failed - the line malformed
                malformed += 1
    vcf[0][7] = info_description # update the vcf list with info from the info line and format desc
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0: # printing if there were any malformed lines
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf

if __name__ == "__main__": # IF the code block is being run on the terminal
    fname = sys.argv[1] # get name of file
    vcf = parse_vcf(fname) # reading in and interpreting vcf file
    # for i in range(10): # print out the first 10 columns
    #     print(vcf[i])