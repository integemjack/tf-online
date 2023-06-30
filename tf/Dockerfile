FROM graphcore/tensorflow:1-amd-ubuntu-18.04

USER root
RUN apt update
RUN apt install wget git curl -y

RUN pip3 uninstall tensorflow tensorboard -y
RUN pip3 install -I absl-py==0.9 jupyter-client==6.1.5 tornado==5.1.0 folium==0.2.1 imgaug==0.2.5 tensorflow==1.13.1 tensorboard==1.13.1

RUN pip3 install jupyterlab
RUN jupyter lab --generate-config
RUN sed -i "s/# c.ServerApp.ip = 'localhost'/c.ServerApp.ip = '0.0.0.0'/g" /root/.jupyter/jupyter_lab_config.py
