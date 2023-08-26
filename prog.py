import pandas as pd
import requests
from datetime import datetime


file_path = 'Your_Files.xlsx'
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    
    df = pd.DataFrame(columns=['S.No',"(Give ur column names accordingly)"])


def process_row(row):
    expected_result = row['Expected Result']
    endpoints = row['EndPoint'].split(';') 
    
    try:
        for endpoint in endpoints:
            if pd.isnull(row['']) and pd.isnull(row['cols']) and pd.isnull(row['cols']) and pd.isnull(row['cols']):
                response = requests.get(endpoint)
                actual_result = response.text.strip()  
                current_date = datetime.now().strftime('%Y-%m-%d')
                current_time = datetime.now().strftime('%H:%M:%S')
                
               
                new_row = {
                    'S.No': len(df) + 1,
                    'col(1)': '',
                    'col(2)': current_time,
                    'col(3)': current_date,
                    'col(4)': actual_result,
                    'col(5)': expected_result,
                    'EndPoint': endpoint
                }
                
                if actual_result == expected_result or "access denied" in actual_result.lower():
                    new_row['Test Result'] = 'PASS'
                else:
                    new_row['Test Result'] = 'FAIL'
                
                
                df.loc[len(df)] = new_row
        
    except Exception as e:
        print(f"Error processing row {len(df) + 1}: {e}")


for index, row in df.iterrows():
    process_row(row)


df.to_excel(file_path, index=False)