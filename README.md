# 各个文件说明
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