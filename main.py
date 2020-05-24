# encoding='UTF-8'
import openpyxl  # excel操作模块
import sys
import configparser  # 导入配置.ini模块
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# 导入Select类


def main(argv=None):

    # 初始化
    config = configparser.ConfigParser()  # 类实例化
    config.read("config.ini", encoding='UTF-8')
    url = config.get('select', 'url')
    userId = config.get('select', 'id')
    userPasswd = config.get('select', 'passwd')
    if url == "":
        url = input("请输入你要登录的网址")

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(url)

    if userId == "":
        userId = input("请输入您的身份证:")
    if userPasswd == "":
        userPasswd = input("请输入您的密码:")
    print("您输入的的账号为:", userId, " 密码为:", userPasswd)
    # login
    ele = driver.find_element_by_css_selector(
        '[placeholder="请输入身份证号"]')
    ele.send_keys(userId)
    ele = driver.find_element_by_css_selector('input[type="password"]')
    ele.send_keys(userPasswd)
    verificationCode = input("请输入验证码:")
    ele = driver.find_element_by_css_selector(
        'input[class = "login_yzm"]')
    ele.send_keys(verificationCode)
    ele = driver.find_element_by_css_selector('input[name = "login"]')
    ele.click()

    # 读取表格
    wb = openpyxl.load_workbook("demo.xlsx")
    # 寻找对应元素群 并填入
    # 进入#document元素
    driver.switch_to_frame('iframeObj')
    # 根据excel内容定位 新增
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_addBtn"]/span[2]').click()
    # 输入奖励名称
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_JLMC"]').send_keys("asdfasfd")
    # 本人角色 选择
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_JSZBRJS_span"]').click()
    # 选择10-独立指导教师
    driver.find_element_by_css_selector(
        '#JZGZDXSCJJSHJXX_JSZBRJS_listContent > table > tbody > tr:nth-child(2)').click
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_JXDJ"]').send_keys('国家级')
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_HJNY"]').send_keys('2010-01')
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_BRCDGZMS"]').send_keys('汪汪叫')
    driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_SJDW"]').send_keys('教育局')
    driver.find_element_by_xpath(
        '/html/body/div[8]/div[3]/div/button[1]/span').click()  # 保存
    input()
# input data


if __name__ == "__main__":
    sys.exit(main())
