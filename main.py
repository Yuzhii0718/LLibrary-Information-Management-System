# coding:utf-8
"""
**************************************************
@File   ：PyQt5_QuickStart -> main
@IDE    ：PyCharm
@Author ：Yuzhii0718
@Date   ：2023/8/17 23:30
@Update ：2023/12/6 19:05
**************************************************
"""
import os
import subprocess

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog

from view.adminInfo import clear_adminInfo, log_status, get_admin_account, get_admin_password
from view.addAccount import addAccount_Dialog
from view.addBook import addBook_Dialog
from view.librarySystem import Ui_MainWindow
from view.loginDB import loginDB_Dialog
from view.viewBooks import viewBooks_Dialog
from view.viewAccount import viewAccount_Dialog

import mysql.connector as mc

import resource.resource_rc
from common.config import *


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
        self.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        # 菜单动作 导入数据库
        self.action_importDB.triggered.connect(self.import_database)
        # 菜单动作 导出数据库
        self.action_exportDB.triggered.connect(self.export_database)

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
        self.addBookDialog.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        self.addAccountDialog.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        self.viewBooksDialog.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        self.viewAccountDialog.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        self.loginDBDialog.setWindowIcon(QIcon(':/gallery/images/yuzu.svg'))
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
        file_path = "./resource/library.sql"
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
            shell = "mysql -u {} -p{} {} < {}".format(admin_username, admin_password, dbname, file_path)
            process = subprocess.Popen(shell, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()

            if process.returncode != 0:
                print("导入失败！")
                print("错误信息：", error)
                return None
            else:
                print("导入成功！")
                # message 显示
                QMessageBox.information(self.toolButton_issue, "成功", "导入成功！")
            print("数据库已导入！")
            QMessageBox.information(self, '提示', '数据库初始化完毕！')

        except Exception as e:
            print(e)
            return None

    # 用于导入数据库
    def import_database(self):
        # 先判断是否登录
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return

        # 提示用户是否进行初始化，是则进行下一步，否则退出
        reply = QMessageBox.question(self, '导入数据库', '请先完成初始化数据库，否则不能继续，已初始化请忽视。',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return

        # 选择文件
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, '选择文件', './', 'SQL Files(*.sql)')
        if file_name == '':
            return
        else:
            file_path = file_name
            # 连接数据库
            dbname = "library"

            try:
                admin_username = get_admin_account()
                admin_password = get_admin_password()

                # 导入数据库,利用source命令
                shell = "mysql -u {} -p{} {} < {}".format(admin_username, admin_password, dbname, file_path)
                process = subprocess.Popen(shell, stdout=subprocess.PIPE, shell=True)
                output, error = process.communicate()

                if process.returncode != 0:
                    print("导入失败！")
                    print("错误信息：", error)
                    return None
                else:
                    print("导入成功！")
                    # message 显示
                    QMessageBox.information(self.toolButton_issue, "成功", "导入成功！")

            except Exception as e:
                print(e)
                QMessageBox.critical(self.toolButton_issue, "错误", "导入失败！请检测是否初始化")
                return None

    # 用于导出数据库
    def export_database(self):
        if log_status() is False:
            print("请先登录！")
            QMessageBox.critical(self.toolButton_issue, "错误", "请先登录！")
            return
        # 选择文件夹
        file_name = QFileDialog.getExistingDirectory(self.centralwidget, '选择文件夹', './')
        if file_name == '':
            return
        else:
            file_path = file_name
            # 连接数据库
            dbname = "library"

            try:
                admin_username = get_admin_account()
                admin_password = get_admin_password()
                if log_status() is False:
                    print("请先登录！")
                    return
                # 导出数据库
                # 使用 sqldump 导出数据库
                shell = "mysqldump -u {} -p{} {} > {}/library.sql".format(admin_username, admin_password, dbname,
                                                                          file_path)
                os.system(shell)
                print("导出成功！")
                # message 显示
                QMessageBox.information(self.toolButton_issue, "成功", "导出成功！")

            except Exception as e:
                print(e)
                QMessageBox.critical(self.toolButton_issue, "错误", "导出失败！")
                return None

    def about(self):
        QMessageBox.about(self, '关于',
                          '关于信息\n开发小组：\n· {}、\n· {}、\n· {}。\n\n版本：v1.0.0\nCopyright (c)：{}'.format(DEVER1,
                                                                                                             DEVER2,
                                                                                                             DEVER3,
                                                                                                             YEAR))

    def help_message(self):
        reply = QMessageBox.question(self, '帮助', '是否打开帮助文档 README ？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # 打开本地文件 :/gallery/doc/index.html
            QDesktopServices.openUrl(QUrl.fromLocalFile('./resource/doc/index.html'))
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
