#app.py
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
#from sklearn.externals import joblib
#import sklearn.external.joblib as extjoblib
import joblib


app = Flask(__name__)
# load the saved model file and use for prediction
logit_model = joblib.load('logit_model.pkl')
knn_model = joblib.load('knn_model.pkl')
svm_model = joblib.load('svm_model.pkl')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    #result_prediction=0
    if request.method == 'POST':
    # receive the values send by user in three text boxes thru request object -> requesst.form.values()
        
        petal_length = request.form['petal_length']
        sepal_length = request.form['sepal_length']
        petal_width = request.form['petal_width']
        sepal_width = request.form['sepal_width']
        model_choice = request.form['model_choice']

        sample_data = [sepal_length, sepal_width, petal_length, petal_width]
        clean_data = [float(i) for i in sample_data]
        print(clean_data)
        final_features = np.array(clean_data).reshape(1,-1)
        
        '''
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        print(final_features)
        model_choice = request.form['model_choice']
'''        
        if model_choice == 'Logistic':
            result_prediction = logit_model.predict(final_features)
    
        elif model_choice == 'KNN': 
            result_prediction = knn_model.predict(final_features)
            
        elif model_choice == 'SVM':
            result_prediction = svm_model.predict(final_features)
            
        return render_template('preview.html', pred= result_prediction)
    

if __name__ == '__main__':
    app.run(debug=False)
