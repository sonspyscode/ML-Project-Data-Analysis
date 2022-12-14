# -*- coding: utf-8 -*-
"""Tubes1-ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xx9DSxSYfehj3WDCVVhyrZvvDfxZZI1L
"""

import pandas as pd
import numpy as np

data1 = pd.read_csv("kendaraan_test.csv")

data1

data2 = pd.read_csv("kendaraan_train.csv")

data2

data = pd.concat([data1,data2],ignore_index = True) #gabungin data

data

data.keys()

data.describe()

data.info()

data.isnull().sum()

print((data['Jenis_Kelamin'].unique()))

data = data.dropna()

data

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
data['Jenis_Kelamin'] = LE.fit_transform(data['Jenis_Kelamin'])
print(LE.classes_)
print(np.sort(data['Jenis_Kelamin'].unique()))
print('')

data

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
data['Umur_Kendaraan'] = LE.fit_transform(data['Umur_Kendaraan'])
print(LE.classes_)
print(np.sort(data['Umur_Kendaraan'].unique()))
print('')

data

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
data['Kendaraan_Rusak'] = LE.fit_transform(data['Kendaraan_Rusak'])
print(LE.classes_)
print(np.sort(data['Kendaraan_Rusak'].unique()))
print('')

data



from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_copy = data.copy()
data = scaler.fit_transform(data)

df = pd.DataFrame(data)

df

import matplotlib.pyplot as plt
import seaborn as sns
f, ax = plt.subplots( figsize=(20,20) )
sns.heatmap(df.corr(),annot=True,linewidths=1)
plt.show()

X = df.iloc[:, [1, 9]].values

m=X.shape[0] #number of training examples
n=X.shape[1] #number of features.
n_iter=3

m

n

X

K=4 # number of clusters

import numpy as np
Centroids= np.array([]).reshape(n,0)

import random as rd
for i in range(K):
    rand=rd.randint(0,m-1)
    Centroids=np.c_[Centroids,X[rand]]

output = {}

for i in range(n_iter):
     #step 2.a
      EuclidianDistance=np.array([]).reshape(m,0)
      for k in range(K):
          tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
          EuclidianDistance=np.c_[EuclidianDistance,tempDist]
      C=np.argmin(EuclidianDistance,axis=1)+1
     #step 2.b
      Y={}
      for k in range(K):
          Y[k+1]=np.array([]).reshape(2,0)
      for i in range(m):
          Y[C[i]]=np.c_[Y[C[i]],X[i]]
     
      for k in range(K):
          Y[k+1]=Y[k+1].T
    
      for k in range(K):
          Centroids[:,k]=np.mean(Y[k+1],axis=0)
      Output=Y

plt.scatter(X[:,0],X[:,1],c='black',label='unclustered data')
plt.xlabel('Umur')
plt.ylabel('Lama Berlangganan')
plt.legend()
plt.title('Plot of data points')
plt.show()

color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(K):
    plt.scatter(Output[k+1][:,0],Output[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(Centroids[0,:],Centroids[1,:],s=300,c='yellow',label='Centroids')
plt.xlabel('Umur')
plt.ylabel('Lama berlangganan')
plt.legend()
plt.show()

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'random', random_state = 18)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()