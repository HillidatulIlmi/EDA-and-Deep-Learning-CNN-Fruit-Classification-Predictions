import streamlit as st
import requests
from PIL import Image
import json
import numpy as np
import tensorflow as tf
from io import BytesIO

img = Image.open('classification-fruits-l.jpg')
st.image(img, width=400, use_column_width=True)
st.title('                           ')

# class fruit classification
list = ['Apple Braeburn','Apple Granny Smith','Apricot','Avocado','Banana','Blueberry','Cactus fruit',
    'Cantaloupe','Cherry','Clementine','Corn','Cucumber Ripe','Grape Blue','Kiwi','Lemon','Limes','Mango','Onion White',
    'Orange','Papaya','Passion Fruit','Peach','Pear','Pepper Green','Pepper Red','Pineapple','Plum','Pomegranate',
    'Potato Red','Raspberry','Strawberry','Tomato','Watermelon']

# predict image
def img_predict(img):
    predict = np.array(img)[:, :, :3]
    predict = tf.image.resize(predict, size=(100, 100))
    predict = predict / 255.0

    image_array = tf.expand_dims(predict, 0)
    image_array = image_array.numpy().tolist()
    
    input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':image_array
                                })
    URL = "https://fruit-backend-ilmi.herokuapp.com/v1/models/fruit_classification:predict" 
    r=requests.post(URL,data= input_data_json)
    result=r.json()

    predict= list[np.array(result['predictions']).argmax()]
    st.write(predict)

# Image Upload Option
choose = st.selectbox("Select Input Method", ["Upload an Image", "URL from Web"])

if choose == "Upload an Image": 
    file = st.file_uploader("Upload a picture of the fruit to be classified", type=["jpg", "png"]) 
    if file is not None:
        img = Image.open(file) 	
else:  
    url = st.text_area("URL", placeholder="Put URL here")
    if url:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
	
# Button of predict
submitted = st.button('Get segmentation map')

st.image(img, width = 400)

if submitted:
    img_predict(img)
