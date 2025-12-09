import pandas as pd 
import scipy 
#from scipy.stats import chi2_contingecy,ttest_ind

data = {
    'PolicyID': [1,2,3,4,5,6,7,8,9,10],
    'Gender': ['M','F','F','M','M','F','F','M','F','M'],
    'TotalClaims': [0, 1, 0, 0, 2, 0, 1, 0, 1, 0],
    'TotalPremium': [500, 600, 550, 520, 700, 580, 600, 500, 620, 510]
}

df = pd.DataFrame(data)

print(df)