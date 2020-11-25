from selenium import webdriver
import time
import math


link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    x = browser.find_element_by_id('input_value').text
    x = int(x)
    print(x)
    y= calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    browser.execute_script("window.scrollBy(0, 150);")
    button = browser.find_element_by_tag_name("button.btn")
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()