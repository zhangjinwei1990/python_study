# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 6:33 下午 
# @Author : Hank 
# @Version：V 0.1
# @File : calculate.py
# @desc :

from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '7.1.2'

desired_caps['deviceName'] = 'redmi'

desired_caps['appPackage'] = 'com.android.calculator2'

desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.android.calculator2:id/digit1').click()

driver.find_element_by_id('com.android.calculator2:id/digit9').click()

driver.find_element_by_id('com.android.calculator2:id/del').click()

driver.find_element_by_id('com.android.calculator2:id/digit5').click()

driver.find_element_by_id('com.android.calculator2:id/plus').click()

driver.find_element_by_id('com.android.calculator2:id/digit6').click()

driver.find_element_by_id('com.android.calculator2:id/equal').click()

driver.quit()