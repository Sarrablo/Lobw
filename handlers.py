import time
from selenium import webdriver



def circulo(driver, telef_num):
    driver.visit("http://www.circulodevidentes.com/te-llamamos/")
    driver.render("circulo0.png")
    driver.at_xpath('.//*[@data-id="rootBtn"]').click()
    time.sleep(1)
    number = driver.at_xpath('.//input[@name="customerPhone"]')
    number.set(telef_num)
    time.sleep(1)
    driver.at_xpath('.//*[@data-id="callBtn"]').click()
    time.sleep(2)
    driver.render("circulo1.png")
    time.sleep(3)
    driver.render("circulo2.png")
    time.sleep(4)
    driver.render("circulo3.png")

def generali(driver, telef_num):
    driver.visit("https://www.generali.es/contacto-generali/te-llamamos")
    time.sleep(1)
    name = driver.at_xpath('.//*[@id="formNavigation:login-form-name"]')
    name.set("Strago")
    phone = driver.at_xpath('.//*[@id="formNavigation:login-form-phone"]')
    phone.set(telef_num)
    driver.at_xpath('.//*[@id="formNavigation:ley"]').click()
    driver.at_xpath('.//*[@id="formNavigation:comunicacionesComerciales"]').click()
    time.sleep(0.5)
    driver.at_xpath('.//*[@id="formNavigation:j_idt92"]').click()
    time.sleep(3)
    driver.render("generali1.png")

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


