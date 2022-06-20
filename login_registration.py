from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("lera-4@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("!741@Lera@789%")
time.sleep(15)
register = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row > .woocommerce-Button.button")
register.click()
driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
account = driver.find_element_by_link_text("My Account")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("lera-4@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("!741@Lera@789%")
login = driver.find_element_by_name("login")
login.click()
if driver.find_element_by_link_text("Logout"):
    print("Logout найден")
else:
    print("Logout не найден")
driver.quit()