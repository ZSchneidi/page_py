import sys, os

ROOT_PATH = '/<PATH>'
ENV_PATH = ROOT_PATH + '/bin/activate_this.py'
WSGI_PATH = ROOT_PATH + '/project'

activate_this = ENV_PATH
execfile(activate_this, dict(__file__=activate_this))

if WSGI_PATH not in sys.path:
    sys.path = [WSGI_PATH] + sys.path

os.chdir(os.path.dirname(__file__))

sys.stdout = sys.stderr

from app import create_app
application = create_app('production.py')



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
