FROM jupyter/tensorflow-notebook:lab-4.0.2

USER root
RUN apt update
RUN apt install wget git curl -y
# RUN curl https://pyenv.run | bash
# RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"\n' >> ~/.bashrc
# RUN echo 'eval "$(pyenv init -)"\n' >> ~/.bashrc
# RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
# RUN source ~/.bashrc

# RUN pip3 install jupyterlab
# RUN jupyter lab --generate-config
# RUN sed -i "s/# c.ServerApp.ip = 'localhost'/c.ServerApp.ip = '0.0.0.0'/g" /root/.jupyter/jupyter_lab_config.py
RUN rm -rf /home/jovyan/*
RUN wget -O /home/jovyan/aiy_retrain_classification.ipynb https://raw.githubusercontent.com/integemjack/tf-online/main/aiy_retrain_classification.ipynb
