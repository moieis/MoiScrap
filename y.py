
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
from selenium.webdriver.common.by import By
import time
from deep_translator import GoogleTranslator
from pywebio import config

app = Flask(__name__)

@config(title='MyNews',manifest=True,css_style="""
footer {
 visibility: hidden;
}     

.footer {display:none;}
footer {display:none;}

 
""")

def man():
    T=[]
    put_grid([[None,None,None,put_image("https://png.pngtree.com/template/20190323/ourmid/pngtree-a-letter-triangle-logo-image_81987.jpg",
             width="150px",height="150px"),None,None]])
    put_html("<hr>")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    put_text("done")
    driver.get("https://www.gemeentebest.nl/nieuws/")
    time.sleep(2)
    for i in range(4,11):
                    driver.find_element(By.XPATH,f'//*[@id="content"]/div/div[{i}]/h2/a').text
                    driver.find_element(By.XPATH,f'//*[@id="content"]/div/div[{i}]/h2/a').click()
                    time.sleep(2)
                    T.append(GoogleTranslator(source='auto', target='ar').translate(driver.find_element(By.XPATH,f'//*[@id="content"]/div').text))
                    driver.back()
                    time.sleep(2)




    




    s=0
    for i in T:
    
    
        if (s%2) == 0:
                    put_html(f'''<h3>{i}</h3>''')
                    
        else:
                   
        
                    put_html(f'''
                <h3>{i}</h3>''')
    
        put_html('<hr>')
    
        s+=1
      
    
        
        
    
    
    
    




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
