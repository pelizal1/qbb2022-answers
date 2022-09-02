# QBB 2022 - Day 4  Lunch
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