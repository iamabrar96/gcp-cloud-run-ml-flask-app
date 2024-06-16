from flask import Flask, request, render_template
import joblib
from sklearn.preprocessing import RobustScaler
app = Flask(__name__)

@app.route("/")
def loadpage():
    return render_template('home.html', query='')

@app.route("/", methods=['POST'])
def predict():
    # Open the model and scaler files in binary mode
    with open("linear_regression_model.joblib", "rb") as model_file:
        model = joblib.load(model_file)
    with open("scaler.joblib", "rb") as scaler_file:
        scaler = joblib.load(scaler_file)
    
    inputQuery1 = float(request.form['query1'])
    inputQuery2 = float(request.form['query2'])
    inputQuery3 = float(request.form['query3'])

    my_data = [[inputQuery1, inputQuery2, inputQuery3]]
    transform_data = scaler.transform(my_data)
    new_data_input = model.predict(transform_data)

    return render_template('home.html', 
                           output1=f'Predicted Ms temperature for given {inputQuery1}Fe-{inputQuery2}Mn-{inputQuery1}Si alloy composition is {new_data_input[0]}',
                           output2='Note : Actual Ms temperature for a given alloy composition is +/- 9 degrees.',
                           query1=request.form['query1'], 
                           query2=request.form['query2'], 
                           query3=request.form['query3'])

if __name__ == "__main__":
    app.run(debug=True)
