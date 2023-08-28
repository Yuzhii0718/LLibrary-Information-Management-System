# coding:utf-8
"""
**************************************************
@File   ：PyQt6_QuickStart -> main
@IDE    ：PyCharm
@Author ：Yuzhii0718
@Date   ：2023/8/17 23:30
**************************************************
"""
import os

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

from adminInfo import clear_adminInfo, log_status, get_admin_account, get_admin_password

from addAccount import addAccount_Dialog
from addBook import addBook_Dialog
from librarySystem import Ui_MainWindow
from loginDB import loginDB_Dialog
from viewBooks import viewBooks_Dialog
from viewAccount import viewAccount_Dialog

import mysql.connector as mc


class LibrarySystemMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 3.添加书籍对话框
        # 3.1创建对话框
        self.addBookDialog_ui = addBook_Dialog()
        # 3.2创建对话框的ui
        self.addBookDialog = QDialog()
        # 4.添加账号对话框
        # 4.1创建对话框
        self.addAccountDialog_ui = addAccount_Dialog()
        # 4.2创建对话框的ui
        self.addAccountDialog = QDialog()
        # 5.查看书籍对话框
        # 5.1创建对话框
        self.viewBooksDialog_ui = viewBooks_Dialog()
        # 5.2创建对话框的ui
        self.viewBooksDialog = QDialog()
        # 6.查看账号对话框
        # 6.1创建对话框
        self.viewAccountDialog_ui = viewAccount_Dialog()
        # 6.2创建对话框的ui
        self.viewAccountDialog = QDialog()

        # 0.登录数据库对话框
        # 0.1创建对话框
        self.loginDBDialog_ui = loginDB_Dialog()
        # 0.2创建对话框的ui
        self.loginDBDialog = QDialog()

        # 1.设置主窗口的ui
        self.setupUi(self)
        # 2.应用图标
        self.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        clear_adminInfo()
        self.show()

        # 连接信号与槽
        # 3.添加书籍 对话框
        self.toolButton_addBook.clicked.connect(self.toolbutton_add_book)
        # 4.添加账号 对话框
        self.toolButton_addAccount.clicked.connect(self.toolbutton_add_account)
        # 5.查看书籍 对话框
        self.toolButton_viewBooks.clicked.connect(self.toolbutton_view_books)
        # 6.查看账号 对话框
        self.toolButton_viewAccount.clicked.connect(self.toolbutton_view_account)

        # 菜单动作 关于
        self.action_about.triggered.connect(self.about)
        # 菜单动作 退出
        self.action_exit.triggered.connect(self.close)
        # 菜单动作 帮助
        self.action_help.triggered.connect(self.help_message)
        # 菜单动作 登录数据库
        self.action_login_db.triggered.connect(self.login_database)
        # 菜单动作 登出数据库
        self.action_logout_db.triggered.connect(self.logout_database)
        # 菜单动作 初始化数据库
        self.action_initDB.triggered.connect(self.init_database)

    def toolbutton_add_book(self):
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 重载对话框 避免页面显示不正常
        self.addBookDialog = QDialog()
        # 将对话框的ui加载到对话框中
        self.addBookDialog_ui.setupUi(self.addBookDialog)
        # 设置对话框的标题
        self.addBookDialog.setWindowTitle('添加书籍')
        # 设置对话框的图标
        self.addBookDialog.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        # 刷新对话框
        self.addBookDialog.exec()

    def toolbutton_add_account(self):
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 重载对话框 避免页面显示不正常
        self.addAccountDialog = QDialog()
        # 将对话框的ui加载到对话框中
        self.addAccountDialog_ui.setupUi(self.addAccountDialog)
        # 设置对话框的标题
        self.addAccountDialog.setWindowTitle('添加账号')
        # 设置对话框的图标
        self.addAccountDialog.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        # 刷新对话框
        self.addAccountDialog.exec()

    def toolbutton_view_books(self):
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 重载对话框 避免页面显示不正常
        self.viewBooksDialog = QDialog()
        # 将对话框的ui加载到对话框中
        self.viewBooksDialog_ui.setupUi(self.viewBooksDialog)
        # 设置对话框的标题
        self.viewBooksDialog.setWindowTitle('查看书籍')
        # 设置对话框的图标
        self.viewBooksDialog.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        # 刷新对话框
        self.viewBooksDialog.exec()

    def toolbutton_view_account(self):
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 重载对话框 避免页面显示不正常
        self.viewAccountDialog = QDialog()
        # 将对话框的ui加载到对话框中
        self.viewAccountDialog_ui.setupUi(self.viewAccountDialog)
        # 设置对话框的标题
        self.viewAccountDialog.setWindowTitle('查看账号')
        # 设置对话框的图标
        self.viewAccountDialog.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        # 刷新对话框
        self.viewAccountDialog.exec()

    def login_database(self):
        # 重载对话框 避免页面显示不正常
        self.loginDBDialog = QDialog()
        # 将对话框的ui加载到对话框中
        self.loginDBDialog_ui.setupUi(self.loginDBDialog)
        # 设置对话框的标题
        self.loginDBDialog.setWindowTitle('登录数据库')
        # 设置对话框的图标
        self.loginDBDialog.setWindowIcon(QIcon('./src/images/yuzu.svg'))
        # 刷新对话框
        self.loginDBDialog.exec()

    def logout_database(self):
        if log_status() is False:
            QMessageBox.critical(self, '错误', '您还未登录！')
            return
        else:
            clear_adminInfo()
            QMessageBox.information(self, '提示', '已登出数据库！')

    def init_database(self):
        # 先判断是否登录
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 选择文件,文件是本地的sql文件，文件路径为 `./src/library.sql`
        # 利用 os.path.abspath() 将 url 转换为绝对路径
        file_path2abs = os.path.abspath("./src/library.sql")
        print(file_path2abs)
        # 先连接数据库，查询是否存在数据库
        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()

            dbname = "library"

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password)
            )

            mycursor = mydatabase.cursor()
            mycursor.execute("create database {}".format(dbname))
            print("数据库已创建！")

            # 导入数据库,利用source命令
            shell = "mysql -u {} -p{} {} < {}".format(admin_username, admin_password, dbname, file_path2abs)
            os.system(shell)
            print("数据库已导入！")
            QMessageBox.information(self, '提示', '数据库初始化完毕！')

        except Exception as e:
            print(e)
            return None

    def about(self):
        QMessageBox.about(self, '关于', '关于信息\n作者：Yuzhii0718\n版本：v1.0.0\n时间：2023-08-20')

    def help_message(self):
        reply = QMessageBox.question(self, '帮助', '是否打开帮助文档 README ？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # 打开本地文件 src/doc/index.html
            QDesktopServices.openUrl(QUrl.fromLocalFile('./src/doc/index.html'))
        else:
            pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确认退出？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # 退出前删除 adminInfo.txt
            clear_adminInfo()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    window = LibrarySystemMainWindow()
    window.show()
    app.exec()
