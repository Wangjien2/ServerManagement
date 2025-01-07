英伟达GPU A100出现问题，无法正常使用，报错信息如下：
```shell
nvidia-smi # 无法找到驱动
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
```
## 方案一
尝试安装aptitude出现如下报错：
![alt text](/figs/image-1.png)
解决办法：<br />
1) 更换/etc/apt/sources.list镜像源。 <br />
https://blog.csdn.net/qq_31985307/article/details/118163462 <br />
```shell
#### 原始的镜像源
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse

# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换
deb http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse

# 新添加的源
# deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
```
```shell
### 新的源
#网易163
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
```
```shell
### 更新源
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get upgrade
```
在更新源的时候，出现没有公钥签名的错误，需要添加公钥签名。
![alt text](/figs/image3.png)
【上面的问题没有解决！！！】
## 方案二
更新为清华镜像源。网站：https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/ <br />
首先查看自己的ubuntu版本：
```shell
lsb_release -a
# uname -a
```