from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Definindo o navegador
driver = webdriver.Safari()
driver.maximize_window()

# Definindo o tempo de espera implícita
driver.implicitly_wait(10)

# Definindo o site
driver.get('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# Definindo o login e pwd
login = driver.find_element(By.NAME,'session_key')
login.send_keys('Your email')
pwd = driver.find_element(By.NAME,'session_password')
pwd.send_keys('Your password')
pwd.send_keys(Keys.RETURN)

# Esperando a página carregar
sleep(3)

# Entrando no menu de conexões
driver.get('https://www.linkedin.com/mynetwork/')
sleep(10)

# Usando WebDriverWait para esperar o carregamento da página
wait = WebDriverWait(driver, 20)

# Loop para rolar e clicar nos botões
while True:
    connect_buttons = driver.find_elements(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.full-width' )
    if not connect_buttons:
        driver.execute_script("window.scrollBy(0, 100);")
        sleep(3)
        pass  

    for button in connect_buttons:
        button.click()  
        sleep(3)

    # Rolar um pouco para carregar mais botões
    

# Mantém a janela do navegador aberta até que o usuário decida fechá-la
while True:
    user_input = input('Pressione 0 para sair...')
    if user_input == '0':
        break

# Fecha o navegador
driver.quit()
