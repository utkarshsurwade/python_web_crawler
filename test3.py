from requests import session
import requests
from selenium import webdriver #trying selenium to evade javascript

payload = {
    'username': 'shr.kum.rt15@rait.ac.in',
    'password': 'dypatil@123'
}

url='http://mydy.dypatil.edu/rait/user/files.php'
files = {'repo_upload_file': open('file1.txt','rb')}
values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

multipart_form_data = {
    'repo_upload_': open('file1.txt', 'rb'),
    'submitbutton': ('file1.txt', open('file1.txt', 'rb')),
    'action': ('', 'store'),
    'path': ('', '/')
}

with session() as c:
    #http://mydy.dypatil.edu/rait/login/index.php is contained in action tag
    p1=c.post('http://mydy.dypatil.edu/rait/login/index.php', data=payload) #login
    
    g = c.get('http://mydy.dypatil.edu/rait/user/files.php')
    
    #print(g.text) #checking if login works(works perfectly)
    #r = c.post(url, files=multipart_form_data, data=values)
    #print(r.text)

    browser = webdriver.Firefox()#trying selenium
    browser.get(url)#trying selenium
    print browser.page_source#trying selenium

#test3's trying to upload
