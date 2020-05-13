# 各个文件用到的技术整理
## 文件：[douban_movie.py](python爬虫/douban_movie.py)
### 主要模块：selenium、re、time、random
#### selenium:结合Chrome/Firefox等浏览器驱动进行浏览器操作;主要为webdriver
##### webdriver:
            1. 创建浏览器对象，支持Chrome、Firefox、Edge等，还有Android、BlackBerry等手机端的浏览器。另外，也支持无界面浏览器PhantomJS
            2. 元素定位：
                    find_element_by_id()   通过元素ID定位  
                    find_element_by_name()   通过元素Name定位  
                    find_element_by_class_name()   通过类名定位  
                    find_element_by_tag_name()   通过元素TagName定位  
                    find_element_by_link_text()   通过文本内容定位  
                    find_element_by_partial_link_text()  
                    find_element_by_xpath()   通过Xpath语法定位  
                    find_element_by_css_selector()   通过选择器定位
            3. 节点交互：比较常见的用法有：输入文字时用send_keys()方法，清空文字时用clear()方法，点击按钮时用click()方法
            4. 动作链：
                没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。
                创建拖动对象：active = ActionChains（drive）  
                点击拖动对象并长按保持：action.click_and_hold(target_ele)  
                执行拖拽      action.move_by_offset(17, 0).perform()  
                释放对象句柄action.release()
            5. 执行JavaScript：browser.execute_script('');
            6. 获取源码：page_source属性
            7. 前进与后退：.forward()、.back()
            8. 标签属性：.get_attribute("title")获取title属性
            9.  窗口句柄切换：.window_handles获取所有句柄；.switch_to.window(all_h[-1])切换最后窗口；.switch_to.window(all_h[0])切换第一个窗口
            10. Cookie处理：get_cookies()获取cookies；.delete_all_cookies()删除cookies
            11. 规避检测识别：在启动Chromedriver之前，为Chrome开启实验性功能参数excludeSwitches，它的值为['enable-automation']；
                             webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-automation'])
                             driver = webdriver.Chrome(options=option)
##### re模块：
- python独有的匹配字符串的模块，该模块中提供的很多功能是基于正则表达式实现的，而正则表达式是对字符串进行模糊匹配，提取自己需要的字符串部分，他对所有的语言都通用
- re.findall（pattern，string，flags = 0 ）：以string列表形式返回string中pattern的所有非重叠匹配项。从左到右扫描该字符串，并以找到的顺序返回匹配项
##### time模块：
- time.sleep(secs):在给定的秒数内挂起调用线程的执行;参数：秒数，参数可以是一个浮点数，表示更精确的睡眠时间。
##### random模块：
- random.random()：用于生成一个0到1的数
---
## 文件：[TestSpider](python爬虫/TestSpider/TestSpider/spiders/mmy_movie.py)
### 主要模块：用到scrapy框架
##### scrapy组件
- Scrapy引擎（Engine）：Scrapy引擎是用来控制整个系统的数据处理流程。
- 调度器（Scheduler）：调度器从Scrapy引擎接受请求并排序列入队列，并在Scrapy引擎发出请求后返还给它们。
- 下载器（Downloader）：下载器的主要职责是抓取网页并将网页内容返还给蜘蛛（Spiders）。
- 蜘蛛（Spiders）：蜘蛛是有Scrapy用户自定义的用来解析网页并抓取特定URL返回的内容的类，每个蜘蛛都能处理一个域名或一组域名，简单的说就是用来定义特定网站的抓取和解析规则。
- 条目管道（Item Pipeline）：条目管道的主要责任是负责处理有蜘蛛从网页中抽取的数据条目，它的主要任务是清理、验证和存储数据。当页面被蜘蛛解析后，将被发送到条目管道，并经过几个特定的次序处理数据。每个条目管道组件都是一个Python类，它们获取了数据条目并执行对数据条目进行处理的方法，同时还需要确定是否需要在条目管道中继续执行下一步或是直接丢弃掉不处理。条目管道通常执行的任务有：清理HTML数据、验证解析到的数据（检查条目是否包含必要的字段）、检查是不是重复数据（如果重复就丢弃）、将解析到的数据存储到数据库（关系型数据库或NoSQL数据库）中。
- 中间件（Middlewares）：中间件是介于Scrapy引擎和其他组件之间的一个钩子框架，主要是为了提供自定义的代码来拓展Scrapy的功能，包括下载器中间件和蜘蛛中间件。
---
## 文件：[excel.py](处理文件/excel.py)
### 主要模块：
#### openpyxl:处理excel的模块
##### 模块对象详解
##### Workbook对象属性（工作簿操作）
- sheetnames：获取工作簿中的表（列表）
- active：获取当前活跃的Worksheet
- worksheets：以列表的形式返回所有的Worksheet(表格)
- read_only：判断是否以read_only模式打开Excel文档
- encoding：获取文档的字符集编码
- properties：获取文档的元数据，如标题，创建者，创建日期等
##### Worksheet，Cell对象（工作表操作，单元格）
###### Worksheet:
- title：表格的标题
- max_row：表格的最大行
- min_row：表格的最小行
- max_column：表格的最大列
- min_column：表格的最小列
- rows：按行获取单元格(Cell对象) - 生成器
- columns：按列获取单元格(Cell对象) - 生成器
- values：按行获取表格的内容(数据) - 生成器
###### Cell:
- row：单元格所在的行
- column：单元格坐在的列
- value：单元格的值
- coordinate：单元格的坐标
---
## 文件：[img.py](处理文件/img.py)
### 主要模块：PIL的image模块
#### 模块常用功能介绍
- open()=>image:打开img文件
- .size ⇒ (width, height)：获取图片尺寸（像素数）
- .resize((width,height)):修改图像大小
- save():保存图片
- .format ⇒ string or None:图片来源
- .mode ⇒ string：图像的模式
- .convert(mode)⇒ image：将当前图像转换为其他模式，并且返回新的图像

- .palette ⇒ palette or None：颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。+
- .info ⇒ dictionary：存储图像相关数据的字典
- .new(mode,size) ⇒ image /.new(mode, size,color) ⇒ image:使用给定的变量mode和size生成新的图像。Size是给定的宽/高二元组，这是按照像素数来计算的。对于单通道图像，变量color只给定一个值；对于多通道图像，变量color给定一个元组（每个通道对应一个值）。
- .copy() ⇒ image:拷贝这个图像。如果用户想粘贴一些数据到这张图，可以使用这个方法，但是原始图像不会受到影响
- .crop(box) ⇒ image:从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标
---
## 文件：[txt.py](处理文件/txt.py)
### 主要功能模块：python文件方法open() 
#### open函数介绍
#### 函数语法 open(name[, mode[, encoding)
- name : 一个包含了你要访问的文件名称的字符串值。
- mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- encoding：所要打开文件的编码格式