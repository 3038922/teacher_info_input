# 中国教师信息管理系统批量录入
- 该项目旨在帮助个人信息较多的老师通过EXCEL 批量录入信息.
- 浙江省的登录地址 `http://jiaoshi.zjedu.gov.cn:8082/selfservice/index`
## 使用说明
1. 必须安装chrome 
2. 下载对应你chrome版本号的chromedriver 我项目里的默认版本号是`83.0.4103.39` [Download](http://npm.taobao.org/mirrors/chromedriver/)

## 开发环境安装
- 如果要协助开发程序请执行这步,只是使用不需要.
1. 安装python3.8 
    - [Download](https://github.com/3038922/new_century_robotics/releases/download/v1.0/python-3.8.1-amd64.exe)

2. 安装需要使用的库
- `pip install openpyxl selenium` 


## 自用命令记录
### pyinstaller配置说明
- 生成一大堆 `pyinstaller main.py`
- 生成单exe `pyinstaller -F main.py`
- 生成带图标文件的EXE `pyinstaller -F -i ./pic/机器人标.ico main.py`