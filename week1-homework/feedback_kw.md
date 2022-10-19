# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)
  * It took me a little bit to realize why you have the `start += 1` within the nested for loop in the simulation. While this is great and shows that you have a fantastic grasp on the algorithm/what your code is doing, It would be more readable if you did something like  `coverages[start+j] += 1`
  * If you didn't want a nested for loop, you could use `coverages[start:start+read_length] += 1`
  * I would recommend that you consider writing a function that you call twice (once for 5x and once for 15x) rather than commenting out repetitive, unnecessary code  


3. Question 1.2, 1.4 plotting script(s)

  * personally, rather than passing the `poisson.pmf` function `coverages`, I would have just passed it an array of x-tick-values like [0, 1, 2, 3, 4, ...] so something like `range(0, max(coverages)+1)`


4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * very nice plots --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * very good --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33, you are correct, but note that insertions in the reference are technically deletions in the assembly.

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5; length is end - start + 1; If you're counting from 1 to 10, you're counting 10 numbers, but 10 -1 is only 9.

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
