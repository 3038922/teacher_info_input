# encoding='UTF-8'
import sys
import openpyxl  # excel操作模块
import configparser  # 导入配置.ini模块
from selenium import webdriver
import time
# 导入Select类
from selenium.webdriver.support.ui import Select


def main(argv=None):

    config = configparser.ConfigParser()  # 类实例化
    config.read('config.ini', encoding='UTF-8')
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
    ele = driver.find_element_by_css_selector('[placeholder="请输入身份证号"]')
    ele.send_keys(userId)
    ele = driver.find_element_by_css_selector('input[type="password"]')
    ele.send_keys(userPasswd)
    verificationCode = input("请输入验证码:")
    ele = driver.find_element_by_css_selector('input[class = "login_yzm"]')
    ele.send_keys(verificationCode)
    ele = driver.find_element_by_css_selector('input[name = "login"]')
    ele.click()
    # find excel

    # 进入#document元素
    driver.switch_to_frame('iframeObj')
    # 根据excel内容定位
    ele = driver.find_element_by_xpath(
        '//*[@id="JZGZDXSCJJSHJXX_addBtn"]/span[2]')
    ele.click()
    # 奖励名称
    ele = driver.find_element_by_xpath('//*[@id="JZGZDXSCJJSHJXX_JLMC"]')
    ele.send_keys("asdfasfd")
    # 本人角色
    select = Select(driver.find_elements_by_css_selector(
        '#JZGZDXSCJJSHJXX_JSZBRJS_span'))
    select.select_by_index(1)
    input()
    # input data


if __name__ == "__main__":
    sys.exit(main())
