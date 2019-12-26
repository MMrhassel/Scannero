from hashlib import md5
import os
def Save(URL,SOURCE):
	try:
	    FileName = md5(b"URL").hexdigest()
	    try:
                URL_FOLDER = re.sub(r'https://www\.|http://www\.|https://www|http://|https://|www\.', "", URL).strip('/')
	        os.mkdir("out/"+URL_FOLDER)
	        with open("out/"+URL_FOLDER+"/"+FileName,'a+',encoding="utf-8") as open_file:
	    	    open_file.write(SOURCE)
	    except Exception as error:
	    	print(error)
	except Exception as error:
		print(error)
