## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 0 + 0 + 0 + 0 = 6 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

6. Script set up to convert sparse data into square matrix

* you don't need the for loop that you have set up for this; you can do just the following two lines and it will fill in the data for all the different combos of f1, f2, and score:

```
d1_full[d1['F1'], d1['F2']] = d1['score']
d1_full[d1['F2'], d1['F1']] = d1['score']
```


7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

* did you not do this part because d1_full wasn't plotting? Try the approach I outline above for `d1_full` and `d2_full` and I think you'll have more success.

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

* Didn't see this plot

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

* Didn't see this plot

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Didn't see the answer to these heatmap interpretation questions

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)
