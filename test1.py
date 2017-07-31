import requests
from lxml import html

USERNAME = "shr.kum.rt15@rait.ac.in"
PASSWORD = "dypatil@123"

LOGIN_URL = "http://mydy.dypatil.edu/rait/login/index.php?uname=shr.kum.rt15@rait.ac.in&wantsurl="
URL = "http://mydy.dypatil.edu/rait/my/"

def main():
	session_requests = requests.session()

	# Get login csrf token
	result = session_requests.get(LOGIN_URL)
	tree = html.fromstring(result.text)
	#authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

	# Create payload
	payload = {
		#"username": USERNAME,
		'action': 'login', 
		'password': PASSWORD, 
		#"csrfmiddlewaretoken": authenticity_token
		}
	
	# Perform login
	result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

	# Scrape url
	#resul = session_requests.get(URL, headers = dict(referer = URL))
	#tree = html.fromstring(result.content)
	#bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

	print(result.text)


if __name__ == '__main__':
    main()



#there are no csrf authenticity tokens provided by rait website which are usually provided by many websites
