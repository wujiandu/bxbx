#id 定位
def test_element_by_id01(self):
    #定位‘语玩’控件
    self.driver.implicitly_wait(60)
    el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
    print(el.text)
    el.click()
def test_element_by_id02(self):
    #定位‘贝爷狂野求生’控件
    self.driver.implicitly_wait(60)
    el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/topic_tv")
    print(el.text)
    el.click()
def test_element_by_id03(self):
    #定位‘神评’控件
    self.driver.implicitly_wait(60)
    el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/god_comment_iv_flag")
    print(el.text)
    el.click()
def test_element_by_id04(self):
    #定位右下角‘我的’控件
    self.driver.implicitly_wait(60)
    el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
    print(el.text)
    el.click()
def test_element_by_id05(self):
    #定位‘2063’发表态度控件
    self.driver.implicitly_wait(60)
    el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_atd_count")
    print(el.text)
    el.click()

#class_name 定位
def test_element_by_id(self):
    self.driver.implicitly_wait(60)
    self.driver.find_element_by_class_name("android.widget.ImageView")
    time.sleep(3)
    el = self.driver.find_element_by_class_name("android.widget.ImageView")
    for i in range(0,len(el)):
        print("第"+str(i)+"个是："+el[i].text)
    el[4].click

def test_element_by_id02(self):
    self.driver.implicitly_wait(60)
    self.driver.find_element_by_class_name("android.widget.RelativeLayout")
    time.sleep(3)
    el = self.driver.find_element_by_class_name("android.widget.RelativeLayout")
    for i in range(0,len(el)):
        print("第"+str(i)+"个是："+el[i].text)
    el[2].click

def test_element_by_id03(self):
    self.driver.implicitly_wait(60)
    self.driver.find_element_by_class_name("android.widget.TextView")
    time.sleep(3)
    el = self.driver.find_element_by_class_name("android.widget.TextView")
    for i in range(0,len(el)):
        print("第"+str(i)+"个是："+el[i].text)
    el[6].click

#xpath通过单个ID查找某个元素
el = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']")

#xpath通过id查找多个元素(定位发布话题按钮)
el = self.driver.find_elements_by_xpath("//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/iconTabItem']")

# xpath通过text文本定位，无控件属性
el = self.driver.find_element_by_xpath("//*[@text='游戏']")

# xpath通过text文本定位
el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='视频']")

# xpath 通过class查找某个元素
el = self.driver.find_element_by_xpath("//android.widget.EditText").click()
el = self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").click()

# 组合定位
el = self.driver.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/title" and @text="关注"]').click()

#父级元素定位
el = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView")

