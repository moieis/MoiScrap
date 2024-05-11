
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
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.recaptchav2proxyless import *



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
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(executable_path=r'/app/.chrome-for-testing/chromedriver-linux64/chromedriver', chrome_options=chrome_options)
    
    
    
    # 
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    
    
    
    url="https://shreateh.net/tiktok-applications/tiktok-osint.html"
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
    
    
    
    
    sitekey = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('outerHTML')
    sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1].split('"')[0]
    print(sitekey_clean)
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key('f4b535a30e5de36c4d3e28e165a9f125')
    solver.set_website_url(url)
    solver.set_website_key(sitekey_clean)
    
    g_response = solver.solve_and_return_solution()
    if g_response!= 0:
        print("g_response"+g_response)
    else:
        print("task finished with error"+solver.error_code)

    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
    
    driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
    
    profile=driver.find_element(By.ID,'khalil_vid')
    profile.send_keys('https://www.tiktok.com/@omarsbshlen?is_from_webapp=1&sender_device=pc')
    
    time.sleep(3)
    
    boton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/div[2]/p[6]/input')
    boton.screenshot('foo.png')
    boton.click()
    time.sleep(5)
    try:
        
        reso = driver.find_element(By.XPATH,'//*[@id="kresult"]/div').text
        put_text("ff1")
        put_text(reso)
        put_image('foo.png')
    except:
        reso = driver.find_element(By.XPATH,'//*[@id="kresult"]').text
        put_text("ff2")
        put_text(reso)
        
        
         
      
    
        
        
    
    
    
    




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
