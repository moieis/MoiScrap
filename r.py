
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


    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    import undetected_chromedriver as uc
    from selenium import webdriver
    from selenium_stealth import stealth
    
    options = webdriver.ChromeOptions() 
    options.headless = True
    # options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(executable_path=r'/app/.chrome-for-testing/chromedriver-linux64/chromedriver',options=options)
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








 
    # import undetected_chromedriver as uc
    # from selenium_stealth import stealth


    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"
    # chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument('--headless=new')
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("user-agent={}".format(user_agent))
    # driver = uc.Chrome(executable_path=r'/app/.chrome-for-testing/chromedriver-linux64/chromedriver',options=chrome_options)
    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True
    # )
   
    # ___________________________________________________________________
    
    # chrome_options = webdriver.ChromeOptions()
    # # # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    
    # driver = webdriver.Chrome(executable_path=r'/app/.chrome-for-testing/chromedriver-linux64/chromedriver', chrome_options=chrome_options)
    
    
    
    # 
    
    
    
    
        # import undetected_chromedriver as uc
    import time
    # from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    
    # Setup the WebDriver (e.g., ChromeDriver)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ######################################################################NOWNWWWWWW########################################
    
    # options = webdriver.ChromeOptions() 
    # options.headless = True
    # # options.add_argument("start-maximized")
    # options.add_argument("--no-sandbox")
    # options.add_argument('--headless=new')
    # options.add_argument("--disable-dev-shm-usage")
    # # options.add_argument("window-size=1400,600")
    # # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # options.add_experimental_option('useAutomationExtension', False)
    # # driver = uc.Chrome(options=options)
    # driver = webdriver.Chrome(options=options)
    driver.get("https://zefoy.com/")
    
    
    
    # Define the coordinates you want to click on
    x_coord = 54
    y_coord = 290
    
    
    
    # Cleanup: close the browser
    time.sleep(10)
    print('screen after 10 sec')
    
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(7)
    print('start')
    time.sleep(6)
    print('did')
    # Create an instance of ActionChains
    actions = ActionChains(driver)
    
    
    # Move to the specified coordinates and click
    actions.move_by_offset(x_coord, y_coord).click().perform()
    time.sleep(2)
    print('screen after click')
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    
    a=driver.find_element(By.XPATH,'/html')
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    time.sleep(3)
    put_image(s)
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(2)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(2)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(2)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(2)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(30)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    actions.move_by_offset(x_coord, y_coord).click().perform()
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    time.sleep(3)
    actions.move_by_offset(x_coord, y_coord).click().perform()
    time.sleep(15)
    a=driver.find_element(By.XPATH,'/html')
    a.screenshot('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png')
    time.sleep(3)
    s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()
    put_image(s)
    
    # s=open('lfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.png','rb').read()





# ################################################################################################################
##################################################################################################################
###########################################################################################################
    # url="https://homedecoratione.com/"
    # driver.get(url)
    # time.sleep(7)
    # a=driver.find_element(By.XPATH,'/html')
    # html = driver.page_source
    # time.sleep(2)
    # put_text(html)

    # a.screenshot('logoo.png')
    # put_text(a.text)
    # time.sleep(3)
    # s=open('logoo.png','rb').read()
    # time.sleep(3)
    # put_image(s)
    # put_text('sdfsdfdkfjhgkjdhfgkj')
    
    # driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
    
    
    
    
    # sitekey = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('outerHTML')
    # sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1].split('"')[0]
    # print(sitekey_clean)
    # solver = recaptchaV2Proxyless()
    # solver.set_verbose(1)
    # solver.set_key('f4b535a30e5de36c4d3e28e165a9f125')
    # solver.set_website_url(url)
    # solver.set_website_key(sitekey_clean)
    
    # g_response = solver.solve_and_return_solution()
    # if g_response!= 0:
    #     put_text("g_response"+g_response)
    # else:
    #     print("task finished with error"+solver.error_code)

    # driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
    
    # driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
    # driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
    
    # profile=driver.find_element(By.ID,'khalil_vid')
    # profile.send_keys('https://www.tiktok.com/@omarsbshlen?is_from_webapp=1&sender_device=pc')
    
    # time.sleep(3)
    
    # boton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/div[2]/p[6]/input')
    # boton.screenshot('foo.png')
    # boton.click()
    # time.sleep(5)
    # try:
        
    #     reso = driver.find_element(By.XPATH,'//*[@id="kresult"]/div').text
    #     put_text("ff1")
    #     put_text(reso)
    #     put_image('foo.png')
    # except:
    #     reso = driver.find_element(By.XPATH,'//*[@id="kresult"]').text
    #     put_text("ff2")
    #     put_text(reso)
        
        
         
      
    
        
        
    
    
    
    




app.add_url_rule('/tool', 'webio_view', webio_view(man),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(man, port=args.port,debug=True)
