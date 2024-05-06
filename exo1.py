from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Spécifiez le chemin vers le fichier chromedriver.exe (assurez-vous de télécharger la version compatible avec votre version de Chrome)
chrome_driver_path = r"D:\Driver\chromedriver.exe"
 
# Créez une instance du service Chrome
service = Service(chrome_driver_path)

# Créez une instance du navigateur Chrome avec le service
driver = webdriver.Chrome(service=service)

# Accédez à une URL
#driver.get("http://127.0.0.1:5500/test.html")   # direction vers une page web specifique
driver.get("https://www.google.fr")

# Faites d'autres actions avec le navigateur...
driver.find_element(By.ID, "L2AGLb").click()
#time.sleep(1)
driver.find_element(By.ID, "APjFqb").send_keys("cash piscines")
#time.sleep(1)
driver.find_element(By.ID, "APjFqb").submit()
time.sleep(1)
driver.find_element(By.CLASS, "CA5RN").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Vidéos").click()
#driver.find_element(By.CSS_SELECTOR, "style").click()
#driver.find_element(By.LINK_TEXT, "xmlns")
#driver.find_element(By.CLASS, "Ylm8Fc YmeD8e").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "xmlns").click()

#logo = driver.find_element(By.CLASS_SELECTOR, "IHxmle")
#logo.find_element(By.TAG_NAME, "FMKtTb UqcIub").click()

#driver.get("https://www.google.fr/search?sca_esv=584875080&q=acheter+un+pull+femme&tbm=vid&source=lnms&sa=X&ved=2ahUKEwiR2IS6rtqCAxXUT6QEHeDYAf8Q0pQJegQIDRAB")
time.sleep(1)
#driver.find_element(By.ID, "L2AGLb").click()

#driver.find_element(By.ID, "742384653").click()
input()