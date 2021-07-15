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

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

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

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


# Create your views here.
class CheckLoginAPI(APIView):
    

    def post(self, request, *arg, **kwargs):    
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
                driver = call_webdriver()
                driver.get(urls)
                element= driver.find_element_by_xpath("//*[@type='text']")
                element.send_keys(login)

                element= driver.find_element_by_xpath("//*[@type='password']")
                element.send_keys(password)
                element= driver.find_element_by_xpath("//*[@type='submit']")
                
                action = ActionChains(driver)
                action.click(on_element = element)
                action.perform()
                sleep(2)

                WebDriverWait(driver=driver, timeout=10).until(
                    lambda x: x.execute_script("return document.readyState === 'complete'")
                )
                error_message = "Incorrect username or password."
                errors = driver.find_elements_by_class_name("flash-error")
                if any(error_message in e.text for e in errors):
                    print("[!] Login failed")
                else:
                    print("[+] Login successful")
        
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
        
        return Response({"success-login": login_success, "failed-login":login_failed, "succes-data": succes_data})

    
    


    
    
    






