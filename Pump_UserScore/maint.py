import os
import re
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, WebDriverException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
# import numpy as np
# import cv2 #openCV package
address = "https://www.health.kr/searchIdentity/search.asp"
# browser = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
if(getattr(sys,"frozen",False) and hasattr(sys,"_MEIPASS")):
        chromedriver_path = os.path.join(sys._MEIPASS,"chromedriver.exe")
        browser = webdriver.Chrome(chromedriver_path)
else:
    browser = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser.get(address)

incom = []
f=open("Entity01.txt", "a+")
# d = open("test.png,""a+")
while(1):
    try:
        print("success")
        web_element = browser.find_element(By.CLASS_NAME, 'tab3_cont')
        web_element2 = browser.find_element(By.CLASS_NAME, 'popupbx')
        # d.write(web_element2.screenshot_as_png)
        print(web_element.text)
        # if(web_element.text == "로그아웃"):
        #
        #     #############################################
        #     #최근 플레이 데이터 0,1,2가 한 묶음
        #     # browser.get(address + "my_page/recently_played.php")
        #     # web_element_ne = browser.find_element(By.CLASS_NAME,'recently_playeList')
        #     # print(web_element_ne)
        #     # web_element_ne = browser.find_elements(By.CLASS_NAME,'con')
        #     # print(web_element_ne)
        #     #############################################
        #
        #     #############################################
        #     browser.get(address + "my_page/my_best_score.php?&&page=1")
        #     # web_element_bestScore = browser.find_elements(By.CLASS_NAME, 'board_paging')
        #     # web_element_bestScore = browser.find_elements(By.CLASS_NAME, 'icon')
        #     web_element_lastPage = browser.find_element(By.XPATH,'//*[@id="contents"]/div[4]/div/div[2]/div/div/button[7]')
        #     web_element_lastPage.click()
        #     web_element_lastpageindex = browser.find_elements(By.CLASS_NAME,'board_paging')
        #     string = web_element_lastpageindex[0].text.split()
        #     lastpage = string[len(string)-1]
        #
        #
        #     for i in range(int(lastpage)):
        #         addressstring =address + "my_page/my_best_score.php?&&page=" + str(i)
        #         browser.get(addressstring)
        #         indexCheck = browser.find_elements(By.CLASS_NAME, 'song_name')  # text
        #         for index in range(len(indexCheck)-1):
        #             songname = browser.find_elements(By.CLASS_NAME, 'song_name')[index].text
        #             score =browser.find_elements(By.CLASS_NAME, 'num')[index].text
        #             songstep = browser.find_elements(By.CLASS_NAME, 'stepBall_in')[index].find_elements(By.TAG_NAME,"img")[0].get_attribute('src') #싱글더블
        #             songlevel1 = browser.find_elements(By.CLASS_NAME, 'stepBall_in')[index].find_elements(By.TAG_NAME,"img")[1].get_attribute('src') #10의자리 레벨
        #             songlevel2 =browser.find_elements(By.CLASS_NAME, 'stepBall_in')[index].find_elements(By.TAG_NAME,"img")[2].get_attribute('src') #11의자리 레벨
        #             resultAlp = browser.find_elements(By.CLASS_NAME, 'etc_con')[index].find_elements(By.TAG_NAME,'img')[0].get_attribute('src') #랭크 알파벳
        #             resultgameRank = browser.find_elements(By.CLASS_NAME, 'etc_con')[index].find_elements(By.TAG_NAME,'img')[1].get_attribute('src')  # 랭크 알파벳
        #
        #             st = songstep.split("/")
        #             sl1 = songlevel1.split("/")
        #             sl2 = songlevel2.split("/")
        #             ra = resultAlp.split("/")
        #             rr = resultgameRank.split("/")
        #             #싱글 더블 구분
        #             if(st[len(st)-1] == "d_text.png"):
        #                 st = "더블"
        #             else:
        #                 st = "싱글"
        #
        #             #알파벳 랭크 구분
        #             sl1 = sl1[len(sl1)-1].replace('.png','')
        #             sl2 = sl2[len(sl2) - 1].replace('.png', '')
        #             ra = ra[len(ra)-1].replace('.png','')
        #             rr = rr[len(rr) - 1].replace('.png', '')
        #
        #
        #             f.write(songname + "\n")
        #             f.write(score + "\n")
        #             f.write(st + "\n")
        #             f.write(re.sub(r'[^0-9]', '', sl1) + re.sub(r'[^0-9]', '', sl2) + "\n")
        #             f.write(ra + "\n")
        #
        #             print(songname)
        #             print(score)
        #             print(st)
        #             print(re.sub(r'[^0-9]', '', sl1) + re.sub(r'[^0-9]', '', sl2))
        #             print(ra)
        #


            #############################################

            # f.close()
    except UnexpectedAlertPresentException:
        print("알람")
        time.sleep(1)
    except NoSuchElementException:
        print("결과없음")
        continue
    finally:
        print("finally")
        time.sleep(1)

