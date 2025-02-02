import os
import sys
import subprocess

# using bash script to install chromedriver
def install_chromedriver():
    pwd_path = os.getcwd()
    script_path = os.path.join(pwd_path, '00-Functions-resolve-installer.sh')
    if os.path.exists(script_path):
        command = f"bash -c '. \"{script_path}\" && install_chromedriver'"
        subprocess.run(command, shell=True)
    else:
        print("Error: Script '00-Functions-resolve-installer.sh' not found.")

    
# Call the function to install chromedriver
install_chromedriver()


# Add the virtual environment's site-packages to sys.path
site_packages_path = print(sys.prefix)
sys.path.insert(0, site_packages_path)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Vervang 'chromedriver' door het pad naar je chromedriver executable
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Ga naar de downloadpagina
driver.get("https://www.blackmagicdesign.com/support/download/edd40117dc3a424296792d423003eeb1/Linux")

# Klik op de "Download Only" knop
download_button = driver.find_element(By.XPATH, "//button[text()='Download Only']")
download_button.click()

# Wacht even om de pagina te laten laden
time.sleep(2)

# Vind de nieuwe downloadlink (pas de XPATH aan naar de structuur van de pagina)
new_link = driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://swr.cloud.blackmagicdesign.com/DaVinciResolve/v19.1.2/')]")
download_link = new_link.get_attribute('href')

print(download_link)

# Sluit de browser
#driver.quit()
