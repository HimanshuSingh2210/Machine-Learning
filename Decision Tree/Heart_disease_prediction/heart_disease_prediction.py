# -*- coding: utf-8 -*-
"""Heart_Disease_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2zs8gWKovt2PFVo82_eTjBXFUXP47BH
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
#from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#EDA--
#data analysis-- shape, info(), describe(), dtypes, corr()
#missing value analysis
#outlier analysis
#visualization--

#supervised model building part-- classification model
#independt and depednt data
#divide the data into train and test set
#create your model
#train your model
#test your model-- predict()
#performance of the model-- accuracy score, confusion matrix, classification_report

df = pd.read_csv('/content/heart-1.csv')
df.head()

df.head(10)

df.shape

df.isnull().sum()

#col-- object--- fill the nan values by the mode of the col
#col-- num-- fill the nan values by mean/median

df.dtypes

df.info()

df.corr()

df.columns

df['target'].value_counts()

df[df['chol']>300].value_counts()

df[df['chol']>300].shape

df[df['age']>40].shape

df[(df['chol']>300) & (df['age']>40)].shape

f=df[df['thal']==2]
f.shape

f[f['target']==1].shape

df.shape

df.describe().T

# from sklearn.metrics.pairwise import normalize
df.target.value_counts(normalize =True)*100

df.target.value_counts()

# import seaborn as sns

#left skewed data-- mean, median, mode
#right skewed data-- mode, median, mean

df['age'].hist(grid=True, bins=10);
plt.title('Age distribuition')

"""In the above graph, we can analyse the distribution of Age column, and we can say that there are 60+ people who are having age between 57 to 63."""

#checking
df[(df['age'] >= 57) & (df['age'] <= 63)].shape

sns.distplot(df[df['target']==1]['age'],  label='heart attack yes',kde=False)
sns.distplot(df[df['target']==0]['age'], label='healthy',kde=False)
plt.legend()
plt.title('Density plot of age by sex')
plt.show()

sns.distplot(df[df['target']==1]['age'],  label='heart attack yes',kde=True)
sns.distplot(df[df['target']==0]['age'], label='healthy',kde=True)
plt.legend()
plt.title('Density plot of age by sex')
plt.show()

"""Density graph shows the smoothed distribution of points along the numerical axis. The density peaks where there is the highest concentration of points. In sum, density graphs can be considered smoothed histograms."""

df['trestbps'].hist()
plt.title('Resting Blood pressure distribuition')

sns.distplot(df['trestbps'], bins=10,kde=1)
plt.title('Resting Blood pressure desnity plot');

"""In the above grapgh, we are having a normal distribution"""

fig, axes = plt.subplots(nrows = 1, ncols=2)
sns.boxplot(x='chol', data=df, orient='v', ax=axes[0])
sns.boxplot(x='oldpeak', data=df,  orient='v', ax=axes[1])

cat_feat = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

for list_var in cat_feat:
  sns.countplot(x=list_var, hue='target', data=df)
  plt.show()

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(17,10))
cat_feat = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']

for idx, feature in enumerate(cat_feat):
    if feature != 'target':
        ax = axes[int(idx/4), idx%4]
        # ax = axes[1,2]

        sns.countplot(x=feature, hue='target', data=df,ax=ax)

"""Let's get some insights frm this chart:

Chest pain: the heart desease diagnosis is greater among the patients that feel any chest pain.

Restegc - Eletrocardiagraph results: the rate of heart desease diagnoses higher for patients with a ST-T wabe abnormality .

Slope: The ratio of patients diagnosed with heart desease is higher for slope = 2

Ca: The diagonosed ratio decreases fo ca between 1 and 3.

