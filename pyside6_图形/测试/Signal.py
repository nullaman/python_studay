# -*- coding: utf-8 -*-
# @Time : 2022/6/6 13:56
# @Author : AMan

from PySide6.QtCore import Signal, QObject


class MySignal(QObject):
    start_get = Signal()


my_signal = MySignal()
