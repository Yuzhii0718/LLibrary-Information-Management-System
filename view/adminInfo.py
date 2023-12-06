# coding:utf-8
"""
**************************************************
@File   ：PyQt5_QuickStart -> adminInfo
@IDE    ：PyCharm
@Author ：Yuzhii0718
@Date   ：2023/8/21 22:48
@Update ：2023/12/6 19:05
@Status : undefined
**************************************************
"""

# 工具类，获取管理员账号密码，无需Gui
# 接收传参，返回账号密码

# 假如 从其他地方使用 id = adminInfo.get_admin_account(), password = adminInfo.get_admin_password()
# 则 id = 'admin', password = 'admin'


def get_admin_account():
    # 从文件中读取账号
    with open('./temp/adminInfo.txt', 'r') as f:
        admin_account = f.readline().split(' ')[0]
    return admin_account


def get_admin_password():
    # 从文件中读取密码
    with open('./temp/adminInfo.txt', 'r') as f:
        admin_password = f.readline().split(' ')[1]
    return admin_password


def clear_adminInfo():
    with open('./temp/adminInfo.txt', 'w') as f:
        f.write('admin admin')
    print('./temp/adminInfo.txt 已清空！')


def log_status():
    account = get_admin_account()
    password = get_admin_password()
    if account == 'admin' and password == 'admin':
        return False


class adminInfo:
    def __init__(self, admin_account, admin_password):
        super().__init__()
        self.adminAccount = admin_account
        self.adminPassword = admin_password
        self.temp_save()
        get_admin_account()
        get_admin_password()

    def temp_save(self):
        # 创建一个文件，保存账号密码,格式为 admin admin
        with open('./temp/adminInfo.txt', 'w') as f:
            f.write(f'{self.adminAccount} {self.adminPassword}')

    def __str__(self):
        return f'admin_account: {self.adminAccount}, admin_password: {self.adminPassword}'

    def __repr__(self):
        return f'admin_account: {self.adminAccount}, admin_password: {self.adminPassword}'
