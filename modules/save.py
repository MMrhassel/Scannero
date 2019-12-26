from hashlib import md5
import os
def Save(URL,SOURCE):
	try:
	    FileName = md5(b"URL").hexdigest()
	    try:
	        os.mkdir("out/"+URL)
	        with open(os.getcwd()+"/out/"+URL+"/"+FileName,'a',encoding="utf-8") as open_file:
	    	    open_file.write(SOURCE)
	    except:
	    	pass
	except Exception as error:
		print(error)
