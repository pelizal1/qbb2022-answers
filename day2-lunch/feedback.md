Great work on the extended bed parser! Your documentation on your current code is also great - when you go back to finish this assignment, it'll be easy to see what each block of code is doing.

I also like your approach to putting all the column reformatting/checking into a try/except block - that's a great idea in case any formatting issues show up in the bed file that would cause errors. I also really like your choice to have one if statement for splitting up columns 9, 11, and 12 into lists - good idea to do all of them at once since they're all lists of integers anyway - and then a separate set of if statements to check whether they're the correct length. I see a lot of people doing each of those columns separately but I like the logical organization of your approach.

It looks like the bed parser itself is complete, so all you have left is to use your bed parser to analyze the hg38 gencode file!
