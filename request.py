import requests
import json

url = 'https://git.heroku.com/loan-prediction-pp.git'


data= {'Gender':1,'Married':1,'Dependents':3,'Education':1,'Self_Employed':0,'ApplicantIncome':340234,'CoapplicantIncome':280456,'LoanAmount':234000,'Loan_Amount_Term':24,'Credit_History':1,'Property_Area':1}

datar=json.dumps(data)

print(requests.post(url,datar))
