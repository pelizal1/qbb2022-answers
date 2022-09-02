#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys

filename = sys.argv[1] #set file name as string variable

if len(sys.argv) > 2: #IF the user set the number of lines
    n_lines = int(sys.argv[2]) #user set number of lines
else:
    n_lines = 10 #set number of lines to default

line_list = [] #storage for lines in the file
for line in open(filename): #for every line in the file
    line_list.append(line)

count = -n_lines #negate n_lines to start at n_lines from end    
for j in range(n_lines): #print the desired lines from line_list
    print(line_list[count].strip("\n\r")) #print the line [count] from the end
    count = count + 1 #go to the next line down