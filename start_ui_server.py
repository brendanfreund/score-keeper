import argparse
from tornado.ioloop import IOLoop

from ui_server.application import UIServerApplication


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Start the UI Server")
    parser.add_argument("--port", type=int, default=8888)
    args = parser.parse_args()

    application = UIServerApplication(
        static_path='ui_server/static',
        template_path='ui_server/templates'
    )
    application.listen(args.port)
    IOLoop.current().start()
