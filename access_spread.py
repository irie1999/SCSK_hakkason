import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("待ち時間").sheet1

# Extract and print all of the values
rows = sheet.get_all_records()

df = pd.DataFrame.from_records(rows)
print(df)