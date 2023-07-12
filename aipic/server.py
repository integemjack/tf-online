from io import BytesIO
from diffusers import StableDiffusionPipeline
import torch
from flask import Flask, request, send_file, Response
from flask import render_template, make_response
import sys
import os
from flask_cors import CORS
import json
import base64

grand_parentdir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(grand_parentdir)
print(sys.path)

# import logic_function_module as logic_class  # 逻辑函数类
app = Flask(__name__)

CORS(app, resources=r'/*')  # 新增

# AI

# make sure you're logged in with `huggingface-cli login`
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)
# pipe = pipe.to("cuda")


@app.route('/call/<function_name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def call_function(function_name: str):
    # function_to_call = getattr(logic_class, function_name) # 指定调用逻辑函数类中的某个逻辑函数
    print(function_name)
    # body = request.json
    # print(body)
    prompt = "a photograph of an astronaut riding a horse"
    result = pipe(prompt)
    # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
    image = result.images[0]

    img_io = BytesIO()
    image.save(img_io, format='PNG')
    img_io.seek(0)
    # return Response(img_io.getvalue(), mimetype='image/PNG')
    headers = {
        'Content-Type':'text/html'
    }
    return base64.b64encode(img_io.getvalue()), 200, headers


app.run(host="0.0.0.0", port=5000, debug=True)  # 改了代码他能自动重启
