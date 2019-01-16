import time
from selenium import webdriver

def pelayo(browser, telef_number):
    """Pelayo handler"""
    browser.get('http://ssl.webphone.es/pelayo/webphone.htm?w=63&p=&c=true&u=')
    elem = browser.find_element_by_id('inputSrv')
    elem.clear()
    elem.send_keys(telef_number)
    button = browser.find_element_by_id('env')
    button.click()
    return True

def jazztel(browser, telef_number):
    """Jazztel handler"""
    browser.get('https://llamamegratis.es/jazztel/v2/webphone.html?lang=es-ES&isLandingLander=1&typeOrigin=wphFollow&widget=2128')
    cb = browser.find_element_by_xpath("//div[@class='checkbox conditions-check-container']")
    action = webdriver.common.action_chains.ActionChains(browser)
    action.move_to_element_with_offset(cb, 10, 10)
    action.click()
    action.perform()

    elem = browser.find_element_by_id('phoneNumber')
    elem.clear()
    elem.send_keys(telef_number)
    time.sleep(1)
    button = browser.find_element_by_id('env')
    button.click()
    button.click()
    return True

def linea_directa(browser, telef_number):
    """Linea directa Handler"""
    browser.get('https://www.lineadirecta.com/te-llamamos-gratis.html?idServicio=http0026&indVehiculo=H')
    time.sleep(1)
    elem = browser.find_element_by_id('telefono')
    elem.clear()
    elem.send_keys(telef_number)
    time.sleep(1)
    button = browser.find_element_by_xpath("//div[@class='flotaBtn']")
    button.click()
    return True

def cofidis(browser, telef_number):
    """Cofidis handler"""
    browser.get('https://www.cofidis.es/es/contactanos/telefono-cofidis.html')
    time.sleep(1)
    elem = browser.find_element_by_id('mainBlock.telephone')
    elem.clear()
    elem.send_keys(telef_number)
    browser.find_element_by_id('mainBlock.politique:DataEntry').click()
    browser.find_element_by_id('mainBlock.evt-wcbIntegradoEI:link').click()

