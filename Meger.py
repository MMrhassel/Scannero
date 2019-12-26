from requests import get
from modules.save import Save
from sys import stdin
def REQUEST(URLS):
	for URL in URLS:
		URL_ = URL.rstrip()
		try:
		    Response = get(URL_).text
		    Save(URL_,Response)
		except:
			pass

REQUEST(stdin.readlines())
