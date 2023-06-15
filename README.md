# 使用 docker 桌面客户端

1. 在 docker.com 网站上下载最新的 docker 客户端
2. 双击客户端安装，待安装完成重启后
3. 在桌面打开 cmd，运行

```bash
docker run --name nvidia --rm -it -v <user tf folder>:/tf -p 8888:8888 tensorflow/tensorflow:1.13.1-jupyter
# like: docker run --name nvidia --rm -it -v C:\Users\zehon\OneDrive\Desktop\tf:/tf -p 8888:8888 tensorflow/tensorflow:1.13.1-jupyter
```

4. 获取 token 地址，比如：

```bash
# http://(d57d8a94448a or 127.0.0.1):8888/?token=b0629e8a2dbabe858d9f93c37878a3eecafe23c80d30
# 将这个链接转化成
# http://127.0.0.1:8888/?token=b0629e8a2dbabe858d9f93c37878a3eecafe23c80d30
```

5. 打开 colab 地址：https://colab.research.google.com/github/google/aiyprojects-raspbian/blob/aiyprojects/tutorials/vision/aiy_retrain_classification.ipynb
6. 登录谷歌账号
7. 点击右上角 connect 旁边的倒三角，选择 connect to a local runtime
8. 将上面获取的链接 填在下面并点击 connect
9. 到此已经完成，可以在 colab 里使用本地 jupyter 操作，生成的文件在你上面设置的目录里


## ------------------------------------------------------------------------

# 导出镜像

在一个目录里面打开 cmd，运行下面命令就可以在当前目录生成 tf.tar 镜像文件

```bash
docker save -o tf.tar tensorflow/tensorflow:1.13.1-jupyter
```

# 导入镜像

进入的你的 U 盘目录，打开 cmd

```bash
docker load -i tf.tar
```

## ------------------------------------------------------------------------


# 普通方式安装
## 第一步

1. 以管理员方式运行 PowerShell

```bash
# 启动 windows 的子系统
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 下载ubuntu系统
wsl --install
# 设置 wsl 为 2
wsl --set-default-version 2

```

2. 在开始菜单中找到 ubuntu，并打开进行初始化，设置账号和密码

# 第二步

1. 在第一步的基础上

```bash
# 更新系统
sudo apt update
sudo apt install docker.io

# 安装gpu支持
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# 下载镜像
docker pull tensorflow/tensorflow:1.13.1-gpu-jupyter

# 运行镜像 CPU
sudo docker run -it -p 8888:8888 tensorflow/tensorflow:1.13.1-gpu-jupyter

# 运行镜像 GPU 【需要你的计算机安装最新的nvidia驱动】
sudo docker run -it --runtime=nvidia -p 8888:8888 tensorflow/tensorflow:1.13.1-gpu-jupyter
```

2. 查看生成的地址，就可以在网页中打开使用

3. 打开 https://colab.research.google.com/github/google/aiyprojects-raspbian/blob/aiyprojects/tutorials/vision/aiy_retrain_classification.ipynb 下载到本地

4. 将下载的文件上传到 jupyter 上

