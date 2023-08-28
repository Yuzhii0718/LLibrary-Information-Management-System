# coding:utf-8
"""
**************************************************
@File   ：PyQt6_QuickStart -> bookStatus
@IDE    ：PyCharm
@Author ：Yuzhii0718
@Date   ：2023/8/27 23:52
@Status : undefined
**************************************************
"""
import mysql.connector as mc
from adminInfo import get_admin_account, get_admin_password, log_status


# Part I
# 用于判断账号是否存可用
# 接收传参，返回布尔值
# 假如 从其他地方使用 bookStatus.is_account_available(book)
# 则从数据库中查询账号是否可用，存在返回True，不存在返回False，数据库连接失败返回None

class bookStatus:
    def __init__(self, book):
        super().__init__()
        self.book = book
        self.is_book_existed()
        self.is_book_available()

    def is_book_existed(self):
        dbname = "library"
        tablename = "tbl_addbook"

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            mycursor.execute("select * from {} where bookid = '{}'".format(tablename, self.book))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            else:
                return True

        except Exception as e:
            print(e)
            return None

    def is_book_available(self):
        dbname = "library"
        tablename = "tbl_addbook"

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            # 查询 isAvail 字段，如果为 1 则返回 True，否则返回 False
            mycursor.execute("select * from {} where bookid = '{}' and isAvail = 1".format(tablename, self.book))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            else:
                return True

        except Exception as e:
            print(e)
            return None


class accountStatus:
    def __init__(self, account):
        super().__init__()
        self.account = account
        self.is_account_existed()
        self.is_account_available()

    def is_account_existed(self):
        dbname = "library"
        tablename = "tbl_addaccount"

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            mycursor.execute("select * from {} where accountID = '{}'".format(tablename, self.account))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            else:
                return True

        except Exception as e:
            print(e)
            return None

    def is_account_available(self):
        dbname = "library"
        tablename = "tbl_addaccount"

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            # 查询 isAvail 字段，如果为 1 则返回 True，否则返回 False
            mycursor.execute("select * from {} where accountID = '{}' and isAvail = 1".format(tablename, self.account))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            else:
                return True

        except Exception as e:
            print(e)
            return None


# Part II
# 用于给账号的 limit 字段赋值
# 接收传参，返回布尔值
# 例如，从其他地方使用 accountLimit.set_account_limit_plus(account)
# 则给 account 账号的 limit 字段 +1，成功返回 True，失败返回 False，数据库连接失败返回 None

class accountLimit:
    def __init__(self, account):
        super().__init__()
        self.account = account
        self.set_account_limit_plus()
        self.set_account_limit_minus()

    def set_account_limit_plus(self):
        dbname = "library"
        tablename = "tbl_addaccount"
        limitation = 5

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            # 先判断 limit 是否为 5，如果为 5 则不执行加法操作
            mycursor.execute(
                "select * from {} where accountID = '{}' and limit = '{}'".format(tablename, self.account, limitation))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            mycursor.execute("update {} set limit = limit + 1 where accountID = '{}'".format(tablename, self.account))
            mydatabase.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def set_account_limit_minus(self):
        dbname = "library"
        tablename = "tbl_addaccount"

        try:
            admin_username = get_admin_account()
            admin_password = get_admin_password()
            if log_status() is False:
                print("请先登录！")
                return

            mydatabase = mc.connect(
                host="localhost",
                user="{}".format(admin_username),
                password="{}".format(admin_password),
                database="{}".format(dbname)
            )

            mycursor = mydatabase.cursor()
            # 先判断 limit 是否为 0，如果为 0 则不执行减法操作
            mycursor.execute("select * from {} where accountID = '{}' and limit = 0".format(tablename, self.account))
            myresult = mycursor.fetchall()
            if myresult is None:
                return False
            mycursor.execute("update {} set limit = limit - 1 where accountID = '{}'".format(tablename, self.account))
            mydatabase.commit()
            return True

        except Exception as e:
            print(e)
            return False
