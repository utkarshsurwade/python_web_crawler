import requests
url='http://mydy.dypatil.edu/rait/user/files.php'
files = {'upload_file': open('file1.txt','rb')}
values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

r = requests.post(url, files=files, data=values)

#r = requests.post(url, files=files)

print(r.text)


#demo
