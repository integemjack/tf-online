import cv2
import os
import datetime
import random
import ipywidgets
import traitlets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg
from jupyter_clickable_image_widget import ClickableImageWidget


CATEGORIES = ['car', 'mouse', 'remote']

top = True
topX = -1
topY = -1
bottomX = -1
bottomY = -1

data = "custom"
Annotations = "./data/" + data + "/Annotations/"
ImageSets = "./data/" + data + "/ImageSets/Main/"
ImageSetsTrain = ImageSets + "train.txt"
ImageSetsTrainval = ImageSets + "trainval.txt"
JPEGImages = "./data/" + data + "/JPEGImages/"
labels = "./data/" + data + "/labels.txt"

# 检查并创建目录
directories = [Annotations, ImageSets, JPEGImages]

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# unobserve all callbacks from camera in case we are running this cell for second time
camera.unobserve_all()

# create image preview
camera_widget = ClickableImageWidget(width=camera.width, height=camera.height)


with open("../images/ready_img.jpg", "rb") as file:
    default_image = file.read()
snapshot_widget = ipywidgets.Image(value=default_image, width=camera.width, height=camera.height)
# traitlets.dlink((camera, 'value'), (camera_widget, 'value'), transform=bgr8_to_jpeg)
def darm(camera):
    snapshot = camera.copy()
    if bottomX >= 0 & bottomY >= 0:
        snapshot = cv2.rectangle(snapshot, (topX, topY), (bottomX, bottomY), (0, 255, 0, 255), 4)
    else:
        snapshot = cv2.circle(snapshot, (topX, topY), 4, (0, 255, 0), 3)
    return bgr8_to_jpeg(snapshot)
traitlets.dlink((camera, 'value'), (camera_widget, 'value'), transform=darm)

# create widgets
category_widget = ipywidgets.Dropdown(options=CATEGORIES, description='category')

top_x_widget = ipywidgets.IntText(description='Top X:')
top_y_widget = ipywidgets.IntText(description='Top Y:')
bottom_x_widget = ipywidgets.IntText(description='Bottom X:')
bottom_y_widget = ipywidgets.IntText(description='Bottom Y:')

def update_top_x_widget(change):
    global topX
    topX = change['new']
top_x_widget.observe(update_top_x_widget, names='value')

def update_top_y_widget(change):
    global topY
    topY = change['new']
top_y_widget.observe(update_top_y_widget, names='value')

def update_bottom_x_widget(change):
    global bottomX
    bottomX = change['new']
bottom_x_widget.observe(update_bottom_x_widget, names='value')

def update_bottom_y_widget(change):
    global bottomY
    bottomY = change['new']
bottom_y_widget.observe(update_bottom_y_widget, names='value')

# update counts when we select a new category

def save_snapshot(_, content, msg):
    global top,topX,topY,bottomX,bottomY
    print(content['event'])
    if content['event'] == 'click':
        data = content['eventData']
        if top:
            topX = data['offsetX']
            topY = data['offsetY']
            top_x_widget.value = topX
            top_y_widget.value = topY
            top = False
        else:
            bottomX = data['offsetX']
            bottomY = data['offsetY']
            bottom_x_widget.value = bottomX
            bottom_y_widget.value = bottomY
            top = True
        

        
camera_widget.on_msg(save_snapshot)

# Add this to create a button for saving images
save_button = ipywidgets.Button(description='Save Image')

# Add this to define a function that will be called when the button is clicked
def save_image(b):
    global data, camera, topX, topY, bottomX, bottomY, category_widget
    
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y%m%d")

    # 生成10位随机数
    random_number = random.randint(1000000000, 9999999999)

    # 构建文件名
    filename = f"{current_time}_{random_number}"
    
    cv2.imwrite(JPEGImages + filename+'.jpg', camera.value)
    
    # Save the bounding box coordinates and category to a text file
    with open(Annotations + filename + '.xml', 'a') as txtfile:  # Change 'data.txt' to your desired filename
        # Write the data for this image
        txtfile.write(f"""<annotation>
    <filename>{filename}</filename>
    <folder>{data}</folder>
    <source>
        <database>{data}</database>
        <annotation>{data}</annotation>
        <image>{data}</image>
    </source>
    <size>
        <width>{camera.width}</width>
        <height>{camera.height}</height>
        <depth>{camera.value.shape[2]}</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>{category_widget.value}</name>
        <pose>unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>{topX}</xmin>
            <ymin>{topY}</ymin>
            <xmax>{bottomX}</xmax>
            <ymax>{bottomY}</ymax>
        </bndbox>
    </object>
</annotation>""")  # Separate entries with a blank line
        # 打开文件以追加写入模式
    with open(ImageSetsTrain, "a") as file:
        # 写入新的文本行
        file.write(filename+"\n")
    
    with open(ImageSetsTrainval, "a") as file:
        # 写入新的文本行
        file.write(filename+"\n")
    
    print('Image saved.')

# Add this to make the button call the function when clicked
save_button.on_click(save_image)

data_collection_widget = ipywidgets.VBox([
    ipywidgets.HBox([camera_widget, ]),
    category_widget,
    ipywidgets.HBox([top_x_widget, top_y_widget,]),
    ipywidgets.HBox([bottom_x_widget, bottom_y_widget]),
    save_button
])

display(data_collection_widget)
print("data_collection_widget created")