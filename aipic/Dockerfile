FROM nvidia/cuda:11.7.1-devel-ubi8

WORKDIR /app

COPY ./server.py ./server.py

RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install diffusers
RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
RUN pip3 install transformers
RUN pip3 install accelerate


ENTRYPOINT ["python3", "/app/server.py"]