import os
from flask import Flask, request
from analitycs import google_analytics_reporting_api_data_extraction
from analitycs import get_refresh_token
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def ping():
    return '<h1>My flask api Google Analytics running</h1>'




@app.route('/analytics', methods=['POST', 'GET'])
def getUserBrowsers():
    fechaIni= ""
    fechaFin= ""
    tipo = ""
    if request.method == 'POST':
        fechaIni= request.form['fechaIni']
        tipo = request.form['tipo']
        fechaFin = request.form['fechaFin']
        # print(request.form['fechaIni'])
        # print(request.form['fechaFin'])
        # print(request.form['tipo'])
        
   
    
    client_id = '' 
    client_secret = '5uzOPV7GUK56uMrKw0iWpX3q'
    refresh_token = get_refresh_token (client_id, client_secret)
    refresh_token=refresh_token
    viewID='230226059'
    dim=['ga:browser','ga:sourceMedium']
    met=['ga:users','ga:goalXXCompletions']
    start_date= fechaIni 
    end_date= fechaFin
    transaction_type='Goal'
    goal_number='1'
    condition='&sort=-ga%3Ausers' 
    if tipo == 'devices':
        viewID='230226059'
        dim=["ga:deviceCategory"]
        met=["ga:visits"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition=''  
    if tipo == 'usuariosxciudad':
        viewID='230226059'
        dim=["ga:city"]
        met=["ga:users"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition='&sort=-ga%3Ausers' 
        
        
    if tipo == 'nuevosUsuarios':
        viewID='230226059'
        dim=[]
        met=["ga:newUsers"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition=''     
    if tipo == 'usuariosactivoxdia':
        viewID='230226059'
        dim=["ga:date"]
        met=["ga:1dayUsers"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition='' 
        
    if tipo == 'userultimos7dias':
        viewID='230226059'
        dim=["ga:date"]
        met=["ga:users"]
        start_date='7daysAgo'
        end_date='today'
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition=''      
    if tipo == 'referral':
        viewID='230226059'
        dim=["ga:medium","ga:source"]
        met=["ga:users"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition='' 
   
    if tipo == 'usuariosxinifin':        
        viewID='230226059'
        dim=["ga:date"]
        met=["ga:users"]
        start_date=fechaIni
        end_date=fechaFin
        transaction_type='Goal'
        goal_number='1'
        refresh_token=refresh_token
        condition=''  
    # sort the data set by users in descending order

    data=google_analytics_reporting_api_data_extraction(viewID,dim,met,start_date,end_date,refresh_token,transaction_type,goal_number,condition)
    
    df = json.dumps(data)
    #jsons = json.loads(data)
    return data

# if __name__ == '__main__' :
#     # app.run(debug = True, port = 4000 ) 
#     app.run(debug = True, port = 5000 ) 
# #web: gunicorn app:app

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  
    