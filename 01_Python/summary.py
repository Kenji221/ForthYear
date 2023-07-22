num1 = 1
num2 = 2

# ---------------------------sns Functions ---------------------------
# 箱ひげ図 box plots
import seaborn as sns 
sns.boxplots(data = 'XXX', x = "YYY", y = "ZZZ")
# heatmapでnullの値が何かを調べるためのもの
sns.heatmatp(PDNAME.isnull(),yticklabels = False, xticklabels=False, cmap="crest")


#--------------------------- Matplotlib ---------------------------
import matplotlib.pyplot as plt
plt.figure(figsize=(num1,num2))



#--------------------------- pandas Functions ---------------------------
import pandas as pd
iris=pd.read_csv('iris.csv')
pd.head()
pd.describte()
iris.drop('column',inplace= True , axis = 1)

# 特定のColumnを二進数で表すメソッドとなっている
pd.get_dummies(train['Sex'],drop_first=True)

#--------------------------- scikit_learn ---------------------------
from sklearn.model_selection import train_test_split
#Split the values into train values and test values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Logestic Regresssion
from sklearn.model_selection import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predict = logmodel.predict(X_test)

# K-Nearest Model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

# Standarlize the Parameters
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit()
scaler_features = scaler.transform('DataFrame', axis=1)


# Evaluation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print(classification_report(y_test,predict))
print(confusion_matrix(y_test,predict))

