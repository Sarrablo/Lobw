from datetime import datetime
from selenium import webdriver
import dryscrape
import handlers

class Lobw:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.driver = dryscrape.Session()
        self.telefon_number = None

    def set_objective(self, telefon_number):
        self.number = telefon_number

    def start_attack(self, option=1):
        if self.number == None:
            raise NameError('Number not set')

        #if handlers.pelayo(self.browser, self.number):
        #    print("Pelayo atack {} at {}".format(self.number,
        #                                         str(datetime.now())))
        #if handlers.jazztel(self.browser, self.number):
        #    print("jazztel atack {} at {}".format(self.number,
        #                                         str(datetime.now())))
        #if handlers.linea_directa(self.browser, self.number):
        #    print("Linea Directa atack {} at {}".format(self.number,
        #                                          str(datetime.now())))
        #if handlers.vodafone(self.browser, self.number):
        #    print("Vodafone atack {} at {}".format(self.number,
        #                                               str(datetime.now())))
        #if handlers.circulo(self.driver, self.number):
        #    print("Circulo atack {} at {}".format(self.number,
        #                                          str(datetime.now())))
        if handlers.generali(self.driver, self.number):
            print("Generali atack {} at {}".format(self.number,
                                                   str(datetime.now())))
