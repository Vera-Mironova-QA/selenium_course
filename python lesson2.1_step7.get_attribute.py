from selenium import webdriver
import time
import math

link= 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id('treasure')
    x=x_element.get_attribute('valuex')
    print(x)
    y= calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
