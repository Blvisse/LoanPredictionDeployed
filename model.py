"""

simple random forest regressor model to predict loan eligibility


"""

import pandas as pd
import numpy as np
import pickle


train=pd.read_csv(r'C:\Users\blais\Desktop\Data Glacier\Task2\DataGlacier\week4\train_ctrUa4K.csv')


def dropNullCols(data):
    print("Deleting in progress")
    data.dropna(inplace=True)

    return data

dropNullCols(train)
# dropNullCols(test)


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

le=LabelEncoder()
oe=OrdinalEncoder()



train['Loan_Status']=train['Loan_Status'].replace({'Y':1,'N':0})
train['Gender']=le.fit_transform(train['Gender'])
train['Education']=le.fit_transform(train['Education'])
train['Dependents']=le.fit_transform(train['Dependents'])
train['Self_Employed']=le.fit_transform(train['Self_Employed'])
train['Property_Area']=le.fit_transform(train['Property_Area'])
train['Married']=le.fit_transform(train['Married'])
train


train.drop(labels=['Loan_ID'],inplace=True,axis=1)


X=train[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']]
y=train['Loan_Status'].values


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,roc_auc_score


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=0)


rf=RandomForestClassifier()

rf.fit(X_train,y_train)

print(rf.score(X_train,y_train))
print(rf.score(X_test,y_test))


predictions=rf.predict(X_test)

print(accuracy_score(y_test,predictions))


pickle.dump(rf,open('model.pkl','wb'))