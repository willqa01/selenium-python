from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

# Spécifiez le chemin vers le fichier chromedriver.exe (assurez-vous de télécharger la version compatible avec votre version de Chrome)
chrome_driver_path = r"I:\Driver\chromedriver.exe"
 
# Créez une instance du service Chrome
service = Service(chrome_driver_path)

# Créez une instance du navigateur Chrome avec le service
driver = webdriver.Chrome(service=service)

# Accédez à une URL
#driver.get("http://127.0.0.1:5500/test.html")   # direction vers une page web specifique
driver.get("https://www.cash-piscines.com/")
#WebDriverWait.until(EC.visibility_of_element_located((driver.get("https://www.cash-piscines.com/"))))
time.sleep(2)
# Faites d'autres actions avec le navigateur...
#driver.find_element(By.ID, "L2AGLb").click()
#time.sleep(1)
#driver.find_element(By.ID, "APjFqb").send_keys("cash piscines")
#time.sleep(1)
#driver.find_element(By.ID, "APjFqb").submit()
#time.sleep(1)
driver.find_element(By.CLASS_NAME, "mini-action-login").click()
time.sleep(2)
#WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, ""mini-action-login"")))
#WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mini-action-login")))
driver.find_element(By.CSS_SELECTOR, "input[type='email']").click()
time.sleep(2)
#WebDriverWait.until(EC.presence_of_element_located((By.CLASS_NAME, "input-default")))
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("william.bani@it-students.fr")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("william.bani@it-stud")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn-lg").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "search-query").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "search-query").send_keys("bache")
#time.sleep(2)
#driver.find_element(By.CLASS_NAME, "inner").click()
#time.sleep(7)
#driver.find_element(By.CLASS_NAME, "input-field").send_keys("william.bani@it-stud")

#WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, ""mini-action-login"")))
#driver.find_element(By.PARTIAL_LINK_TEXT, "Vidéos").click()
#driver.find_element(By.CSS_SELECTOR, "style").click()
#driver.find_element(By.LINK_TEXT, "xmlns")
#driver.find_element(By.CLASS, "Ylm8Fc YmeD8e").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "xmlns").click()

#logo = driver.find_element(By.CLASS_SELECTOR, "IHxmle")
#logo.find_element(By.TAG_NAME, "FMKtTb UqcIub").click()

#driver.get("https://www.google.fr/search?sca_esv=584875080&q=acheter+un+pull+femme&tbm=vid&source=lnms&sa=X&ved=2ahUKEwiR2IS6rtqCAxXUT6QEHeDYAf8Q0pQJegQIDRAB")
#time.sleep(1)
#driver.find_element(By.ID, "L2AGLb").click()

#driver.find_element(By.ID, "742384653").click()
input()