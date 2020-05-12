from PIL import Image
import re
import time
import os
import requests
#保存图片（以豆瓣为例）
""""
url:图片网络地址
name：图片保存名称
head:部分特定网站需要head,此处以豆瓣为例
"""
def img_save(url,name):
    #添加访问头信息
    refer_num = re.findall("c/p(.*?).jpg",url)
    refer = "https://movie.douban.com/photos/photo/"+refer_num[0]+"/"
    head = { 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            "referer" :refer}       
    #创建文件夹    
    save_path = 'data'
    #看文件夹是否存在，不存在则新建
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    #图片地址
    path = save_path+"/"+"1.jpg"
    #保存图片
    r=requests.get(url,headers=head)    
    with open(path,'wb')as f:
        f.write(r.content)
        f.close()
    #修改图片大小
    img = Image.open(path)
    len_img = img.size
    len_img_width = len_img[0]    
    len_img_height = len_img[1]
    len_img_prop = len_img_height / len_img_width
    if len_img_width > 900:
        len_img_width = 900
        len_img_height =int(round(900 * len_img_prop))
    img = img.resize((len_img_width,len_img_height))
    try:
        img.save(path)
    except OSError:
        path =   save_path+"/"+"1.png"
        img.save(path) 
    print('%s已完成'%(name))

#打开图片修改图片尺寸
def img_size(the_path):    
    #选择所需更改的图片格式
    value =input('1:.jpg;2:.png  :')
    if value == '1':
        the_str = '.jpg'
    else:
        the_str = '.png'
    #默认图片名称为1(可有多张进行批量修改)
    for i in range(1,2):
        #定位图片
        the_path = path + str(i) + the_str
        #打开图片
        img = Image.open(the_path)
        #获取图片大小
        len_img = img.size
        len_img_width = len_img[0]    
        len_img_height = len_img[1]
        #锁定纵横比
        len_img_prop = len_img_height / len_img_width
        #宽度大于900px则修改
        if len_img_width > 900:
            len_img_width = 900
            len_img_height =int(round(900 * len_img_prop))
        img = img.resize((len_img_width,len_img_height))
        img.save(the_path)
        print('尺寸成功修改为宽度900px')
    img_size(path)

if __name__ == "__main__":
    img_save('https://img1.doubanio.com/view/photo/raw/public/p2555117729.jpg','name')
    #图片所在文件夹
    path = 'data/'
    img_size(path)


    #用途：处理img文件
#所需模块：
    # PIL里面的image模块:处理图片的模块
    #image常用功能：
        #open()=>image:打开img文件
        #save():保存图片
        #.format ⇒ string or None:图片来源
        #.mode ⇒ string：图像的模式
        #.convert(mode)⇒ image：将当前图像转换为其他模式，并且返回新的图像
        #.size ⇒ (width, height)：获取图片尺寸（像素数）
        #.palette ⇒ palette or None：颜色调色板表格。如果图像的模式是“P”，则返回ImagePalette类的实例；否则，将为None。+
        #.info ⇒ dictionary：存储图像相关数据的字典
        #.new(mode,size) ⇒ image /.new(mode, size,color) ⇒ image:使用给定的变量mode和size生成新的图像。Size是给定的宽/高二元组，这是按照像素数来计算的。对于单通道图像，变量color只给定一个值；对于多通道图像，变量color给定一个元组（每个通道对应一个值）。
        #.copy() ⇒ image:拷贝这个图像。如果用户想粘贴一些数据到这张图，可以使用这个方法，但是原始图像不会受到影响
        #.crop(box) ⇒ image:从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标
        #.resize((width,height)):修改图像大小


