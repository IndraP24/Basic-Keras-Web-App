import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image

st.title('ResNet50 Image Classification on ImageNet')

# fastapi endpoint
url = 'http://localhost:8000'
endpoint = '/predict'

# description and instructions
st.markdown('''Upload an image and get the results of classification on it using the ResNet50 model architecture trained on the ImageNet dataset.
         This streamlit app uses a FastAPI service as backend.
         Visit this URL at [localhost:8000/docs](http://localhost:8000/docs) for FastAPI - Swagger UI documentation.''')

# image upload widget
image = st.file_uploader('Insert Image Here')

def process(image, server_url: str):

    m = MultipartEncoder(
        fields={'file': ('filename', image, 'image/jpeg')}
        )

    r = requests.post(server_url,
                      data=m,
                      headers={'Content-Type': m.content_type})

    return r


if st.button('Predict'):

    if image == None:
        st.write("Insert an image!")  # handle case with no image
    else:
        # File details
        st.subheader("File Details")
        file_details = {"FileName": image.name,"FileType": image.type,"FileSize":image.size}
        st.write(file_details)

        # File content
        #files = {"file": image.get}

        col1, col2 = st.beta_columns(2)

        # Show original image
        original_image = Image.open(image)
        col1.header("Image")
        col1.image(original_image, use_column_width=True)
        
        # Post to server
        res = process(image, url+endpoint)
        # processed_image = Image.open(io.BytesIO(res.content))
        # col2.image(processed_image, use_column_width=True)
        col2.header("Prediction")
        result = res.content.decode("utf-8")
        col2.json(str(result))
        Class = result.split('"')[7].capitalize()
        col2.markdown("### Predicted Class: " + Class)