import pandas as pd
%matplotlib inline
tips_data = pd.read_csv('tips.csv')


import pandas.tools.rplot as rplot

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
plt.figure()

import seaborn as sns
g = sns.FacetGrid(tips_data, row = "sex", col = "smoker")
g.map(plt.hist, "total_bill")

