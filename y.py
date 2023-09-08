
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
import numpy
import os
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
from selenium import webdriver

app = Flask(__name__)


def man():
    put_text("start")
  

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    put_text("done")
    
    
    








app.add_url_rule('/tool', 'webio_view', webio_view(man),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(man, port=args.port,debug=True)














# if __name__ == '__main__':
#     import argparse
#     from pywebio.platform.tornado_http import start_server as start_http_server
#     from pywebio import start_server as start_ws_server

#     parser = argparse.ArgumentParser()
#     parser.add_argument("-p", "--port", type=int, default=8080)
#     parser.add_argument("--http", action="store_true", default=False,
#                         help='Whether to enable http protocol for communicates')
#     args = parser.parse_args()

#     if args.http:
#         start_http_server(man, port=args.port, debug=False)
#     else:
#         # Since some cloud server may close idle connections (such as heroku),
#         # use `websocket_ping_interval` to  keep the connection alive
#         start_ws_server(man, port=args.port, websocket_ping_interval=30,debug=False)
