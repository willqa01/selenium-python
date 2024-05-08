from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Spécifiez le chemin vers le fichier chromedriver.exe (assurez-vous de télécharger la version compatible avec votre version de Chrome)
chrome_driver_path = r"I:\Driver\chromedriver.exe"
 
# Créez une instance du service Chrome
service = Service(chrome_driver_path)

# Créez une instance du navigateur Chrome avec le service
driver = webdriver.Chrome(service=service)

# Accédez à une URL
driver.get("http://127.0.0.1:5500/test.html")   # direction vers une page web specifique
#driver.get("https://www.google.fr")

# Faites d'autres actions avec le navigateur...

driver.find_element(By.NAME, "gender").click()
driver.find_element(By.NAME, "gender").click()

driver.find_element(By.ID, "fname").clear()
test3 = driver.find_elements(By.ID, "fname")
for a in test3:
    a.send_keys("w")
    time.sleep(2)
    a.send_keys("i")
    time.sleep(5)
    a.send_keys("l")
    time.sleep(7)
    a.send_keys("l")
    time.sleep(2)
    a.send_keys("y")

test = driver.find_elements(By.CLASS_NAME, "information")
#test.send_keys("admin@localhost.dev")
#for i in test:
    #i.send_keys("Bonjour")
    #time.sleep(2)


driver.find_element(By.ID, "lname").clear()
test2 = driver.find_elements(By.ID, "lname")
for y in test2:
    y.send_keys("D")
    time.sleep(2)
    y.send_keys("T")
    time.sleep(5)
    y.send_keys("C")
    time.sleep(7)
    y.send_keys("    ")
    time.sleep(2)
    y.send_keys("merci")


driver.find_element(By.NAME, "newsletter").click()
#driver.find_element(By.ID, "top").click()
#driver.find_element(By.ID, "will").click()

# Fermez le navigateur à la fin      
input()     #driver.quit() 

