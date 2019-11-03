# **python selenium自动化测试框架**

说明：本UI自动化测试框架只是初版，公用的操作方法写的不多，还有很多是待完善。仅供个人学习使用，禁止商业用途。

本框架基于关键字驱动模式，采用python3.7+selenium3+yaml+unittest技术将公用方法封装，测试报告使用HTMLTestRunner生成。能完成B/S模式网页的自动化测试工作。

1、将基本操作方法封装，模块管理

2、yaml管理页面控制和测试用例数据。

## 测试框架分层设计

1、把浏览器驱动、查找定位元素、 常见的操作、检查点验证封装成基础类，不管是什么类型的B/S模式的产品，可直接使用此框架。

2、用例层针对产品页面功能进行构造模拟执行测试

3、框架层提供基础的组件，支撑整个流程执行及功能扩展，给用例层提供页面的元素数据，用例测试数据，测试报告输出。

测试框架目录结构

![1572787042103](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1572787042103.png)



## 编写用例方法

如果我们新增测试系统登录功能测试用例：

邮件邮箱配置文件在目录database->user.ini

1、首先，在elementpage目录下新增一个页面对象yaml文件，可参考element.yaml格式编写。这些文件是提供给测试用例中调度并执行定位识别操作。

2、在testdata目录下新增下个登录的yaml文件提供测试用例作为测试数据

3、在testcase目录下创建测试用例文件login.py文件，采购关键字驱动读取yaml页面元素和测试数据文件

4、执行主程充，可输出测试报告看到实际结果

## 测试结果展示

HTML报告日志

![1572787879078](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1572787879078.png)



用例失败自动截图存放指写的目录

![1572787940953](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1572787940953.png)



## 邮件测试报告

![1572788087222](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1572788087222.png)



