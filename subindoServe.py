import unittest
from appium import webdriver
import time 
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait


def aguarde(elemento, tempo = 10):
        # Objetivo: Aguarda a presença de um elemento com base no seu ID.
        element = WebDriverWait(driver, tempo).until(expected_conditions.presence_of_element_located((By.XPATH, elemento)))
        return element

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'ce011711dcd5671c05'
#desired_caps['browserName'] = 'Chrome'
desired_caps['appPackage'] = 'com.instagram.android'
                             
desired_caps['appActivity'] =  'com.instagram.android.activity.MainTabActivity'
                              
#desired_caps['app'] = 'com.instagram.android/.activity.MainTabActivity,android.intent.action.MAIN,NULL,NULL,270532608,com.sec.android.app.launcher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.implicitly_wait(1000)
e = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextSwitcher/android.widget.TextView')
e.click()
e = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Perfil"]/android.widget.ImageView')
e.click()
e = driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_following_count')
e.click()
e = driver.find_element_by_id('com.instagram.android:id/row_search_edit_text').send_keys('ryan.augustoo15')
e = driver.find_element_by_id('com.instagram.android:id/follow_list_username').click()
e = driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_followers_count').click()

contador_2 = 0
contador = 1

while(contador_2 != 50):
    print("O WHILE ESTA NO {}".format(contador_2))
    for usuario in range(2, 6):
        try:                                                                                                                                                                                                                                                                                                                   
            el = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'.format(usuario))

            print('O NOME DO USUARIO NO EL TEXT {}'.format(el.text)) 
                                                           
            el3 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView'.format(usuario))
            el3 = el3.text
            print(el3)
                

            if(el3 != 'Seguindo' and el3 != 'Solicitado'and el.text != 'moreira_feeh'):

                print('O CONTADOR ESTÁ NO {}'.format(contador)) 
                print("O USUARIO eh o numero {}".format(usuario))                   
                print('O Nome do usuairo eh {}'.format(el.text))

                if(el.text != ''):

                    actions = TouchAction(driver)
                    actions.tap(el)
                    actions.perform()
            
                    seguidores = driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_followers_count')   
                                                                 
                    seguindo =driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_following_count')

                    seguidores = seguidores.text
                    seguindo = seguindo.text

                    print(seguidores)
                    print(seguindo)
            #-----------------------------algoritmo de limpeza de inteiros
                    if('.' in seguidores): 

                        seguidores = list(filter(lambda palavra: '.' not in palavra ,  seguidores))

                        seguidores = ''.join(seguidores)

                        if('mil' in seguidores):
                            seguidores = seguidores.replace('mil', '000')
                        elif('mi' in seguidores):
                            seguidores = seguidores.replace('mi', '000')    
                        else:
                            pass
                    else:
                        pass 

                    if('.' in seguindo):   

                        seguindo = list(filter(lambda palavra: '.' not in palavra ,  seguindo))

                        seguindo = ''.join(seguindo)

                        if('mil' in seguindo):

                            seguindo = seguindo.replace('mil', '000')

                        elif('mi' in seguidores or 'mi' in seguindo):

                            seguindo = seguindo.replace('mi', '000')    
                        else:
                            pass
                    else:
                        pass 

                    if(',' in seguidores):

                        seguidores = list(filter(lambda palavra: ',' not in palavra ,  seguidores))

                        seguidores = ''.join(seguidores)

                        if('mil' in seguidores):
                            seguidores = seguidores.replace('mil', '00')

                        elif('mi' in seguidores):
                            seguidores = seguidores.replace('mi', '00000')
           
                        else:
                            pass
                    else:
                        pass

                    if(',' in seguindo):

                        seguindo = list(filter(lambda palavra: ',' not in palavra ,  seguindo))

               
                        seguindo = ''.join(seguindo)

                        if('mil' in seguindo):
                    
                            seguindo = seguindo.replace('mil', '00')
                        elif('mi' in seguindo):

                            seguindo = seguindo.replace('mi', '00000')    
                        else:
                            pass
                    if(' ' in seguindo):

                        seguindo = list(filter(lambda palavra: ' ' not in palavra ,  seguindo))

               
                        seguindo = ''.join(seguindo)

                        if('mil' in seguindo):
                    
                            seguindo = seguindo.replace('mil', '000')
                        elif('mi' in seguindo):

                            seguindo = seguindo.replace('mi', '00000')    
                        else:
                            pass
                    if(' ' in seguidores):

                        seguidores = list(filter(lambda palavra: ' ' not in palavra ,  seguidores))

               
                        seguidores = ''.join(seguidores)

                        if('mil' in seguidores):
                    
                            seguidores = seguidores.replace('mil', '000')
                        elif('mi' in seguidores):

                            seguidores = seguidores.replace('mi', '00000')    
                        else:
                            pass                
                    else:
                        pass 


                    seguidores = list(filter(lambda palavra: ' ' not in palavra ,  seguidores))
                    seguindo = list(filter(lambda palavra: ' ' not in palavra ,  seguindo))

                    seguidores = ''.join(seguidores)
                    seguindo = ''.join(seguindo)

        #--------------------------------------------------------------------
                    #elemento com escrito Mensagem '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]'
                    #BOTAO ESCRITO 'Solicitado' em ID = com.instagram.android:id/row_profile_header_button_follow
                    ja_seguindo_1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
                    print(ja_seguindo_1.text)
        
                    if(ja_seguindo_1.text != 'Mensagem' and ja_seguindo_1.text != 'Solicitado' and ja_seguindo_1.text != 'Seguir de volta'):    
                        if(int(seguindo) > int(seguidores)):
                            e = driver.find_element_by_id('com.instagram.android:id/action_bar_textview_title')
                            e = e.text
                            driver.find_element_by_id('com.instagram.android:id/row_profile_header_button_follow').click()
                
                            file_ = open('Seguidos.txt', 'r')
                            conteudo_txt = file_.readlines()
                
                            conteudo_txt.append('\n'+e)

                            file_.close()    

                            file_ = open('Seguidos.txt', 'w')
                            file_.writelines(conteudo_txt)
                            file_.close() 
                            driver.back()

                        else:
                            driver.back()
                            if(contador == 4):
                                TouchAction(driver).press(x=429, y=1719).move_to(x=450, y=420).release().perform()
        
                                contador = 1
                                contador_2 = contador_2 + 1 
                            else:
                                contador = contador + 1

                    else:
                        
                        driver.back()

                        if(contador == 4):
                            TouchAction(driver).press(x=429, y=1719).move_to(x=450, y=420).release().perform()
        
                            contador = 1
                            contador_2 = contador_2 + 1 
                        else:
                            contador = contador + 1
                
                else:
                    pass

            else:
                
                if(contador == 4):
                    TouchAction(driver).press(x=429, y=1719).move_to(x=450, y=420).release().perform()
        
                    contador = 1
                    contador_2 = contador_2 + 1 
                else:
                    contador = contador + 1
                pass
        except:
            pass
            
           
time.sleep(2)


        

