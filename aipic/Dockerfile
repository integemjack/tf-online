FROM huggingface/transformers-pytorch-gpu:4.29.2

WORKDIR /app

COPY ./server.py ./server.py

RUN pip3 install diffusers flask flask_cors accelerate

# RUN apt update
# RUN apt install python3 python3-pip -y
# RUN pip3 install diffusers
# RUN pip3 install flask
# RUN pip3 install flask_cors
# RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
# RUN pip3 install transformers
# RUN pip3 install accelerate

# RUN apt update && apt install curl wget -y
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# RUN bash Miniconda3-latest-Linux-x86_64.sh -b
# RUN echo export PATH="/root/miniconda3/bin:$PATH" >> ~/.bashrc
# RUN source ~/.bashrc
# RUN conda create --name py36_torch python=3.6 -y
# RUN conda activate py36_torch
# RUN conda init bash
# RUN conda install pytorch torchvision torchaudio -c pytorch -y
# RUN pip3 install diffusers flask flask_cors accelerate transformers


# apt update && apt install curl wget -y
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# bash Miniconda3-latest-Linux-x86_64.sh -b
# echo export PATH="/root/miniconda3/bin:$PATH" >> ~/.bashrc
# source ~/.bashrc
# conda create --name py36_torch python=3.6 -y
# conda activate py36_torch
# conda init bash
# conda install pytorch torchvision torchaudio -c pytorch -y
# pip3 install diffusers flask flask_cors accelerate transformers
# cd /home
# python3 server.py


# apt update && apt install python3 python3-pip -y && pip3 install diffusers && pip3 install flask && pip3 install flask_cors && pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117 && pip3 install transformers && pip3 install accelerate

ENTRYPOINT ["python3", "/app/server.py"]
