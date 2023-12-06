
Language: [English](README_en.md) | 中文

## 图书馆信息管理系统

### 1. 项目简介

图书馆信息管理系统是一个基于 PyQt5 的图书馆信息管理系统，主要功能包括：图书信息管理、读者信息管理、借阅信息管理、系统管理等。

### 2. 项目结构

```
application
├─build
│  └─main
├─common
├─dist
│  ├─resource
│  │  └─doc
│  │      └─images
│  └─temp
├─resource
│  ├─doc
│  │  └─images
│  ├─images
│  └─ui
├─temp
└─view
```

### 3. 使用

Python3.9.13 使用通过。

#### 3.1. 安装依赖

```shell
pip install -r requirements.txt
```

#### 3.2. 运行

```shell
python main.py
```

#### 3.3. 打包

```shell
pyinstaller -F -w main.py
```

### 4. 项目截图

![1](resource/doc/images/1.png) 
![2](resource/doc/images/2.png)
![3](resource/doc/images/3.png)
![4](resource/doc/images/4.png)
![5](resource/doc/images/5.png)
