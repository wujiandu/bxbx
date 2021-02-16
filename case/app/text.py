import os
import unittest
import time
from public.loginApp import Mylogin
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['app'] = PATH('E:/newCourse/zuiyou518.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testshoye01_001(self):
        '''验证游戏界面是否正常显示'''
        Mylogin(self.driver).login()
        time.sleep(6)
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        time.sleep(3)
        aText = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/titile")
        self.assertEqual(aText[6].text,"关注")

    def testshouye01_002(self):
        '''验证滑动功能是否正常'''
        self.driver.implicitly_wait(60)
        aa = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        time.sleep(3)
        self.driver.swipe(300,300,800,600,2000)
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()