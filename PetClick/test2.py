from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = '../key.json'
SPREADSHEET_ID = '1PrHE2FBeBhQnVYeCLQclLqj_tiIOq7z3JuMAG-2aAXg'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Debe ser una matriz por eso el doble [[]]
values = [['Prueba2!']]
# Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='hoja!A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")