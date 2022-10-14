# -*- coding: utf-8 -*-
# @Time : 2022/6/6 10:32
# @Author : AMan
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow

# 执行命令生成ui对应的py文件
# PySide6-uic 【demo.ui】 o 【ui_demo.py】
from dy_demo import Ui_Form
import MyDySpider
from Signal import my_signal


class MainWindow(QMainWindow):
    db_connect = ' '

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()  # UI类实例化
        self.ui.setupUi(self)
        self.band()

    def band(self):
        # ------------- 使用 -------------
        # self.ui.___ACTION___triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___clicked.connect___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # #自定义信号.属性名.connect(_FUNCTION___)
        # -------------------------------
        self.ui.startBase.clicked.connect(self.handle_connect_date_base)
        self.ui.startGet.clicked.connect(self.handle_start_get_click)
        my_signal.start_get.connect(self.my_start_get)

    def my_start_get(self):
        self.ui.startGet.clicked.connect(self)

    def handle_connect_date_base(self):
        log = self.ui.logPrint
        ip = self.ui.inputIp.text()
        port = self.ui.inputPort.text()
        user = self.ui.inputUser.text()
        password = self.ui.inputPassword.text()
        database = self.ui.inputDataBase.text()
        log.append(f'ip:{ip},端口:{port},\n用户名:{user},密码:{password},\n数据库:{database}')
        self.db_connect = MyDySpider.get_db_connect(host=ip, port=port, user=user, password=password, database=database,
                                                    log=log)

    # 连接dy直播，获取打印评论
    def handle_start_get_click(self):
        def inner_fuc():
            log = self.ui.logPrint
            url = self.ui.inputUrl.text()
            log.append(f'>>> 连接直播间:{url}')
            # https://live.douyin.com/694834626408
            MyDySpider.stat_get(url=url, log=log, db=self.db_connect)

        task = Thread(target=inner_fuc)
        task.start()


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行直接退出
