from selenium import webdriver
import time
import random
from selenium.webdriver.common. keys import Keys
import re
from selenium.common.exceptions import NoSuchElementException
#打开浏览器
def browser_open():
    browser = webdriver.Chrome()
    browser.get('https://movie.douban.com/')
    time.sleep(random.random()*4)
    return browser
#处理输入
def select_douban():
    #输入
    urlname = input("请输入电影名（多个请用空格隔开）：")    
    #定义搜索错误的电影名数组
    name_cw = []
    #打开浏览器
    browser = browser_open()
    #add_cookies(browser)#添加缓存
    browser.refresh()#刷新浏览器
    #判断输入是否有空格
    if ' ' in urlname:
        #将输入用空格分隔为列表
        urlname = urlname.split()        
        #定义搜索次数
        b = 0
        #循环输入列表
        for name in urlname:
            #搜索次数相加
            b = b + 1          
            year = name[-4:]            
            #判断输入是否有年份
            if year.isdigit():
                num_year = int(year)
                #判断年份是否合理
                if num_year > 2021 or num_year < 1600:
                    year = '没有找到'
            print(name)            
            #进行搜索
            try:
                search_movie(browser,name,year)  
                print('%s:已完成'%(name))
                time.sleep(2)
            except:
                #错误项加入错误列表
                name_cw.append(name)
                #存入文件
                name_erro = open('data/doubanname_erro.txt','a',encoding='utf-8')
                name_erro.write('%s\n'%(name))      
                name_erro.close()
                print('%s:错误'%(name))
                print(time.time())
                #将错误写入文件，保持顺序正确
                movie_fullname = open('data/doubanurl.txt','a',encoding='utf-8')
                movie_fullname.write('出现错误\n')      
                movie_fullname.close()  
                movie_fulltitle = open('data/doubanname.txt','a',encoding='utf-8')
                movie_fulltitle.write('出现错误\n')      
                movie_fulltitle.close()
                #关闭浏览器并且休息一会打开
                browser.close()
                time.sleep(1600)
                browser = browser_open()
            time.sleep(random.random()*25)
            #每执行100次休息20min
            if b % 100 == 0:
                browser.close()
                time.sleep(1200)            
                browser = browser_open()
            #每执行50次休息1min
            elif b % 50 == 0:
                browser.close()
                time.sleep(60)            
                browser = browser_open()
    #输入单个电影名称
    else:               
        year = urlname[-4:]            
            #判断输入是否有年份
        if year.isdigit():
            num_year = int(year)
            #判断年份是否合理
            if num_year > 2021 or num_year < 1600:
                year = '没有找到'
        try:
            search_movie(browser,urlname,year)  
            print('%s:已完成'%(urlname))        
        except:
            #错误项加入错误列表
            name_cw.append(name)
    #搜索完毕，打印搜索错误项
    print(name_cw)
    browser.close()
    select_douban()
