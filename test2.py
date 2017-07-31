from requests import session

payload1 = {
    #'next': 'Next',
    'username': 'shr.kum.rt15@rait.ac.in',
    'password': 'dypatil@123'
}

payload2 = {
    'action': 'login',
    #'username': 'shr.kum.rt15@rait.ac.in',
    'password': 'dypatil@123'
}

with session() as c:
    r=c.post('http://mydy.dypatil.edu/rait/login/index.php', data=payload1)
    
    #response = c.get('')
    print(r.text)

#test2's login works perfectly
