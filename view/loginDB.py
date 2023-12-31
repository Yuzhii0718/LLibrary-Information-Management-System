# Form implementation generated from reading ui file 'loginDB.ui'
#
# Created by: PyQt5 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

"""
**************************************************
@IDE    ：PyCharm
@Author ：Yuzhii0718
@Update ：2023/12/6 19:05
**************************************************
"""

from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector as mc
from PyQt5.QtWidgets import QMessageBox

from .adminInfo import adminInfo


class loginDB_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_adminID = QtWidgets.QLabel(parent=Dialog)
        self.label_adminID.setObjectName("label_adminID")
        self.horizontalLayout_2.addWidget(self.label_adminID)
        self.lineEdit_adminID = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        self.lineEdit_adminID.setFont(font)
        self.lineEdit_adminID.setObjectName("lineEdit_adminID")
        self.horizontalLayout_2.addWidget(self.lineEdit_adminID)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_adminKey = QtWidgets.QLabel(parent=Dialog)
        self.label_adminKey.setObjectName("label_adminKey")
        self.horizontalLayout_3.addWidget(self.label_adminKey)
        self.lineEdit_adminKey = QtWidgets.QLineEdit(parent=Dialog)

        # 设置密码输入框
        self.lineEdit_adminKey.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        self.lineEdit_adminKey.setFont(font)
        self.lineEdit_adminKey.setObjectName("lineEdit_adminKey")
        self.horizontalLayout_3.addWidget(self.lineEdit_adminKey)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.pushButton_addAccount = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_addAccount.setObjectName("pushButton_addAccount")
        self.horizontalLayout_5.addWidget(self.pushButton_addAccount)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.label_actionStatus = QtWidgets.QLabel(parent=Dialog)
        self.label_actionStatus.setText("")
        self.label_actionStatus.setObjectName("label_actionStatus")
        self.horizontalLayout_6.addWidget(self.label_actionStatus)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem14)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 公用的数据库连接 账号密码
        self.mydatabase_adminID = ""
        self.mydatabase_adminKey = ""
        # 设置按钮的点击事件
        self.pushButton_addAccount.clicked.connect(self.login)

    def login(self):
        try:
            # 获取输入的账号和密码
            adminID = self.lineEdit_adminID.text()
            adminKey = self.lineEdit_adminKey.text()

            # 为空则提示
            if adminID == "" or adminKey == "":
                QMessageBox.critical(self.pushButton_addAccount, "错误", "账号或密码不能为空！")
                self.label_actionStatus.setText("账号或密码不能为空！")
                self.label_actionStatus.setStyleSheet("color: rgb(200, 150, 0);")
                return
            # 数据库的 user 与 password 使用的是 adminID 与 adminKey
            mydatabase = mc.connect(
                host="localhost",
                user=adminID,
                password=adminKey,
            )
            # 如果连接成功，则关闭当前窗口，提示成功
            mydatabase.close()
            QMessageBox.information(self.pushButton_addAccount, "成功", "管理员登录成功！")
            self.label_actionStatus.setText("管理员登录成功！")
            self.label_actionStatus.setStyleSheet("color: rgb(0, 200, 0);")
            # 将账号密码保存到公用的变量中
            self.mydatabase_adminID = adminID
            self.mydatabase_adminKey = adminKey
            # 向 admininfo 传递账号密码
            adminInfo(self.mydatabase_adminID, self.mydatabase_adminKey)

        except mc.Error as e:
            print("管理员登录失败：", e)
            QMessageBox.critical(self.pushButton_addAccount, "错误", "管理员登录失败！")
            # 输出 e.args 的内容
            self.label_actionStatus.setText(e.args[1])
            self.label_actionStatus.setStyleSheet("color: rgb(200, 0, 0);")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_adminID.setText(_translate("Dialog", "🪪管理员账号"))
        self.lineEdit_adminID.setPlaceholderText(_translate("Dialog", "请输入管理员账号..."))
        self.label_adminKey.setText(_translate("Dialog", "🗝️管理员密码"))
        self.lineEdit_adminKey.setPlaceholderText(_translate("Dialog", "请输入管理员密码..."))
        self.pushButton_addAccount.setText(_translate("Dialog", "🛠️登录"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = loginDB_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
