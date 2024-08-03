from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el driver para Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre la URL
driver.get("https://community.secop.gov.co/STS/Users/Login/Index")

# Espera un poco para asegurarte de que la página se cargue completamente
time.sleep(5)

# Realiza acciones en la página, por ejemplo, iniciar sesión
username = driver.find_element(By.ID, "txtUserName")
password = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLoginButton")

username.send_keys("Team2024")
password.send_keys("Team2024+")
login_button.click()

# Espera un poco para asegurarte de que la página siguiente se cargue completamente
time.sleep(5)

# Espera hasta que el menú esté presente y clicable
menu_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='SessionBarWidget']/div[5]/div[1]/div[1]"))
)
menu_button.click()

secop_process= WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((driver.find_element(By.ID, "lnkSubItem4")))
)
secop_process.click()

input("Resuelve el reCAPTCHA manualmente y presiona Enter para continuar...")

secop_process= WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((driver.find_element(By.ID, "btnSearchButton")))
)
secop_process.click()

process_detail = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/table/tbody/tr/td[3]/form/table/tbody/tr[2]/td/table/tbody/tr[6]/td/div[1]/table/tbody/tr[2]/td[9]/a"))
)
process_detail.click()

# Espera hasta que el elemento con el objetivo del proceso esté presente
process_objective = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "divDescriptionDiv_spnDescription"))
)
process_entity = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "BusinessCardCompanyName"))
)
process_number = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "fdsRequestSummaryInfoP2Gen_tblDetail_trRowRef_tdCell2_spnRequestReference"))
)

process_type = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "fdsRequestSummaryInfoP2Gen_tblDetail_trRow5_tdCell2_spnProcedureType"))
)
contract_duration_process = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "fdsObjectOfTheContractP2Gen_tblDetail_trRow4_tdCell2_spnContractDuration"))
)
ending_date_of_the_contract = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "dtmbContractEndDateBoxGen_txt"))
)

# Imprime el texto del objetivo del proceso
print(process_objective.text)
print(process_entity.text)
print(process_number.text)
print(process_type.text)
print(contract_duration_process.text)
print(ending_date_of_the_contract.text)

time.sleep(30)

driver.quit()

# https://www.secop.gov.co/CO1BusinessLine/Tendering/ContractNoticeView/Index?prevCtxLbl=Buscar+procesos&prevCtxUrl=https%3a%2f%2fwww.secop.gov.co%3a443%2fCO1BusinessLine%2fTendering%2fContractNoticeManagement%2fIndex&notice=CO1.NTC.6224113

# https://www.secop.gov.co/CO1BusinessLine/Tendering/ContractNoticeView/Index?prevCtxLbl=Buscar+procesos&prevCtxUrl=https%3a%2f%2fwww.secop.gov.co%3a443%2fCO1BusinessLine%2fTendering%2fContractNoticeManagement%2fIndex&notice=CO1.NTC.6224113

# https://www.secop.gov.co/CO1BusinessLine/Tendering/ContractNoticeView/Index?prevCtxLbl=Buscar+procesos&prevCtxUrl=https%3a%2f%2fwww.secop.gov.co%3a443%2fCO1BusinessLine%2fTendering%2fContractNoticeManagement%2fIndex&notice=CO1.NTC.6223938