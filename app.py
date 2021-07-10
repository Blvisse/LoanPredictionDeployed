from flask import Flask,request,render_template,jsonify
import numpy as np
import pickle


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))





@app.route('/time')

def homepage():
    return render_template('homepage.html')




@app.route('/',  methods=['GET', 'POST'])

def predict():
    import pandas as pd

    # gender=request.args.get('Gender')
    # married=request.args.get('Married')
    # dependents=request.args.get('Dependents')
    # education=request.args.get('Education')
    # self_employed=request.args.get('Self_Employed')
    # applicantIncome=request.args.get('ApplicantIncome')
    # coapplicantIncome=request.args.get('CoapplicantIncome')
    # loanAmount= request.args.get('LoanAmount')
    # loanamountTerm=request.args.get('Loan_Amount_Term')   
    # creditHistory=request.args.get('Credit_History')    
    # propertyArea =request.args.get('Property_Area')
    
    data=request.get_json(force=True)
    data.update((X,[y])for X,y in data.items())
    data_DF=pd.DataFrame.from_dict(data)


    # data=pd.DataFrame({'Gender':[gender],'Married':[married],'Dependents':[dependents],'Education':[education],'Self_Employed':[self_employed],'ApplicantIncome':[applicantIncome],'CoapplicantIncome':[coapplicantIncome],'LoanAmount':[loanAmount],'Loan_Amount_Term':[loanamountTerm],'Credit_History':[creditHistory],'Property_Area':[propertyArea],})
    # data.fillna(0, inplace=True)
    print(data_DF)
    prediction=model.predict(data_DF)

    output={'results':int(prediction[0])}

    return jsonify(results=output) 
    # return dependents

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == "__main__":
    app.run(debug=True)