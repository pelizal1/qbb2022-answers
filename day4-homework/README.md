# QBB2022 - Day 4 Homework Exercises
##A
In the numpy.arange(0.55, 1.05, 0.05), 0.55 represents the inclusive start value, 
1.05 represents the exclusive stop value, and 0.05 represents the step.  For the numpy.around(),
the first argument is the numpy.arange array and the decimals argument spcifies the number of places
to round to. The [::-1] reverses the order of the array.

##C
The number of tosses and power as well as probability and power
are correlated.  

##D
The study is concerned with Mendel's Law of Segregation, which states that children of 
diploid, heterozygous parents inherit either allele at the same rate, in human sperm and 
transmission distortion (TD), which suggests that some alleles are inherited disproportionately
and has been observed in other non-human organisms.

The graphs all follow the same trend with power correlating with tosses and probability in
our experiment and correlating with transmission rate and number of sperm in the paper. The 
probability of heads seems to correspond to the transmission rate axis while the number of
tosses corresponds to the number of sperm. Both simulations use a binomial test because there
are only two conditions: (1) heads or tails or (2) allele1 or allele2.

##Response to feedback
I made a new file (day4-homework) where function is called once rather than repeatedly. As we
spoke about with Jack and through Slack, the results are different from if you call the 
function repeatedly and set the random seed every time.

To be more specific about the correlation, the power increases with increasing probability of heads 
and increasing the number of coin tosses.  