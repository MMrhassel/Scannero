from hashlib import md5
import os
import re


def Save(URL, SOURCE):
    try:
        FileName = md5(b"URL").hexdigest()
        try:
            URL_FOLDERX = re.sub(
                r'https://www\.|http://www\.|https://www|http://|https://|www\.', "", URL)
            URL_Folder = URL_FOLDERX
            os.mkdir("out/"+URL_Folder)
            with open("out/"+URL_Folder+"/"+FileName, 'a+', encoding="utf-8") as open_file:
                open_file.write(SOURCE)
        except:
            pass
    except:
        pass
