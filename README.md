#                                                                  MoiScrap !

###### Deploy Selenium And Merge It With PyWebIo = WebApp For Scraping News Web  Count(10)  Then Tr Into Ar Lang


<p align="center">
  <img src="logoo.png" alt="Image Description"  width="200" height="200">
</p>


<style>
.styled-gif {
    width: 300px;
    border: 2px solid blue;
    border-radius: 10px;
}
</style>
<img src="exm.gif" alt="Your GIF description" class="styled-gif" />




---
#### (1) Imports and requirements ;
---
```
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
import numpy
import os
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import argparse
from pywebio import start_server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from deep_translator import GoogleTranslator
from pywebio import config

```
---
#### (2) Start with build the webapp ;
---
```
app = Flask(__name__)

@config(title='MyNews',manifest=True,css_style="""
footer {
 visibility: hidden;
}     

.footer {display:none;}
footer {display:none;}


""")

#Note: We are using the PyWebIo library here. We did not hide the library tag as an example, and we do not recommend imitating it as we do not consider stealing the content.

```



***
#### (3) Function: We inserted the input into Chrome Drive and gave it scripting commands and instructions, while adding the output to our website using PyWebIo ;
---
```
def man():
    T=[]
    put_grid([[None,None,None,put_image("https://png.pngtree.com/template/20190323/ourmid/pngtree-a-letter-triangle-logo-image_81987.jpg",
             width="150px",height="150px"),None,None]])
    put_html("<hr>")
    
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    driver.get("https://www.gemeentebest.nl/nieuws/")
    time.sleep(2)
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

```


___

#### (4) Close the webapp circuit and identify the server ;
---
```




app.add_url_rule('/tool', 'webio_view', webio_view(man),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(man, port=args.port,debug=True)

```


___
