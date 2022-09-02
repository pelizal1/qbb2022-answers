#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

fs = np.genfromtxt("joined_parent.tsv", dtype = None,
                    encoding = None,
                    names = ["Proband_id", "Father_age", "Mother_age", "Paternal_count", "father", "Maternal_count", "mother"])

# plot the parent age and number of mutations
# fig, ax = plt.subplots()
# ax.scatter(fs["Maternal_count"], fs["Mother_age"])
# ax.set_xlabel("Number of maternally inherited mutations")
# ax.set_ylabel("Maternal Age")
# plt.title("Maternal Age and Inherited Mutations")
# plt.savefig("ex2_a.png")

# # OLS for association between maternal age and mutations
# mat_model = smf.ols(formula = "Maternal_count ~ 1 + Mother_age", data = fs).fit()
# print(mat_model.summary())
#
# # # OLS for association between paternal age and mutations
# pat_model = smf.ols(formula = "Paternal_count ~ 1 + Father_age", data = fs).fit()
# print(pat_model.summary())

# # histogram of maternal vs paternal mutation counts
fig, ax = plt.subplots()
ax.hist(fs["Maternal_count"], alpha =  0.5, label = "Maternally-inherited mutations")
ax.hist(fs["Paternal_count"], alpha =  0.5, label = "Paternally-inherited mutations")
ax.set_xlabel("Number of mutations")
ax.set_ylabel("Frequency")
plt.legend()
plt.title("Frequency of Paternal and Maternal Mutations")
plt.savefig("ex2_c.png")

# paired t-test maternal vs paternal mutations
# print(stats.ttest_rel(fs["Maternal_count"], fs["Paternal_count"]))

# # predict the number of mutations with 50.5 y/o father
# new_data = fs[0] # select first row of dataframe
# new_data.fill(0) # replace values in row with zeros
# # add in prediction values of interest
# new_data['Father_age'] = 50.5
# # predict
# print(pat_model.predict(new_data))
