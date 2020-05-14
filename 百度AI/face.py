
import requests,base64,time
from urllib.parse import urlencode

def main():
    #取图片
    file = input("请输入图片绝对地址（如./.../图片名.jpg或png）")
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    try:
        f = open(file, 'rb')
    except:
        print('路径出错')
        main()
    #图片转换为BASE64模式
    img = base64.b64encode(f.read())
    params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', 'face_field': "faceshape,facetype,age,gender,beauty","max_face_num":10}
    #参数转换为urlcode
    params = urlencode(params)
    #百度AI授权信息
    access_token = '[24.06efd4eb3d6262ed7805d2ea8286bb33.2592000.1592036301.282335-19881347]'
    #完整访问地址
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    #处理响应
    if response:
        if response.json()['error_code'] ==0:
            my_txt = 'face_info'+time.strftime("%F-%H.%M-")+'.txt'
            write_word = open(my_txt,'a',encoding='utf-8')        
            #文件写入TXT文件
            for word in response.json()['result']['face_list']:            
                write_word.write('性别：%s\n年龄:%s\n颜值:%s\n脸型:%s\n'%(word['gender']['type'],word['age'],word['beauty'],word['face_shape']['type']))
                print('性别：',word['gender']['type'])
                print('年龄',word['age'])
                print('颜值：',word['beauty'])
                print('脸型：',word['face_shape']['type'])
            write_word.close()
        else:
            print('出现错误')
    else:
        print('出现错误')
    main()
if __name__ == '__main__':
  try:
      main()
  except :
      main()