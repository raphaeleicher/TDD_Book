from selenium import webdriver

url = 'http://localhost:8000'
browser = webdriver.Firefox()
browser.get(url)
assert 'Django in Firefox' in browser.title
