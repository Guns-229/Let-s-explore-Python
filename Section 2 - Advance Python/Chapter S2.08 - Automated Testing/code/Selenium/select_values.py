#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select


WD = webdriver.Firefox()
WD.get("http://localhost:5000/welcome")


sel = WD.find_element_by_css_selector("[id='welcome']")
print(sel)

select = Select(sel)

all_options = [o.get_attribute('value') for o in select.options]
print(all_options)