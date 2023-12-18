import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def normalize_data(data):
    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(data)
    return data_normalized

data_imported = pd.read_csv('data_toexport.csv')

def preprocessing(list):
    list=pd.DataFrame([list],columns=data_imported.columns)
    
    DataAppended=pd.concat([data_imported,list],ignore_index=True)
    data = normalize_data(DataAppended)
    data = data[-1]
    return(data)


clf_normal_dt=None
clf_ProbeAttack_dt=None
clf_Dos_dt=None
clf_U2R_dt=None
clf_R2L_dt=None



def detect_attacks(input_data, normal_model ,dos_model , probe_model , u2r_model , r2l_model ):
    detected_attacks = []
    input_data=[input_data]
    if normal_model.predict(input_data)== 0 :
        detected_attacks.append('Normal')
    else :
        dos_prediction = dos_model.predict(input_data)
        if dos_prediction == 1:
            detected_attacks.append('DoS')

        probe_prediction = probe_model.predict(input_data)
        if probe_prediction == 1:
            detected_attacks.append('ProbeAttack')

        u2r_prediction = u2r_model.predict(input_data)
        if u2r_prediction == 1:
            detected_attacks.append('U2R')

        r2l_prediction = r2l_model.predict(input_data)
        if r2l_prediction == 1:
            detected_attacks.append('R2L')

    return detected_attacks