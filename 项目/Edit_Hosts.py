from re import sub
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HostGet(object):
    def __init__(self,file,on_off):

        self.driver=None
        self.name=None
        self.file=file
        self.on_off=on_off
        
    def onoff(self):        #窗口开关
        
        if self.on_off :
            self.driver = webdriver.Chrome()
        else:
            from selenium.webdriver.chrome.options import Options
            option =Options()
            option.add_argument('--headless')#不显示
            option.add_argument("--disable-gpu")#规避BUG
            option.add_argument('blink-settings=imagesEnabled=false') #不加载图
            self.driver = webdriver.Chrome(options=option)

 
    def gethost(self):

        file = open(self.file,"r",errors="ignore")

        while True:
            try:
                self.name = file.readline().strip()
                if not self.name:
                    file.close()
                    break
                elif self.name[0] =="#":
                    continue
                else:
                    m.get()                    
            except Exception as e:
                print("报错")
        self.driver.quit()
        self.driver.service.stop()
    def get(self):
        self.driver.get("http://ping.chinaz.com/"+self.name)
        sleep(20)
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#speedlist")))
        
        while True:
            try:
                soup = BeautifulSoup(self.driver.page_source, "lxml").find_all("div",class_="row listw tc clearfix")
                if soup[-1].find_all("div")[1].text == "-" :
                    sleep(5)
                else:
                    break
            except:
                print("检查网络")
            
        n,L=0,[[]for i in range(120)]
        for i in soup:
            x=i.find_all("div")
            if x[3].text in ["-","超时"]  :
                continue
            else:
                L[n].append(int(sub("\D","",x[3].text)))
                L[n].append(x[1].text.strip())
                n=n+1
                
        L=[i for i in L if i]    #删除空行
        if L :
            L.sort()#排序
            print(L[0][1]+" "+self.name)
        else:
            print("disable  "+self.name)
        
        ##    temp=[]
        ##    for i in L:
        ##        if i[1] not in temp:
        ##            temp.append(i[1])
        ##            print(i[1]+" "+self.name)
        
           

    def main(self):
        m.onoff()
        m.gethost()

if __name__ == "__main__" :
    m = HostGet(
        on_off=1,##窗口开关0，1
        file="C:\\Users\Administrator\Desktop\host.txt"##域名存放路径
        )
    
    m.main()
