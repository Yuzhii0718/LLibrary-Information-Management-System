
Language: English | [中文](README.md)

## Library Information Management System

**note: Chinese version only**

### 1. Introduction

Library Information Management System is a library information management system based on PyQt5. The main functions include: book information management, reader information management, borrowing information management, system management, etc.

### 2. Project Structure

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

### 3. Usage

Python3.9.13 is used to pass.
MySQL 8.0.33/35 is used to pass.

#### 3.1. Install dependencies

It is suggested to install in virtual environment.

```shell
pip install -r requirements.txt
```

#### 3.2. Run

```shell
python main.py
```

#### 3.3. Package

```shell
pyinstaller -F -w main.py
```

### 4. Screenshots

![1](resource/doc/images/1.png)
![2](resource/doc/images/2.png)
![3](resource/doc/images/3.png)
![4](resource/doc/images/4.png)
![5](resource/doc/images/5.png)
