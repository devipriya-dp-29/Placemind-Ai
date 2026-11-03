import pandas as pd
import json
df = pd.read_excel('d:/Fix_it_bro_projects/dharani/backend/data/placement_csv.xlsx')
cols = list(df.columns)
data = df.to_dict('records')[:2]
with open('cols.json', 'w') as f:
    json.dump({'cols': cols, 'data': data}, f)
