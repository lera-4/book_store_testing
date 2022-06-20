
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element_by_xpath("//h3[text() ='Selenium Ruby']")
ruby.click()
reviews = driver.find_element_by_css_selector(".reviews_tab > a")
reviews.click()
star = driver.find_element_by_css_selector(".star-5")
star.click()
your_review = driver.find_element_by_id("comment")
your_review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Lera")
email = driver.find_element_by_id("email")
email.send_keys("lera-4@mail.ru")
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()
