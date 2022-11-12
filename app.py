import black76
from flask import Flask, request, jsonify
import pandas as pd

app=Flask(__name__)

def create_app():
    app=Flask(__name__)
    return app

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    """
    HTML form and functionality to upload Excel data
    """
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_csv(f, header=None)
        data_xls.to_csv('data.csv')
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/retrieve",  methods=['GET'])
def retrieve_data():
    """
    Retrieves data from storage and returns option prices as json
    
    Note that the json key describes the input parameters in full,
            price returned is the json value.
    """
    DATA_PATH = 'data.csv'
    res = black76.run(DATA_PATH)
    res_list = {key: res[key].option_price for key in res}
    print(res_list)
    return jsonify(res_list) 
            
if __name__ == "__main__":
    app.run()