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