Thal: the diagnosed ratio is higher for thal = 2.
"""

sns.pairplot(df)

plt.rcParams['figure.figsize'] = (10,8)
sns.countplot(x='target', hue='sex', data=df);
plt.title('Count of target feature by sex')

"""The amount of healthy male people is greater than the amount of unhealthy. For women, the number of unhealthy women is higher."""

df.corr()

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

"""Apparently there are no features with a pretty strong correlation (above |0.7|)"""

plt.rcParams['figure.figsize'] = (8,8)
sns.scatterplot(x='cp', y='thalach', hue='target', size=None, data=df)
plt.title(' CP vs Thalach in rest')

"""As can be seen there is a paitient with high cholesterol. But, there's not a specific division between those that feel pain during exercise practice and those of not feel pain. We can use hue to filter by sex. It's also possible to filter using size = 'label_to_filer'."""

#supervised model building part-- classification model
#independt and depednt data
#divide the data into train and test set
#create your model
#train your model
#test your model-- predict()
#performance of the model-- accuracy score, confusion matrix, classification_report

#df.drop(columns=['target'])
#if you want to take only age value as your independent data
pd.DataFrame(df['age'])

X = df.drop(columns=['target'])#independent variable or feature
y = df['target']#dependent or target value
print(X.shape)
print(y.shape)

# can write in this way as well
# X = df.iloc[:, :-1]#independent variable should always be in a dataframe fromat(2D) data
# y = df['target']#dependent or target value
# print(X.shape)
# print(y.shape)

#x_train-- remaining 70% of x
#y_train-- remaining 70% of y
#x_test-- 30%of x== 30 records from the df and store those values in x_test
#y_test-- 30%of y== 30 records from the df and store those values in y_test

# from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(X,y,random_state=0, test_size=0.3)
print(x_train.shape)
print(x_test.shape)

x_train

y_train

#DecisionTreeRegressor-- work with regression problem

# from sklearn.metrics import accuracy_score,confusion_matrix
# import seaborn as sns
# import matplotlib.pyplot as p

# from sklearn.tree import DecisionTreeClassifier

#decisiontreeclassifier/decisiontreeregressor
clf = tree.DecisionTreeClassifier() #we are creating a decision tree model which is untrained

clf.fit(x_train,y_train) # training the model

#testing the model--= clf.predict(x_train)
y_train_pred = clf.predict(x_train)

y_test_pred = clf.predict(x_test)

len(y_train_pred)

len(y_test_pred)

print(f'Train score {accuracy_score(y_train_pred,y_train)}')
print(f'Test score {accuracy_score(y_test_pred,y_test)}')

# a=90
# print('The value of a is', a,' and that is it')

# print(f'The value of a is {a} and that is it')

# helper function
def plot_confusionmatrix(y_train_pred,y_train,label):
    print(f'{label} Confusion matrix')
    cf = confusion_matrix(y_train_pred,y_train)
    sns.heatmap(cf,annot=True,cmap='Blues', fmt='g')#For g and G , the maximum number of significant digits
    plt.tight_layout()
    plt.show()

plot_confusionmatrix(y_train_pred,y_train,label='Train Data')

plot_confusionmatrix(y_test_pred,y_test,label='Test Data')

#               Actual Values
#predicted       1   0
#             1  TP  FP
#             0  FN  TN

c_parameter_name = 'max_depth'
c_parameter_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,50,75,100,150]
df1= pd.DataFrame(columns=[c_parameter_name, 'accuracy'])
df1

#for the 1st loop, input_parameter will 1
#inside the for loop, it will create a dt model with 1 as the max depth vallue:
#model = tree.DecisionTreeClassifier(max_depth=1)

for input_parameter in c_parameter_values:
    model = tree.DecisionTreeClassifier(max_depth=input_parameter,splitter='best')
    y_pred_train = model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    acc_score = accuracy_score(y_test,y_pred)*100
    # acc_score_train = accuracy_score(y_train,y_pred_train)*100
    df1 = df1.append({c_parameter_name : input_parameter , 'accuracy' : acc_score}, ignore_index=True)

df1

#max_depth=3

model = tree.DecisionTreeClassifier(max_depth=3,splitter='best')
model.fit(x_train,y_train)
y_train_pred =model.predict(x_train)
y_test_pred = model.predict(x_test)

accuracy_score(y_test,y_test_pred)*100

accuracy_score(y_train,y_train_pred)*100

plot_confusionmatrix(y_test_pred,y_test,label='Test')

from sklearn.metrics import classification_report

print(classification_report(y_test_pred,y_test))

#recall->tp / (tp + fn)
#The recall is the measure of our model correctly identifying True Positives.
#Thus, for all the customers who actually have heart disease, recall tells us how many we correctly identified as a heart patient.

#precision of class 0 = TP of class 0/total number of object
#What is the Precision for our model? Yes, it is 0.843 or, when it predicts that a patient has heart disease, it is correct around 84% of the time.
#precision of class 1 = TP of class 1/total number of object

#macro average = (precision of class 0 + precision of class 1)/2

#weighted average is precision of all classes merge together
#weighted average = (TP of class 0 + TP of class 1)/(total number of class 0 + total number of class 1)

#F1-score is a measure of a model's accuracy on a dataset
#a good F1 score means that you have low false positives and low false negatives,
#Accuracy is used when the True Positives and True negatives are more important while
#F1-score is used when the False Negatives and False Positives are crucial.
#Support is the number of actual occurrences of the class in the specified dataset.

