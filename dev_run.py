# -*- coding: utf-8 -*-
import sys, os
PATH = os.getcwd()
ROOT_PATH = PATH

ENV_PATH = ROOT_PATH + '/ENV_MYPAGE_01/bin/activate_this.py'
WSGI_PATH = ROOT_PATH + '/project'

activate_this = ENV_PATH
execfile(activate_this, dict(__file__=activate_this))

if WSGI_PATH not in sys.path:
    sys.path = [WSGI_PATH] + sys.path

#os.chdir(os.path.dirname(__file__))

sys.stdout = sys.stderr


from app.main import *

app = Main()
app.dev_run()


