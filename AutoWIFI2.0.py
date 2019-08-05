#用于自动连接校园网，配合1.0使用，实现自动连接，自动登录。
from pywifi import const,PyWiFi,Profile
import time
def test_interfaces():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    if ifaces.status() in [const.IFACE_CONNECTED, const.IFACE_CONNECTING]:
        print('无线网卡 %s 已连接！' % ifaces.name())
    else:
        print('无线网卡 %s 未连接！' % ifaces.name())
def test_scan():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    bsses = iface.scan_results()
    for bss in bsses:
        print("WIFI名称: %s" % bss.ssid)
def test_disconnect():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    if ifaces.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
        print("无线网卡 %s 未连接！" % ifaces.name())
    else:
        print("无线网卡 %s 未连接！" % ifaces.name())

def test_connect(wifi_name,wifi_password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    test_disconnect()
    time.sleep(3)
    profile_info = Profile()
    profile_info.ssid = wifi_name
    profile_info.auth = const.AUTH_ALG_OPEN
    profile_info.akm.append(const.AKM_TYPE_NONE)
    profile_info.cipher = const.CIPHER_TYPE_CCMP
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile_info)
    iface.connect(tmp_profile)
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:
        print("wifi: %s 连接成功"% wifi_name)
    else:
        print("wifi: %s 连接失败" % wifi_name)
if __name__ == "__main__":
    test_disconnect()
    test_interfaces()
    test_scan()
    test_connect("BISTU","")
