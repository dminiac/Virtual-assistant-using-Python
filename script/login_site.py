from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
from getpass import getpass



def login_site(user,pwd,site):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    avai_site=[["https://www.codechef.com/","edit-name","edit-pass"],
    ["https://www.facebook.com/","email","pass"],
    ["https://www.hackerrank.com/auth/login","input-1","input-2"],
    ["https://codeforces.com/enter?back=%2Fprofile%2Flogin","handleOrEmail","password"],
    ["https://www.linkedin.com/login","username","password"]]
    driver.get(avai_site[site][0]) 
    print ("Opened "+(avai_site[site][0].split("www."))[1].split(".")[0]) 
    sleep(1) 
    username_box = driver.find_element_by_id(avai_site[site][1]) 
    username_box.send_keys(user) 
    print ("Email Id entered") 
    sleep(1)  
    password_box = driver.find_element_by_id(avai_site[site][2]) 
    password_box.send_keys(pwd) 
    print ("Password entered") 
    password_box.submit()
    input()
    driver.quit()
    print ("Done") 