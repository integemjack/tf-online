# use docker desktop client

1. Download the latest docker client from the docker.com website
2. Double-click the client to install, and restart after the installation is complete
3. If you are using it for the first time and the network environment is not good, you can download the tf.tar image in advance and import it into docker. The tf.tar image address: https://github.com/integemjack/tf-online/releases/download/v1/tf.tar, [the specific process](https://github.com/integemjack/tf-online#import-image)
4. Open cmd on the desktop and run

```bash
docker run --name nvidia --rm -it -p 8888:8888 integem/tf:latest
```

5. Get the token address, for example:

```bash
# http://(d57d8a94448a or 127.0.0.1):8888/?token=b0629e8a2dbabe858d9f93c37878a3eecafe23c80d30
# convert this link to
# http://127.0.0.1:8888/?token=b0629e8a2dbabe858d9f93c37878a3eecafe23c80d30
```


## ------------------------------------------------------------------------

# export image

Open cmd and run the following command to generate a tf.tar image file in the set directory

```bash
docker save -o <tf.tar absolute path> tensorflow/tensorflow:1.13.1-jupyter
```

# import image

You can download the tf.tar file through https://github.com/integemjack/tf-online/releases/download/v1/tf.tar, or you can get tf.tar through the above export

```bash
docker load -i <tf.tar absolute path>
```

## ------------------------------------------------------------------------


# Normal installation
## first step

1. Run PowerShell as Administrator

```bash
# Start the windows subsystem
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Download the ubuntu system
wsl --install

# set wsl to 2
wsl --set-default-version 2

```

2. Find ubuntu in the start menu, open it for initialization, and set the account and password

# second step

1. Building on the first step

```bash
# update system
sudo apt update
sudo apt install docker.io

# Install gpu support
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# Download mirror
docker pull tensorflow/tensorflow:1.13.1-gpu-jupyter

# Run the mirrored CPU
sudo docker run -it -p 8888:8888 tensorflow/tensorflow:1.13.1-gpu-jupyter

# Run the mirrored GPU [You need to install the latest nvidia driver on your computer]
sudo docker run -it --runtime=nvidia -p 8888:8888 tensorflow/tensorflow:1.13.1-gpu-jupyter
```

2. View the generated address, you can open it on the web page

3. Open <a href="https://colab.research.google.com/github/integemjack/tf-online/blob/main/aiy_retrain_classification.ipynb" target="_blank">![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)</a> and download it locally

4. Upload the downloaded file to jupyter

