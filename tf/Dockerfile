FROM tensorflow/tensorflow:1.13.1

RUN apt update
RUN apt update
RUN apt install wget git curl -y
RUN pip3 install jupyterlab boto3 pandas tensorboard torchvision opencv-contrib-python
RUN jupyter lab --generate-config
RUN sed -i "s/# c.ServerApp.ip = 'localhost'/c.ServerApp.ip = '0.0.0.0'/g" /root/.jupyter/jupyter_lab_config.py
RUN rm -rf /tf/*
# RUN wget -O /tf/aiy_retrain_classification.ipynb https://raw.githubusercontent.com/integemjack/tf-online/main/aiy_retrain_classification.ipynb
