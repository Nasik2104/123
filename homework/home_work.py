import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
 
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('E:\\python_work\\wwork\\16_07\\creds.json', scope)
client = gspread.authorize(creds)
 
data = client.open_by_key("12QLk3yWwbmufeR8pmfszM3TDonA9zV-trMDpBZNaXEY")

print(data)

spreadsheet_name = 'sheets'
worksheet_name = 'sheet2'

spreadsheet = client.open(spreadsheet_name)

worksheet_exists = worksheet_name in [worksheet.title for worksheet in spreadsheet.worksheets()]

if worksheet_exists:
    worksheet = data.worksheet(worksheet_name)
       
else:
    worksheet = data.add_worksheet(title=worksheet_name, rows=100, cols=100)

def write():
    data_for_write = {
        "Місяць":['Березень','Квітень','Травень','Червень','Липень'],
        "Годин на навчання":[10, 12, 11, 0, 0],
        "Годин на хоббі":[5,6,7,8,9]

    }

    df = pd.DataFrame(data_for_write)

    cell_range = f'A1:{chr(ord("A") + len(df.columns) - 1)}{len(df) + 1}'

    data = [df.columns.tolist()] + df.values.tolist()

    worksheet.update(cell_range, data)

write()

print(data)

