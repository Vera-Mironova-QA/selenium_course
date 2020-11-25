from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    input1.send_keys("test")
    input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    input2.send_keys("test")
    input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    input3.send_keys("test")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcom_test_ale = browser.find_element_by_tag_name("h1")
    welcom_text = welcom_test_ale.text

    assert "Congratulations! You have successfully registered!" == welcom_text
finally:
    time.sleep(10)
    browser.quit()