#处理搜索
def search_movie(drive,name,year):
    #刷新浏览器
    drive.refresh()
    #定位搜索框
    movie_search = drive.find_element_by_xpath('//*[@id="inp-query"]')
    #清空搜索框
    movie_search.clear()
    time.sleep(random.random()*4)
    #输入name并且模拟按回车键提交
    movie_search.send_keys(name[:-4])
    movie_search.send_keys(Keys.ENTER)
    time.sleep(random.random()*12)    
    #点击搜索按钮
    drive.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
    time.sleep(random.random()*2)
    #定义循环
    canWhile = True
    #循环次数
    i = 1        
    #对豆瓣搜索结果的电影标题进行循环选中，判断年份与输入的year是否相等
    while(canWhile):               
        #变量置空
        doubanurl = ' '
        doubanname= ' '
        movie_title_txt = ''
        movie_country_txt=''
        #判断是否出现错误，需要重新循环
        canif = True
        #xpath为定位电影title,xpath2为定位制片国家名称
        xpath = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[' + str(i) + ']/div/div/div[1]/a'                
        xpath2 ='//*[@id="root"]/div/div[2]/div[1]/div[1]/div[' + str(i) + ']/div/div/div[3]'
        #循环十次即可终止循环
        if i > 10:            
            canWhile = False
        #循环八次以上就从头开始（可能输入的年份错误，默认以搜索第一个为搜索结果）
        if i > 8:
            xpath = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[' + str(i-8) + ']/div/div/div[1]/a'
            xpath2 ='//*[@id="root"]/div/div[2]/div[1]/div[1]/div[' + str(i-8) + ']/div/div/div[3]'
        #判断xpath和xpath2定位是否正确
        try:            
            movie_title = drive.find_element_by_xpath(xpath)
            movie_country = drive.find_element_by_xpath(xpath2)
            #定位不准确，要判断输入是否有电影又名的存在，进行名称修订，再次搜索
        except NoSuchElementException:                        
            #有/符号则可能存在又名，只需要一个，判断是否是没有输入年份
            if '/' in name[:-4]:
                movie_search_name = '【'+name[:-4].replace('/','】',1)
                movie_search_namelist = re.findall(r'【(.*?)】',movie_search_name)
                name = movie_search_namelist[0] + "1231"  
            else:
                name = name + '没有年份'     
            #进行搜索
            movie_search = drive.find_element_by_xpath('//*[@id="inp-query"]')
            movie_search.clear()
            time.sleep(random.random())
            movie_search.send_keys(name[:-4])
            movie_search.send_keys(Keys.ENTER)
            time.sleep(random.random())    
            drive.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
            time.sleep(random.random())
            #重新进行i赋值
            i = i - 1
            canif = False            
        if canif:
            #获取title与国家
            movie_title_txt = movie_title.get_attribute('textContent')
            movie_country_txt = movie_country.get_attribute('textContent')
            #判断输入的year为数字且title中的year也为数字
            if year.isdigit() and movie_title_txt[-5:-1].isdigit():
                #年份相等
                if int(year) == int(movie_title_txt[-5:-1])  :
                    doubanurl = movie_title.get_attribute("href")
                    canWhile = False
                    break       
                #可能存在一年的误差
                elif int(year) == int(movie_title_txt[-5:-1]) + 1 or int(year) == int(movie_title_txt[-5:-1]) - 1 :
                    doubanurl = movie_title.get_attribute("href")
                    canWhile = False
                    break         
                #如果已经查找了八次以上，并且title中含有）字符，则循环结束
                elif i>8 and ')' in movie_title_txt[-5:]:
                    doubanurl = movie_title.get_attribute("href")
                    canWhile = False
                    break  
            #当输入的年份不为数字则默认搜索项第一个
            elif')' in movie_title_txt[-5:]:
                doubanurl = movie_title.get_attribute("href")
                canWhile = False
                break                             
        time.sleep(random.random()*10)
        i = i+1
    #判断title和country是否为空
    if movie_title_txt and movie_country_txt:
        movie_country_name = '【' + movie_country_txt.replace('/','】',1)
        if '】' in movie_country_name:
            print(1)
        else:
            movie_country_name = movie_country_name + '】'
        #利用正则表达式提取country
        movie_country_namelist = re.findall(r'【(.*?)】',movie_country_name)
        #处理title
        movie_title_douban = movie_title_txt.replace(' ','】',1)
        movie_title_douban = '【' + movie_title_douban
        #提取title
        doubanname_list = re.findall(r'【(.*?)】',movie_title_douban)
        #整合信息，将doubanname整合为：电影名+年份+制片国家
        doubanname = doubanname_list[0] + movie_title_txt[-5:-1] + ' ' + movie_country_namelist[0]              
    #保存url和name
    movie_fullname = open('data/doubanurl.txt','a',encoding='utf-8')
    movie_fullname.write('%s\n'%(doubanurl))      
    movie_fullname.close()  
    movie_fulltitle = open('data/doubanname.txt','a',encoding='utf-8')
    movie_fulltitle.write('%s\n'%(doubanname))      
    movie_fulltitle.close()
    
if __name__ == "__main__":       
    select_douban()


#用途：通过电影名称列表获取豆瓣地址
#所需模块：selenium、re、time、random
 # selenium模块：结合Chrome/Firefox驱动进行浏览器操作
 # webdriver:1、创建浏览器对象，支持Chrome、Firefox、Edge等，还有Android、BlackBerry等手机端的浏览器。另外，也支持无界面浏览器PhantomJS
            #2、元素定位：find_element_by_id()  # 通过元素ID定位    find_element_by_name()  # 通过元素Name定位    find_element_by_class_name()  # 通过类名定位
                    #find_element_by_tag_name()  # 通过元素TagName定位  find_element_by_link_text()  # 通过文本内容定位  find_element_by_partial_link_text()
                    #find_element_by_xpath()  # 通过Xpath语法定位       find_element_by_css_selector()  # 通过选择器定位
            #3、节点交互：比较常见的用法有：输入文字时用send_keys()方法，清空文字时用clear()方法，点击按钮时用click()方法
            #4、动作链：没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。
            #     创建拖动对象：active = ActionChains（drive）     点击拖动对象并长按保持：action.click_and_hold(target_ele) 
            #     执行拖拽      action.move_by_offset(17, 0).perform()      释放对象句柄action.release()
            #5、执行JavaScript：browser.execute_script('');
            #6、获取源码：page_source属性
            #7、前进与后退：.forward()、.back()
            #8、标签属性：.get_attribute("title")获取title属性
            #9、窗口句柄切换：.window_handles获取所有句柄；.switch_to.window(all_h[-1])切换最后窗口；.switch_to.window(all_h[0])切换第一个窗口
            #10、Cookie处理：get_cookies()获取cookies；.delete_all_cookies()删除cookies
            #11、规避检测识别：在启动Chromedriver之前，为Chrome开启实验性功能参数excludeSwitches，它的值为['enable-automation']；
            #                 webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-automation'])
            #                 driver = webdriver.Chrome(options=option)
# re模块：python独有的匹配字符串的模块，该模块中提供的很多功能是基于正则表达式实现的，而正则表达式是对字符串进行模糊匹配，提取自己需要的字符串部分，他对所有的语言都通用
    #比较常用：re.findall（pattern，string，flags = 0 ）：以string列表形式返回string中pattern的所有非重叠匹配项。从左到右扫描该字符串，并以找到的顺序返回匹配项
#time模块：time.sleep(secs):在给定的秒数内挂起调用线程的执行;参数：秒数，参数可以是一个浮点数，表示更精确的睡眠时间。
#random模块：random.random()#用于生成一个0到1的数







