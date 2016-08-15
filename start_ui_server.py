import argparse
from tornado.ioloop import IOLoop

from ui_server.application import UIServerApplication


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Start the UI Server")
    parser.add_argument("--port", type=int, default=8888)
    args = parser.parse_args()

    application = UIServerApplication(
        static_path='static',
        template_path='templates'
    )
    application.listen(args.port)
    IOLoop.current().start()
