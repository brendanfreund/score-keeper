import glob
import httplib
import os
import tornado
from tornado.web import Application
from models.base import use_db, db_proxy

class UIServerApplication(Application):
    '''Application object that sets up handlers'''

    def __init__(self, *args, **kwargs):
    	use_db()
        handlers = [
            (r"/", LeaderBoardHandler),
        ]
        Application.__init__(self, handlers, *args, **kwargs)


class BaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        db_proxy.connect()
        return super(BaseHandler, self).prepare()

    def on_finish(self):
        if not db_proxy.is_closed():
            db_proxy.close()
        return super(BaseHandler, self).on_finish()


class LeaderBoardHandler(BaseHandler):
    def get(self):
        rounds = [{'player_name':'Steph Curry', 'score':9001, 'date':'August 16, 2016'}]
        self.render("leader_board.html", rounds=rounds)
