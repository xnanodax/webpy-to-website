#This file is uploaded under the "File" tab, under the user created folder named "bin"
#file location: /home/yourUSERNAME/yourWEBSITE/bin/app.py

import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())
app = app.wsgifunc()

render = web.template.render('/home/yourUSERNAME/yourWEBSITE/templates/')
	#type in your python anywhere USERNAME
	#type in your python anywhere WEBAPP Folder's name
	#Ex. /home/missmascience/websitev1/templates/

class index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting=greeting)

if __name__ == "__main__":
	app.run()
