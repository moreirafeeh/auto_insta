import unittest
from appium import webdriver
import time 
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'ce011711dcd5671c05'
#desired_caps['browserName'] = 'Chrome'
desired_caps['appPackage'] = 'com.detectunfollowers'
                             
desired_caps['appActivity'] =  'com.instagramclient.android.act.MainActivity'
                              
#desired_caps['app'] = 'com.instagram.android/.activity.MainTabActivity,android.intent.action.MAIN,NULL,NULL,270532608,com.sec.android.app.launcher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(100000)

e = driver.find_element_by_id('com.detectunfollowers:id/username').send_keys('moreira_feeh')
 
e = driver.find_element_by_id('com.detectunfollowers:id/password').send_keys('sharingan12345') 

e = driver.find_element_by_id('com.detectunfollowers:id/login').click()

# numero de nao seguem de volta '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.TextView[1]'

#e = driver.find_element_by_id('com.detectunfollowers:id/search_button').click()

e = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Pesquisar"]')

actions = TouchAction(driver)
actions.tap(e)
actions.perform()

                           
e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('lukitsx')


e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('bielzau')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('pomogisebe')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('gustavobantel')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('santix_xx')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('yasminosawa')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.ImageView').click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('anajuliamilani')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.ImageView').click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('vsco')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView').click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('avrillavigne')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()

e = driver.find_element_by_id('com.detectunfollowers:id/search_src_text').send_keys('danrleyoficial_')
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView' ).click()


for i in range(1,10):
    e = driver.find_element_by_id('com.detectunfollowers:id/unfollow_from_top').click()
    driver.find_element_by_id('android:id/button1').click()
    
    

#  botao deixar de seguir 

