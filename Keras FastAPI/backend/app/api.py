# import the necessary packages
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from PIL import Image
import numpy as np

from fastapi import FastAPI
import io


app = FastAPI(title="Keras ImageNet Web App")


@app.get("/", tags=["root"])
async def read_root():
    return {
        "message": "Head over to /predict"
    }
