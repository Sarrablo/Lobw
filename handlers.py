
def pelayo(browser, telef_number):
    browser.get('http://ssl.webphone.es/pelayo/webphone.htm?w=63&p=&c=true&u=')
    elem = browser.find_element_by_id('inputSrv')
    elem.clear()
    elem.send_keys(telef_number)
    button = browser.find_element_by_id('env')
    button.click()
    return True

