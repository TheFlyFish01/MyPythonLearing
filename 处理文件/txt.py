def save_txt(name):
    #打开TXT文件，没有则创建
        #方式一
    title_data1 = open("data/22.txt",'a',encoding='utf-8')
    title_data1.write("%s"%(name))
    title_data1.close()
        #方式二
    with open("data/22.txt", "a+",encoding='utf-8') as fp:
        fp.write("%s\n"%(name))
        
if __name__ == "__main__":
    save_txt('5')