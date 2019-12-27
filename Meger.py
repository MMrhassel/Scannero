import faster_than_requests as requests
from modules.save import Save
from sys import stdin
def REQUEST(URLS):
	for URL in URLS:
		URL_ = URL.rstrip()
		try:
		    Response = requests.get2str(URL_)
		    Save(URL_,Response)
		except:
			pass

REQUEST(stdin.readlines())
