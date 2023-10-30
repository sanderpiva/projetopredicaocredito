# -*- coding: utf-8 -*-
"""Atividade7 - Export Pickle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b4xj06PEc8PqSE6MZQDF5f7FOj3xtOh1
"""

#!pip install -q scikit-learn==1.3.1
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import datasets
import pickle#exporta modelo ml
import pandas as pd

base=pd.read_csv('C:/Users/Sander/Documents/exe_IA1/IA1_Semana9_exe/atv_7_alternativa2/modelo/credit_risk_dataset.csv')
base.keys()

base.describe()

labels_names = base['loan_status']
pickle.dump(labels_names, open('names.pkl','wb'))
nomesbase = pickle.load(open('names.pkl','rb'))
print(nomesbase)

base=base[['person_age',	'person_income',	'person_emp_length',	'loan_amnt',	'loan_status']]

base.describe()

base.shape

# Remover valores negativos
base = base[base >= 0]

# Remover valores ausentes
base = base.dropna()

# Verificar se não há valores negativos ou valores ausentes
if (base >= 0).all().all():
    print("Não há valores negativos e nem valores missing no DataFrame.")
else:
    print("O DataFrame ainda contém valores negativos ou valores missing.")

base[base['person_age']>100]

base[base['person_income']>800000]

base[base['person_emp_length']>55]

base.shape

base = base.drop(base[base['person_age'] > 100].index)

base = base.drop(base[base['person_income'] > 800000].index)

base = base.drop(base[base['person_emp_length'] > 55].index)

base[base['person_age']>100]
base[base['person_income']>800000]
base[base['person_emp_length']>55]

base.describe

base.shape

x = base[['person_age',	'person_income',	'person_emp_length',	'loan_amnt']]
y = base[[	'loan_status']]

#realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)

preditos = clf.predict(x_teste)
print("Preditos:",preditos)
print("Real    :",y_teste)

from sklearn.metrics import accuracy_score
print("Acuracia:", accuracy_score(y_teste,preditos))

pickle.dump(clf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print (model.predict([ [56,150000,5,2000] ]))
#resposta 1:
#21,9600,2,2500
#65,76000,3,35000

#referencia
#https://www.kaggle.com/datasets/laotse/credit-risk-dataset