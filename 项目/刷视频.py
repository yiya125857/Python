import time,random,re,os,requests,base64
from subprocess import run #不显示dos
from PIL import Image
import sys  #结束程序


class DouYin(object):
     

     def __init__(self,app,tb,x,t,rang):
          self.rang=rang
          self.tb=tb  #定时
          self.bool = app#判断哪个app
          c=["com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity" , "com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.main.MainActivity"]
          self.app= c[app]  
          self.a = 1080 #屏幕x
          self.b = 2244 #屏幕y
          self.x = x #回刷参数
          self.t = t #视频观看时长
     def Shibie(self):
          from aip import AipOcr
          try:
               #time.sleep(1)
               run('adb shell screencap -p /sdcard/jt.png',shell=True)

               run('adb pull /sdcard/jt.png .',shell=True)
               img = Image.open("jt.png")
               if self.bool == 0 :
                    img.crop((940,1775,1050,1830)).save("jt.png")#kuaishou
               elif self.bool == 1 :
                    img.crop((930,1360,1070,1415)).save("jt.png")#douyin
               else:
                    None
          except Exception as e:
               print(e+"截屏失败")
          """ 你的 APPID AK SK """
          """请修改成你的"""
          APP_ID = '18787824'
          API_KEY = 'auIAy7QAg7p6cKcqG068jqdN'
          SECRET_KEY = 'HKmdQkChsa1XQihuHbIb8hbamyy5MXY5'
          client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
          file=open("jt.png",'rb')
          image=file.read()
          file.close

          options = {};
          options["language_type"] = "ENG";
          x=client.basicGeneral(image,options)["words_result"]   #普通识别
          #x=client.basicAccurate(image)["words_result"]       #高精度识别
          t=""
          try:
               for i in x:
                    t=i["words"]
               z=0#<<<<<<<<<<<<<<<<<<<<<
               if t:
                    if t[-1] == "w" or t[-1] == "W":
                         z = int(re.sub("\D", "", t))*1000
                    else:
                         z= int(re.sub("\D", "", t))#\D匹配任何非数字字符，因此，上面的代码实际上是替换每个非数字字符为空字符串的。
                    print("------------"+str(z))
               else:
                    None
          except Exception as e:
               print(e)
          
          return z
     def DianZan(self):#点赞坐标获取
          if self.bool==0:
               return 'adb shell input tap {} {} 200'.format(str(self.a-80),str(round(self.b*0.77)))
          elif self.bool ==1 :
              return 'adb shell input tap {} {} 200'.format(str(self.a-80),str(round(self.b*0.6)))
          else:
               print("请将参数app设成0或1")
          
     def Start(self):#启动app
          run("adb shell am start -n {}".format(self.app),shell=True)
          time.sleep(3)
          
     def GetWm(self):#获取屏幕尺寸
          try:
               #print(os.popen("adb devices").read())#获取设备id

               wm=os.popen("adb shell wm size").read()#获取回应
               x=wm.strip().split(": ")[-1].split("x")
               if x[0]>x[1]:
                   x.reverse()
               else:
                   None  
               self.a=int(x[0])
               self.b=int(x[1])
          except IndexError as e:
               print("请检查 设备连接/开发者模式/USB调试")
               sys.exit(1)
               
     def Box(self):#定时box
          if self.bool == 0:
               return None
          else:
               a=self.a
               b=self.b
               run('adb shell input tap {} {}'.format(round(a/2),round(b-100)),shell=True)
               time.sleep(0.5)
               run('adb shell input tap {} {}'.format(round(a-100),round(b-100)),shell=True)
               time.sleep(0.5)
               run('adb shell input swipe {} 200'.format("{0} {1} {2} {3}".format(a-10,round(b/2),round(a/2),round(b/2))),shell=True)
               time.sleep(3)
               
     def Shua(self):
          z=0 #计数器
          c=["快手极速版","抖音极速版"]
          print(c[self.bool]+"开始刷视频")
          #滑动参数
          a="{0} {1} {2} {3}".format(round(self.a/2),round(self.b/3),round(self.a/2),round(self.b*0.7))
          b="{0} {1} {2} {3}".format(round(self.a/2),round(self.b*0.7),round(self.a/2),round(self.b/3))
          startime=time.time()

          while True:
##               try:
                    if random.randrange(0,self.x,1) == 1:  ##1/5概率往回刷
                         
                         for i in range(random.randint(1,3)):  ##回刷几次
                              
                              print("↑↑↑↑↑↑")
                              run('adb shell input swipe {} {}'.format(a,random.randint(300,500)),shell=True)
                              time.sleep(random.uniform(0,4))
                              run(m.DianZan(),shell=True)
                              z=z+1   #回刷计数器 
                    else:
                         print("↓↓↓↓↓↓")
                         x=random.randint(self.x-1,self.x+1)
                         for i in range(x):
                              
                              run('adb shell input swipe {} {}'.format(b,random.randint(300,500)),shell=True)
                              s1=random.uniform(self.t-3,self.t+3)     #随机数
                              s2=random.uniform(1,3)
                              
                              if z != 0 :   #回刷之后快速刷过
                                   print(str(x)+"----快----"+str(i+1))
                                   time.sleep(s2)
                                   z=z-1     #刷过减数 
                              else:
                                   print(str(x)+"----慢----"+str(i+1))
                                   time.sleep(s1)
                                   
                              
                              
                              (x1,x2)=self.rang
                              
                              t=m.Shibie ()
                              if  t>=x1 and t<=x2:
##                              if random.randint(1,3) == 0: #1/3点赞概率
                                   run(m.DianZan(),shell=True)
          
                                   endtime=time.time()
                                   if round((endtime-startime)/60) >= self.tb : #定时判断
                                        break
                                   elif round((endtime-startime)%30) == 0 and round((endtime-startime)%30) != 0:
                                        Box()
                                   else:
                                        None
                                   
                              else:
                                   None
                                        
##               except Exception as e:
##                    print(e)                 
                    
         
     def main(self):
          m.Start()
          m.GetWm()
          m.Box()
          m.Shua()
                   
if __name__ == '__main__':
     m=DouYin(
          tb=120,      #定时,单位分钟
          x=5,         #1/5概率回刷，防止封号
          t=10,        #一个视频大概看10s
          rang=(10000,100000),  #赞在10000—100000点赞
          app=0,       #app代码  0：快手  1：抖音  <<<<<<<<<<<<<<<<<<<<<<<<<<<<一定要设置好
          #打开开发者模式，指针位置 点在赞的位置查看
          )

     m.main()

     print("完成")
