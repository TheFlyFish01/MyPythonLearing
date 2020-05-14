from PIL import ImageGrab
from aip import AipOcr
import keyboard,os,time,base64,requests

global Count
Count = 1
def Solve():
    """ 你的 APPID AK SK """
    APP_ID = '19457851'
    API_KEY = 'RQErUldr8qdY0rCMP11kj8G2'
    SECRET_KEY = 'QuyGDWhHbIIgBpXhbCDyWzA5849Ewn8G'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """结束"""
    global Count #这是按顺序命名的全局变量
    try:
        Image = ImageGrab.grabclipboard() #获取截图图片
        Name ='data/' + str(Count)+r'.jpg' 
        Image.save(Name) #保存图片
        time.sleep(1) #睡觉等待
        Count = Count + 1
        with open(Name,'rb') as File:
            Img = File.read()
        Result = client.basicAccurate(Img)
        Num = Result['words_result_num']
        now_time = time.strftime("%F-%H.%M-") 
        word_str = 'data/'+'文字内容' + now_time +str(Count)+'.txt'
        word = open(word_str,'a',encoding='utf-8')
        if (Num==0):
            print("图片没有字") #你的图片里面没有字哦
        else:
            for x in Result['words_result']:                
                word.write('%s\n'%(x['words']))                
                print(x['words'])
        word.close()
        print('当前解析完成\n如需解析请先截图，截完图回来按F7执行解析')
    except:
        print("请先截图") #你内存没有图片哦
    
def Clear():    
    global Count
    try:
        for x in range(1,999):#应该最多用999个吧
            Name = str(x)+r'.jpg'
            os.remove(Name)
    except:
        print("Done")
    Count = 1 #把序号再变为1
    
def main():
    print('***********使用说明**************')
    print('本软件将产生大量图片文件和txt文件，建议新建文件夹，将本软件放入新文件夹再运行')
    print('使用方法：请先截图，截完图回来按F7执行解析')
    keyboard.add_hotkey('f7',Solve) #f7处理图片    
    print('注：截图默认保存在文件夹，按F9可删除上次截图')
    keyboard.add_hotkey('f9',Clear) #f9删除图片
    keyboard.wait('esc') #按退出键结束程序
def imgToTxt():
    file = input("请输入图片绝对地址（如./.../图片名.jpg或png）")
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    access_token = '[24.3615b8d7ab53f2cba5249b358c2a620d.2592000.1592033404.282335-19457851]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if response.json()['words_ result num'] ==0:
            print('图片没有字')
        else:
            my_txt = 'data/'+'myword'+time.strftime("%F-%H.%M-")+'.txt'
            write_word = open(my_txt,'a',encoding='utf-8')        
            for word in response.json()['words_result']:            
                write_word.write('%s\n'%word['words'])
            write_word.close()
            print (response.json())
    else:
        print('百度ai接口出错')

if __name__ == '__main__':
    print('选择启动模式：1、打开图片；2、截图使用')
    choice = input('请选择')
    if '1' in choice:
        imgToTxt()
    else:
        main()