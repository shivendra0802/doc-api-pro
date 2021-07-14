# from django.shortcuts import render

# # Create your views here.


# from django.shortcuts import render

# # Create your views here.
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# from rest_framework import serializers
# from rest_framework import response
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView


# # from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
  
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# # driver = webdriver.Remote(
# #         command_executor='http://hub:4444/wd/hub',
# #         # command_executor='http://hub:4444/grid/register',
# #         desired_capabilities=DesiredCapabilities.CHROME,
# #         )
# # driver.maximize_window()

# def call_webdriver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     chrome_options = Options()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--profile-directory=Default')
#     chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')

#     #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver, options=chrome_options")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     return driver




# # Create your views here.
# class CheckLoginAPI(APIView):
    

#     def post(self, request, *arg, **kwargs):
        
#         driver = call_webdriver()
#         # driver = webdriver.Remote("http://hub:4444/wd/hub", DesiredCapabilities.CHROME)
        

#         # driver.maximize_window()
#         # driver.get(f"{request.data.get('urls')}")
#         # element = driver.find_element_by_id("username")
#         # element.send_keys(request.data.get("login"))
#         # sleep(0.2)
        
#         # # try:
#         # dir_path = BASE_DIR / 'chromedriver'
#         # print(dir_path)
#         # # driver = webdriver.Chrome(executable_path=dir_path)
#         # # print("driver", driver)
#         # # /home/development/Desktop/robboproject/chromedriver
        
    

#         driver.maximize_window()
#         driver.get(f"{request.data.get('urls')}")

#         element = driver.find_element_by_id("username")
#         element.send_keys(request.data.get("login"))


#         # element= driver.find_element_by_xpath("//input[@type='text']")
#         # element.send_keys(request.data.get("login"))
        
#         # element = driver.find_element_by_id("password")
#         element= driver.find_element_by_xpath("//*[@type='password']")
#         element.send_keys(request.data.get("password"))

#         # element= driver.find_element_by_xpath("//input[@type='password']")
#         # sleep(0.2)
#         # submit
#         element= driver.find_element_by_xpath("//*[@type='submit']")
        
#         # element = driver.find_element_by_class_name("ebid-btn")
#         action = ActionChains(driver)
#         action.click(on_element = element)

# # perform the operation
#         action.perform()
#         sleep(2)
#         print("Login successfull")
#         return Response({"success": True})

#         # except:
#         #     print("Login Failed")

        

#         # element.click()
#         # if a is not None:
#         #     return Response("login successfull")s
#         #     # 
        
#         # return Response({"success": False})

    
    


    
    
    
from logging import log
from django.conf.urls import url
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# driver = webdriver.Chrome()  
def call_webdriver():
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')

    #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver, options=chrome_options")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver
# driver = webdriver.Chrome(executable_path='/home/development/Downloads/chromedriver')

# driver.maximize_window()


# Create your views here.
class CheckLoginAPI(APIView):
    

    def post(self, request, *arg, **kwargs):
    # def post(self, request,  *kwargs):
    
        all_data = request.data['data']
        print(all_data)

        login_success = 0
        login_failed = 0

        succes_data = []
        
        
        for data in all_data:
            urls = data['urls']
            login = data['login']
            password = data['password']
            login_data = {}

            print(urls, login, password)
            try:
                print('this is the way')
                driver = call_webdriver()
                # driver = RemoteWebDriver.Chrome()
                # driver = webdriver.Remote.Chrome()
                print('how can i solve this')

                # driver.maximize_window()
                
                driver.get(urls)

                # element = driver.find_element_by_id("username")
                element= driver.find_element_by_xpath("//*[@type='text']")
                element.send_keys(login)


                # element= driver.find_element_by_xpath("//input[@type='text']")
                # element.send_keys(request.data.get("login"))
                
                # element = driver.find_element_by_id("password")
                element= driver.find_element_by_xpath("//*[@type='password']")
                element.send_keys(password)

                # element= driver.find_element_by_xpath("//input[@type='password']")
                # sleep(0.2)
                # submit
                element= driver.find_element_by_xpath("//*[@type='submit']")
                
                # element = driver.find_element_by_class_name("ebid-btn")
                action = ActionChains(driver)
                action.click(on_element = element)
        
        # perform the operation
                action.perform()
                sleep(2)
                # wait the ready state to be complete
                WebDriverWait(driver=driver, timeout=10).until(
                    lambda x: x.execute_script("return document.readyState === 'complete'")
                )
                error_message = "Incorrect username or password."
                # get the errors (if there are)
                errors = driver.find_elements_by_class_name("flash-error")
                # print the errors optionally
                # for e in errors:
                #     print(e.text)
                # if we find that error message within errors, then login is failed
                if any(error_message in e.text for e in errors):
                    print("[!] Login failed")
                else:
                    print("[+] Login successful")
            
                # close the driver
                driver.close()
                    
                login_success += 1
                
                login_data["url"] = urls
                login_data['login'] = login
                login_data['password'] = password
                login_data['is_loggedIn'] = True
                succes_data.append(login_data)

            except Exception as e:
                print(e)
                login_failed +=1
                login_data["url"] = urls
                login_data['login'] = login
                login_data['password'] = password
                login_data['is_loggedIn'] = False
                succes_data.append(login_data)
                print("Login Failed")

        

        # element.click()
        # if a is not None:
        #     return Response("login successfull")s
        #     # 
       
        
        return Response({"success-login": login_success, "failed-login":login_failed, "succes-data": succes_data})

    
    


    
    
    










