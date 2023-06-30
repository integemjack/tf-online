# use docker desktop client

1. Download the latest docker client from the docker.com website
2. Double-click the client to install, and restart after the installation is complete
3. If you are using it for the first time and the network environment is not good, you can download the tf.tar image in advance and import it into docker. The tf.tar image address: https://github.com/integemjack/tf-online/releases/download/v1/tf.tar, [the specific process](https://github.com/integemjack/tf-online#import-image)
4. Open cmd on the desktop and run

```bash
docker run --name nvidia --rm -it -p 8888:8888 integem/tf:latest bash -c "cd /home && wget https://raw.githubusercontent.com/integemjack/tf-online/main/aiy_retrain_classification.ipynb && jupyter lab --allow-root"
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
docker save -o <tf.tar absolute path> integem/tf:latest
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
docker pull integem/tf:latest

# Run the mirrored CPU
sudo docker run -it -p 8888:8888 integem/tf:latest

# Run the mirrored GPU [You need to install the latest nvidia driver on your computer]
sudo docker run -it --runtime=nvidia -p 8888:8888 integem/tf:latest
```

