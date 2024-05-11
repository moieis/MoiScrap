
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



import telebot



bot = telebot.TeleBot("7199127665:AAHflk6KytAKmxYBnPMssCNkhJO7h9mRRYM")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, " مرحبا بك اسمي موي بوت !!\n قم بارسال رابط حساب الملف الشخصي من التيك تاك لاقوم بسحب البيانات لك \n⚠️ الرجاء عدم الاسائة والسعي للصلاح فلنا ولكم لقاء في يوما تشخص فيه الابصار .....  \n \n\n Hoi, my name is MoiBot :) !!\n*Send me the link of the profile account from tiktak to scrap the data for you. \n⚠️ Please do not offend and strive for goodness, We and you will meet on a day when the eyes will be blinded by the horror of the scene. .....")
    print(message)




def me(message):
    return True
@bot.message_handler(func=me)
def send_welme(message):
    print(message.text[0:4], message)
    if message.text[0:18] in ['http',' htt','https://www.tiktok'] :
        bot.reply_to(message, "⌛⏳")
    
        
    elif len(message.text) == 1:
        bot.reply_to(message, "😝")
    elif len(message.text) == 2:
        bot.reply_to(message, "😝😝")
    elif len(message.text) < 4 or len(message.text) < 3 or len(message.text) < 2:
        bot.reply_to(message, "😆😆😆😆😆")
    
    else:
        bot.reply_to(message, "❌الرجاء ارسال رابط الملف الشخصي يجب ان يبدأ  [https://www.tiktok]❌\n\n\n❌ please enter valid link Must start with [https://www.tiktok]❌")
        
    

bot.infinity_polling()

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
    
    driver.get("https://www.gemeentebest.nl/nieuws/")
    time.sleep(2)
    driver.save_screenshot("image.png")
    dta=open('image.png','rb').read()
    put_image(dta)
    for i in range(4,11):
                    driver.find_element(By.XPATH,f'//*[@id="content"]/div/div[{i}]/h2/a').text
                    driver.find_element(By.XPATH,f'//*[@id="content"]/div/div[{i}]/h2/a').click()
                    time.sleep(2)
                    T.append(GoogleTranslator(source='auto', target='ar').translate(driver.find_element(By.XPATH,f'//*[@id="content"]/div').text))
                    driver.back()
                    time.sleep(2)
                    with use_scope(name="m",clear=True):
                           put_grid([[None,None,None,put_html(f"<h1>{i}</h1>"),None,None]])




    



    driver.close()
    toast("close my mageic cod 012")
    s=0
    for i in T:
     
    
        if (s%2) == 0:
                    put_html(f'''<h5>{i}</h5>''')
                    
        else:
                   
        
                    put_html(f'''
                <h5>{i}</h5>''')
    
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
