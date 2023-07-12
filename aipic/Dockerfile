FROM huggingface/transformers-pytorch-gpu:4.23.0

WORKDIR /app

COPY ./server.py ./server.py

RUN pip3 install diffusers
RUN pip3 install flask_cors

ENTRYPOINT ["python", "/app/server.py"]