import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
import datetime
from tornado.options import define, options
import time

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/mainsocket", MainSocketHandler)
        ]
        settings = dict(
            cookie_secret="Oatmeal_Pistachio_Butterscotch_Rum_Raisin",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("awsnap_demo.html")
class MainSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    def open(self):
        MainSocketHandler.waiters.add(self)
        tornado.ioloop.IOLoop.current().add_timeout(datetime.timedelta(seconds=1),self.render)
    def on_close(self):
        MainSocketHandler.waiters.remove(self)
    def render(self):
        print("Sending render command")
        self.write_message({'id': str(uuid.uuid4())})
        tornado.ioloop.IOLoop.current().add_timeout(datetime.timedelta(seconds=1),self.render)
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
