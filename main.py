import time
import re
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class Bidoo():
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.vars = {}

    def bidooLogin(self):
        self.driver.get("https://it.bidoo.com/")
        self.driver.set_window_size(974, 727)
        
        # Aspetta che il pulsante di login sia cliccabile
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login_btn"))
        ).click()
        
        # Aspetta che il campo email sia visibile e interattivo
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "field_email"))
        )
        email_field.send_keys(EMAIL)
        
        # Aspetta che il campo password sia visibile e interattivo
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_field.send_keys(PASSWORD)
        
        # Clicca sul pulsante di login
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btlogin:nth-child(1)"))
        ).click()

    def is_logged_in(self):
        """Verifica se l'utente è loggato controllando la presenza di un elemento visibile solo dopo il login"""
        try:
            # Aspetta che l'elemento che indica il login avvenuto sia visibile (può essere modificato in base al sito)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'divSaldoBidMobile'))
            )
            print("Utente loggato")
            return True  # Login riuscito
        except Exception as e:
            print(f"Errore durante la verifica del login: Utente non loggato")
            return False  # Login fallito
        
    def extract_links_from_file(self, filename):
        """Estrai solo i link dal file di testo, ignorando il testo non URL."""
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        links = []
        for line in lines:
            if self.is_url(line):
                links.append(line)
        return links

    def is_url(self, text):
        """Verifica se la stringa è un URL valido di Bidoo."""
        regex = re.compile(
            r'^(https?://(?:www\.)?(?:it\.)?bidoo\.com(?:[^\s]*)$)', re.IGNORECASE)
        return re.match(regex, text) is not None

    def open_links(self, links):
        """Apre i link uno per uno, aspettando 2-3 secondi tra un link e l'altro."""
        n=1
        linkSize=len(links)
        for link in links:
            self.driver.get(link)
            print(f"Link {n} di {linkSize}")
            n+=1
            time.sleep(2 + (time.time() % 1))  # Pausa casuale tra 2 e 3 secondi
            
    def teardown_method(self, method):
        input("Premi Enter per chiudere il browser...")
        self.driver.quit()

if __name__ == "__main__":
    # Esegui il login
    bidoo = Bidoo()
    bidoo.setup_method(None)
    bidoo.bidooLogin()
    if(not bidoo.is_logged_in()):
        bidoo.teardown_method(None)
        exit()

    #Pausa di 5 secondi
    time.sleep(5)

    # Estrai e apri i link
    links = bidoo.extract_links_from_file('links.txt')
    bidoo.open_links(links)
    
    bidoo.teardown_method(None)
