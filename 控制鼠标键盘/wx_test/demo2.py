import psutil
from pywinauto.application import Application
import pyperclip
import io
import sys
import time
import pyautogui

pyautogui.FAILSAFE = False  # 关闭自动保护机制

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


# 根据进程名获取到对应的id ,用于连接
def get_pid(processName):
    for proc in psutil.process_iter():
        try:
            if (proc.name() == processName):
                return proc.pid
        except psutil.NoSuchProcess:
            pass
    return -1


# 发送对应的消息给指定的联系人
def sendInfo(info=u'你好吃饭了吗？', friend=u'文件传输助手'):
    if (info is None):
        print("************ 任务终止，传入的信息为空 ******************")
        return
    # 获取到程序进程 PID
    procId = get_pid("WeChat.exe")
    print("Wechat.exe pid is "+ procId.__str__())
    if (procId == -1):
        print("WeChat.exe  is not running")

    # 连接到对应的app
    app = Application(backend='uia').connect(process=procId)

    # 获取到微信实例
    main_Dialog = app.window_(title=u"微信", class_name="WeChatMainWndForPC")

    # 打开微信窗口
    pyautogui.hotkey('ctrl', 'alt', 'w')

    # 弹出窗口,防止快捷键打开失败
    main_Dialog.restore()

    # 打开指定的用户消息框
    main_Dialog.type_keys('^f')
    pyperclip.copy(friend)
    main_Dialog.type_keys('^v')
    # 休息0.5秒
    time.sleep(0.5)
    # 打开指定用户的发消息页面
    main_Dialog.type_keys('{ENTER}')

    # 发送消息
    print("********* 发送消息 ****************")
    inputMsg = main_Dialog.child_window(title="输入", control_type="Edit")
    inputMsg.click_input()
    pyperclip.copy(info)
    inputMsg.type_keys('^v')

    # 休息0.5秒，点击发送
    time.sleep(0.5)
    main_Dialog.type_keys('{ENTER}')


# 触发
sendInfo()
