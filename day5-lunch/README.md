# QBB 2022 - Day 4  Lunch
##Exercise1
grep -v "Proband_id" aau1043_dnm.csv > dnm_nohead.csv
sort -k 5 -t ',' dnm_nohead.csv > dnm_nohead.sorted.csv 

phase_combined=mother - print for mother
awk 'BEGIN{FS=","; OFS="\t"} {if ($6=="mother") {print $5,$6}}' dnm_nohead.sorted.csv > maternal.tsv

awk 'BEGIN{FS=","; OFS="\t"} {if ($6=="father") {print $5,$6}}' dnm_nohead.sorted.csv > paternal.tsv

uniq -c maternal.tsv > counts_maternal.tsv

---Join the counts tables---
join -1 2 -2 2  counts_paternal.tsv counts_maternal.tsv > joined.tsv

---Convert the Parent Age File to space-separated and Sort---
tr "," " " < parent_age_nohead.csv | sort > parent_age_nohead.tsv

---Add the parental ages---
join -1 1 -2 1 parent_age_nohead.tsv joined.tsv > joined_parent.tsv

##Exercise 2
2. The relationship is significant because the p-value is small.  The size of the relationship is 0.3.
This means that for probands gain a de novo mutation for every 0.3 years the mother is older by the time of birth
3. The relationship between paternal age and inherited mutations is significant and the size is 1.3.
This means that for probands gain a de novo mutation for every 1.3 years the father is older by the time of birth.
6. There is a significant difference between the number of maternally- and paternally-inherited mutations per proband.
Ttest_relResult(statistic=-61.60929763491804, pvalue=1.1245140794572799e-204)
7. There should be about 78 de novo mutations with a father who is 50.5 y/o at the time of birth.