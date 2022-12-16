from flask import Flask, request, render_template
import csv
import joblib
# import numpy as np
# from tensorflow import keras


app = Flask(__name__)
app.debug = True

@app.route("/")
def myapp():
    return render_template('sample.html')


naive_model = joblib.load('assets\\naivebayes_model.joblib')
dectree_model = joblib.load('assets\\decision_tree_model.joblib')
# ann_model = keras.models.load_model('assets\\model.h5')

@app.post('/test2', methods=['POST'])
def upload_csv():
    # model used
    model_class = request.form['model']
    
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        rows = []
        # Check if the file is not empty
        if csv_file.filename != '':
            # Read the file and get the rows as a list of lists
            file_data = csv_file.read().decode('utf-8')
            reader = csv.reader(file_data.splitlines())
            for row in reader:
                rows.append(row)
        
        if model_class == 'naive_bayes' :
            pred = naive_model.predict(rows)
        elif model_class == 'decision_tree' :
            pred = dectree_model.predict(rows)

    return render_template('sample.html',rows=rows, predict=pred)
    
