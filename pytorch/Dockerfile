FROM graphcore/pytorch-jupyter:latest

RUN apt update
RUN apt install wget git curl -y
RUN pip3 install jupyterlab boto3 pandas tensorboard torchvision opencv-contrib-python
RUN jupyter lab --generate-config
RUN sed -i "s/# c.ServerApp.ip = 'localhost'/c.ServerApp.ip = '0.0.0.0'/g" /root/.jupyter/jupyter_lab_config.py

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install build-essential cmake pkg-config -y
RUN apt-get install libjpeg-dev libtiff5-dev libjasper-dev -y
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
RUN apt-get install libxvidcore-dev libx264-dev -y
RUN apt-get install libgtk-3-dev -y
RUN apt-get install libatlas-base-dev gfortran -y
RUN apt-get install python2.7-dev python3.5-dev -y

RUN apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-tools -y

RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
RUN unzip opencv.zip

RUN cd opencv-4.5.0
RUN mkdir build
RUN cd build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D WITH_GSTREAMER=ON \
      ..
RUN make -j4
RUN make install
RUN ldconfig
