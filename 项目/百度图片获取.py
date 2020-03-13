import re,os,requests  
from urllib import error

class CoImage(object):
    def __init__(self,keyword,path,List):

        self.keyword=keyword
        self.path = path
        self.List=List

    def Find(self):##查找
        
        ##创建文件夹
        dir_2=self.path + self.keyword
        if os.path.exists(self.path):
            if os.path.exists(dir_2):
                print("文件夹已经存在")
            else:
                os.mkdir(dir_2)
                print("已经创建成功")
        else:
            os.mkdir(self.path)
            os.mkdir(dir_2)
            print("已经创建成功")
        self.path=dir_2

        ##检测有多少
        print('正在检测图片总数，请稍等.....')
        t=0   ## url参数
        url= 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + self.keyword + '&pn='
        while t < 1000:
            Url = url + str(t)
            try:
                Result = requests.get(Url, timeout=7)
            except BaseException:
                t = t + 60
                continue
            else:
                image_url = re.findall('"objURL":"(.*?)",',Result.text, re.S) 

                if len(image_url) == 0:
                    break
                else:
                    for i in image_url:
                        
                        self.List.append(i)

                    t = t + 60
    
        print('经过检测%s类图片共有%d张' % (self.keyword, len(self.List)))
        
    def DownloadImage(self):##下载图片
        numimage = int(input('请输入想要下载的图片数量 '))
        print('找到关键词:' + self.keyword + '的图片，即将开始下载图片...')
        for image in self.List:
            print('正在下载第' + str(self.List.index(image)+1)+ '张图片')
    
            try:
                if image is not None:
                    r = requests.get(image, timeout=7)
                else:
                    continue
            except BaseException:
                print('错误，当前图片无法下载')
                continue
            else:
                string = self.path +"/"+ self.keyword +  '_' + str(self.List.index(image)) + '.jpg'
                with open(string,"wb") as f:
                    f.write(r.content)
                    f.close()
                
            if  self.List.index(image)>= numimage:
                return
     
                    
    def main(self):
        self.Find()
        self.DownloadImage()

if __name__ == '__main__': 
    
    m=CoImage(
        List=[],##存放url
        keyword = input("请输入搜索关键词: "),
        path = r"C:\Users\Administrator\Desktop\image\\"##存放路径注意最后\
    )
    
    m.main()


    print('当前搜索结束，感谢使用')


