import pandas as pd
import numpy as np

csv = pd.read_csv('Salaries.csv')
mean = csv.groupby('Year')['BasePay'].mean()

top5 = csv['JobTitle'].value_counts().head(5)
print(top5)

one = sum(csv[csv['Year']==2013]['JobTitle'].value_counts()==1)
print(one)

