from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os,time
# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

FILES = [f for f in os.listdir("/home/phani/strawberries/images") if  time.strptime(time.ctime(os.path.getctime(f))).tm_hour > 17]
errors = []

for filename in FILES:
    metadata = {'name': filename,'parents' : ['1XAwUBgG2SQ0FHxeTSmiZQmC0dqybzwro']}
    res = service.files().create( body=metadata,
            media_body=filename, fields='mimeType').execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))
    else:
    	errors.append(filename)
    time.sleep(1)
print "upload failed for : ",errors
print "upload failed count : ",len(errors)



# # Call the Drive v3 API
# results = service.files().list(
#     pageSize=10, fields="nextPageToken, files(id, name)").execute()
# items = results.get('files', [])
# if not items:
#     print('No files found.')
# else:
#     print('Files:')
#     for item in items:
#         print('{0} ({1})'.format(item['name'], item['id']))
