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
shop = driver.find_element_by_link_text("Shop")
shop.click()
html = driver.find_element_by_css_selector(".post-181 > a >img")
html.click()
if driver.find_element_by_css_selector(".product_title.entry-title"):
    print("HTML5 найдена")
else:
    print("HTML5 не найдена")
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
shop = driver.find_element_by_link_text("Shop")
shop.click()
html = driver.find_element_by_link_text("HTML")
html.click()
products = driver.find_elements_by_css_selector(".attachment-shop_catalog.size-shop_catalog.wp-post-image")
if len(products) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(products)))
driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
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
shop = driver.find_element_by_link_text("Shop")
shop.click()
element = driver.find_element_by_css_selector(".orderby")
option_checked = element.get_attribute("value")
if option_checked == 'menu_order':
    print("Выбран вариант сортировки по умолчанию")
else:
    print("Не выбран вариант сортировки по умолчанию")
select = Select(element)
select.select_by_visible_text("Sort by price: high to low")
element = driver.find_element_by_css_selector(".orderby")
option_checked = element.get_attribute("value")
if option_checked == "price-desc":
    print("Выбран вариант сортировки по цене от большей к меньшей")
else:
    print("Не выбран вариант сортировки по цене от большей к меньшей")
driver.quit()



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
shop = driver.find_element_by_link_text("Shop")
shop.click()
android = driver.find_element_by_xpath("//h3[text()='Android Quick Start Guide']")
android.click()
book_old_price = driver.find_element_by_css_selector("p  > del > span")
book_old_price_text = book_old_price.text
book_new_price = driver.find_element_by_css_selector("p  > ins > span")
book_new_price_text = book_new_price.text
assert book_old_price_text == '₹600.00'
assert book_new_price_text == '₹450.00'
book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()
book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()
driver.quit()



from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
shop = driver.find_element_by_link_text("Shop")
shop.click()
html5 = driver.find_element_by_css_selector(".post-182 > .button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
html5.click()
time.sleep(3)
number = driver.find_element_by_css_selector(".cartcontents")
number_text = number.text
price = driver.find_element_by_css_selector(".wpmenucart-contents >.amount")
price_text = price.text
assert number_text == '1 Item'
assert price_text == '₹180.00'
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
some_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹180.00"))
ome_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal > .woocommerce-Price-amount"), "₹180.00"))
driver.quit()


from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
shop = driver.find_element_by_link_text("Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
html5 = driver.find_element_by_css_selector(".post-182 > .button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
html5.click()
time.sleep(5)
js = driver.find_element_by_css_selector(".post-180 > .button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
js.click()
basket = driver.find_element_by_css_selector(".cartcontents")
basket.click()
time.sleep(5)
delete = driver.find_element_by_xpath("//*[@data-product_id = '182']")
delete.click()
undo = driver.find_element_by_css_selector(".woocommerce-message > a")
undo.click()
quantity = driver.find_element_by_css_selector(".quantity > .input-text.qty.text").clear()
quant = driver.find_element_by_css_selector(".input-text.qty.text")
quant.send_keys(3)
update = driver.find_element_by_xpath("//input[@value = 'Update Basket']")
update.click()
quantity_new = driver.find_element_by_css_selector(" .cart_item:nth-child(1) input")
quantity_new_value = quantity_new.get_attribute("value")
assert quantity_new_value == '3'
time.sleep(5)
apply_coupon = driver.find_element_by_css_selector(".coupon >.button")
apply_coupon.click()
message = driver.find_element_by_css_selector(".woocommerce-error > li")
message_text = message.text
assert message_text == 'Please enter a coupon code.'
driver.quit()


from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
shop = driver.find_element_by_link_text("Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
html5 = driver.find_element_by_css_selector(".post-182 > .button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
html5.click()
time.sleep(10)
basket = driver.find_element_by_xpath("//*[text()='1 item']")
basket.click()
proceed_to_checkout = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
proceed_to_checkout.click()
first_name = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Lera")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Kalashnikova")
email = driver.find_element_by_id("billing_email")
email.send_keys("lera-4@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89057841879")
country = driver.find_element_by_id("select2-chosen-1")
country_russia = driver.find_element_by_id("billing_address_2")
country_russia.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Red square")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("117000")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
option = driver.find_element_by_css_selector("[value='cheque']")
option.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
one_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
two_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details"), "Check Payments"))
driver.quit()
