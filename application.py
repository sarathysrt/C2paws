from flask import Flask
from flask import request, jsonify
import pandas as pd
import numpy as np
import C2P_Core as Dm
import json

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username
	
def hello():
    content = request.get_json()
    data = pd.io.json.json_normalize(content)
    data=np.array(data)
    aDict=Dm.main_Call(data)
    return json.dumps(aDict)

def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    data = pd.io.json.json_normalize(content)
    #data.columns=['Record']#['Time','Record']
    # Peak points
    data=np.array(data)
    #aDict=Dm.Get_PQRS(data)
    aDict=Dm.main_Call(data)
    
    #print (type(content))
    return json.dumps(aDict)#jsonify(content)

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

application.add_url_rule('/getD', 'getD',hello,methods = ['POST'])
# add a rule when the page is accessed with a name appended to the site
# URL.

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()