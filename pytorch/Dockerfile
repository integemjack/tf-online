FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

RUN apt update
RUN apt install wget git curl libgl1-mesa-glx libglib2.0-0 -y
RUN pip3 install jupyterlab boto3 pandas tensorboard torchvision opencv-contrib-python
RUN jupyter lab --generate-config
RUN sed -i "s/# c.ServerApp.ip = 'localhost'/c.ServerApp.ip = '0.0.0.0'/g" /root/.jupyter/jupyter_lab_config.py
