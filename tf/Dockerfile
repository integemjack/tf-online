FROM tensorflow/tensorflow:1.13.1-jupyter

RUN apt update
RUN apt install wget -y
RUN rm -rf /tf/*
RUN wget -O /tf/aiy_retrain_classification.ipynb https://raw.githubusercontent.com/integemjack/tf-online/main/aiy_retrain_classification.ipynb
