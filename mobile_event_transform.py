#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import json
import requests
data = {
    'token': 'API TOKEN HERE',
    'content': 'report',
    'format': 'csv',
    'report_id': '5094',
    'csvDelimiter': '',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'returnFormat': 'csv'
}
r = requests.post('API URL HERE',data=data)


from io import StringIO
df = pd.read_csv(StringIO(r.text))
df['Today'] = pd.to_datetime("today").normalize()
df['mob_date_1'] = pd.to_datetime(df['mob_date_1'])
df['date_diff'] = (df['mob_date_1'] - df['Today']).dt.days
clean_events = (
    df[df['date_diff'] >= 0].sort_values(by='mob_date_1').drop(columns=['Today', 'date_diff']).to_dict(orient='records')
)


data_load = {
    'record_id': 'Mobile_Events'
}

MAX_EVENTS = 30

for i in range(1, MAX_EVENTS + 1):
    data_load[f'event_{i}_date'] = ''
    data_load[f'event_{i}_location'] = ''
    data_load[f'event_{i}_address'] = ''
    data_load[f'event_{i}_notes'] = ''

for i, event in enumerate(clean_events, start=1):

    data_load[f'event_{i}_date'] = event['mob_date_1'].strftime('%m-%d-%Y')
    data_load[f'event_{i}_location'] = event['mob_loc_1']
    data_load[f'event_{i}_address'] = event['mob_address_1']
    data_load[f'event_{i}_notes'] = event['mob_notes_1']


import_data = {
    'token': 'API TOKEN HERE',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'overwriteBehavior': 'overwrite',
    'forceAutoNumber': 'false',
    'data': json.dumps([data_load]),
    'returnContent': 'count',
    'returnFormat': 'json'
}

import_response = requests.post('API URL HERE', data=import_data)

print(import_response.text)


# In[ ]:




