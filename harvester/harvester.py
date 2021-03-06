# Code written by @Cosm00_ and adapted by @NoahCardoza
# Stay Based Youngins....

import argparse
from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException
import time
import getpass
from os import path

__basedir__ = path.dirname(__file__)


def load_html_template(captcha, sitekey, server):
    with open(path.join(__basedir__, 'html', captcha + '.html')) as f:
        return f.read().replace('{sitekey}', sitekey).replace('{server}', server)


class Harvest:
    def __init__(self, domain, html_template):
        self.chrome = Chrome()
        self.domain = domain.replace('https://', 'http://')
        self.html_code = html_template

    def signin(self, email, password):
        self.chrome.get('https://accounts.google.com/signin/v2')
        while True:
            try:
                emailfield = self.chrome.find_element_by_xpath(
                    '//*[@type="email"]')
                break
            except:
                pass
        while True:
            try:
                emailfield.send_keys(email)
                break
            except:
                pass
        while True:
            try:
                self.chrome.find_element_by_xpath(
                    '//*[text() = "Next"]').click()
                break
            except:
                pass
        while True:
            try:
                passfield = self.chrome.find_element_by_xpath(
                    '//*[@name="password"]')
                break
            except:
                pass
        while True:
            try:
                passfield.send_keys(password)
                break
            except:
                pass
        while True:
            try:
                self.chrome.find_element_by_xpath(
                    '//*[@id="passwordNext"]').click()
                break
            except:
                pass
        while True:
            if 'My Account gives you quick access to settings and tools that let you safeguard your data' in self.chrome.page_source:
                break
            else:
                pass
        self.chrome.get('https://www.youtube.com/watch?v=ZAyvEft9MIs')

    def solve(self):
        self.chrome.get(self.domain)
        try:
            self.chrome.execute_script(
                'document.write(`{}`)'.format(self.html_code))
        except WebDriverException:
            pass
        while True:
            if 'Captcha Token Harvester' in self.chrome.page_source:
                break
            else:
                pass
        time.sleep(1)
        try:
            self.chrome.execute_script(
                "var evt = document.createEvent('Event');evt.initEvent('load', false, false);window.dispatchEvent(evt);")
        except WebDriverException:
            pass
        while True:
            if 'Success' in self.chrome.page_source:
                break
            else:
                pass
