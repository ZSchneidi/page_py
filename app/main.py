# -*- coding: utf-8 -*-

import sys
import gc
import json
import traceback


from bottle import *
from beaker.middleware import SessionMiddleware

class Main():
    
    def __init__(self):
        gc.collect()
            
        self.app = app()
        SimpleTemplate.defaults["get_url"] = self.app.get_url
        self.set_routes()       
 
    def set_routes(self):
        
                        
        @self.app.route('/index')
        @self.app.route('/')
        def index():
			return template('index', request=request)
			
        @self.app.route('/test')
        def index():
			return "Hello INDEX!"
			
        @self.app.route('/assets/<filename:re:.+>', name='assets')
        def static(filename):
            gc.collect()
            return static_file(filename, root='assets')
        
    def dev_run(self):
        self.session_opts = {
            #'session.cookie_expires': True,
            'session.timeout': 3600,
            'session.type': 'file',
            'session.data_dir': './data/session',
            'session.auto': True
        }
        self.app = SessionMiddleware(app(), self.session_opts)
        #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        run(app=self.app,host='localhost', port=8080, debug=True,reloader=True)
    
    def run(self):
        self.session_opts = {
            'session.type': 'memory',
            'session.cookie_expires': True,
            'session.timeout': 1800,
            'session.auto': True
        }
        self.app = SessionMiddleware(app(), self.session_opts)
        NET_INSTANCE.deploy_status = True
        cherrypy.config.update({'environment': 'production',
                        'log.access_file': 'access.log',
                        'log.error_file': 'error.log'
                        })
        #cherrypy.config["tools.encode.on"] = True
        #cherrypy.config["tools.encode.encoding"] = "utf-8"
        
        server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), self.app )
        server.start()
        
        
        
        
        
        
            
