#This file is uploaded under the "Web" tab, under the WSGI configuration file:/var/www/yourUSERNAME_pythonanywhere_com_wsgi.py

import sys

path = '/home/yourUSERNAME/yourWEBSITE/bin/'
	#type in your python anywhere USERNAME
	#type in your python anywhere WEBAPP Folder's name
	#Ex. /home/missmascience/websitev1/bin/
	
if path not in sys.path:
    sys.path.append(path)

from app import app as application
