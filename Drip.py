# https://stackoverflow.com/questions/32189741/sending-json-string-to-cherrypy
import json
import cherrypy
import numpy as np


class Drip(object):
    
    def __init__(self, f, port):
        self.f = f

        class Handler(object):
            
            @cherrypy.expose
            @cherrypy.tools.json_in()
            def default(self):
                raw_data = cherrypy.request.json
                json_data = json.loads(raw_data)
                X_test = [np.array(json_data['X_test'])]
                print(f.predict(X_test))
                return "Success!"
                
        cherrypy.config.update({'server.socket_port':8080})
        cherrypy.quickstart(Handler())