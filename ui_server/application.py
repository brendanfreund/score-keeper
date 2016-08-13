import glob
import httplib
import os
import tornado
from tornado.web import Application
import traceback

class UIServerApplication(Application):
    '''Application object that sets up handlers'''

    def __init__(self, *args, **kwargs):
        handlers = [
            (r"/", LeaderBoardHandler),
        ]
        Application.__init__(self, handlers, *args, **kwargs)

class LeaderBoardHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("1963 Rock Leader Board")
