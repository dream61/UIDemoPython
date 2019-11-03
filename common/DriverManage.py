# coding=utf-8
from selenium.webdriver import Remote
from selenium import webdriver
class DriverManage(object):
    # def __init__(self):
    #     self.dl = webdriver
    #     # 设置 chrome 二进制文件位置
    #     self._binary_location = "..//driver//chromedriver.exe"
    #     # 添加启动参数
    #     self._arguments = ["--test-type", "--disable-popup-blocking"]
    #     # 添加扩展应用
    #     self._extension_files = []
    #     self._extensions = []
    #     # 添加实验性质的设置参数
    #     self._experimental_options = {}
    #     # 设置调试器地址
    #     self._debugger_address = None
    def getDriver(type):
        driver = webdriver
        if driver is None:
            driver = DriverManage.initDriver(type)
            print(type)
        return driver

    def initDriver(type):
        if type.lower() == "ie":
            capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
            capabilities['acceptSslCerts'] = True
            dl = webdriver.Ie(capabilities=capabilities)
        elif type.lower() == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            dl = webdriver.Firefox(firefox_profile=profile)
        elif type.lower() == "chrome":
            # capabilities = webdriver.DesiredCapabilities.chrome()
            # options = webdriver.ChromeOptions()
            # options.add_argument('--ignore-certificate-errors')
            # options.add_argument('--user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
            # dl = webdriver.Chrome(chrome_options=options)
            dl = webdriver.Chrome()
            dl.maximize_window()
            dl.implicitly_wait(10)
        else:
            print("浏览器类型错误")
        return dl


