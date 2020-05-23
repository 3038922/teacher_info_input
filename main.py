# encoding='UTF-8'
import userCore
import getData
import sys

# 导入Select类


def main(argv=None):

    # 初始化
    core = userCore.core("config.ini")
    # 读取表格
    getData.getData(core.getConig('excelPath'))
    # 寻找对应元素群 并填入
    core.findElements()

    input()
    # input data


if __name__ == "__main__":
    sys.exit(main())
