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


driver.get("https://www.cash-piscines.com/")
#WebDriverWait.until(EC.visibility_of_element_located((driver.get("https://www.cash-piscines.com/"))))
time.sleep(2)
driver.find_element(By.ID, "axeptio_btn_acceptAll").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mini-action-login").click()
time.sleep(2)

#WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mini-action-login")))
driver.find_element(By.CSS_SELECTOR, "input[type='email']").click()
time.sleep(1)
#WebDriverWait.until(EC.presence_of_element_located((By.CLASS_NAME, "input-default")))
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("william.bani@it-students.fr")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("william.bani@it-stud")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "btn-lg").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "search-query").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "search-query").send_keys("jouer")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "visual").click()
time.sleep(1)
#driver.find_element(By.CLASS_NAME, "active-show").click()
driver.find_element(By.CLASS_NAME, "btn-lg").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,"glyphicon-plus").click()
time.sleep(1)
#driver.find_element(By.CLASS_NAME,"pull-left").click()
#time.sleep(2)
driver.find_element(By.CLASS_NAME, "search-query").send_keys("robot")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "picture").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "py-20").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "mini-action-cart").click()
time.sleep(1)
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"lazy loaded")))



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