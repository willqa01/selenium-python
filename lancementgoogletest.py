from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Spécifiez le chemin vers le fichier chromedriver.exe (assurez-vous de télécharger la version compatible avec votre version de Chrome)
chrome_driver_path = r"D:\Driver\chromedriver.exe"
 
# Créez une instance du service Chrome
service = Service(chrome_driver_path)

# Créez une instance du navigateur Chrome avec le service
driver = webdriver.Chrome(service=service)

# Accédez à une URL
#driver.get("https://www.google.com")   # direction vers une page web specifique

# Faites d'autres actions avec le navigateur...

# Fermez le navigateur à la fin     #driver.quit()   # quite le navigateur  ...
input()

