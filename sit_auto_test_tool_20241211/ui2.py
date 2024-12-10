import sys
from PySide6.QtCore import (QThread, Slot)
from PySide6.QtWidgets import QApplication, QWidget
import autotest
from main_logic import RebootLogic


class mystats(QWidget):
    def __init__(self, parent=None):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        super().__init__(parent)
        self.ui = autotest.Ui_Form()
        self.ui.setupUi(self)
        #引用逻辑代码类
        self.logic = RebootLogic()# 逻辑代码的实例化

    #reboot逻辑代码
    @Slot()
    def on_reboot_test_clicked(self):
        self.logic.reboot_logic()



if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication()
    myWindow = mystats()
    myWindow.show()
    n = app.exec_()
    sys.exit(n)
