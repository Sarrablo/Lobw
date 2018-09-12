from datetime import datetime
from selenium import webdriver
import handlers

class Lobw:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.telefon_number = None

    def set_objective(self, telefon_number):
        self.number = telefon_number

    def start_attack(self, option=1):
        if self.number == None:
            raise NameError('Number not set')

        #if handlers.pelayo(self.browser, self.number):
        #    print("Pelayo atack {} at {}".format(self.number,
        #                                         str(datetime.now())))
        if handlers.jazztel(self.browser, self.number):
            print("jazztel atack {} at {}".format(self.number,
                                                 str(datetime.now())))
