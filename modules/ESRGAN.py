# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:35:24 2021

@author: Mads Emil Marker Jungersen
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import requests
import tensorflow_datasets as tfds
import tensorflow_hub as hub
import tqdm
import os
import shutil
import re
import cv2
import time
import logging
from PIL import Image


def create_ESRGAN_model():
    #Import ESRGAN model
    SAVED_MODEL_PATH = "https://github.com/captain-pool/GSOC/releases/download/1.0.0/esrgan.tar.gz"#"https://tfhub.dev/captain-pool/esrgan-tf2/1"
    model = hub.load(SAVED_MODEL_PATH)
    return model

# Defining helper functions
def downscale_image(image, down_factor = 6):
  """
      Scales down images using bicubic downsampling.
      Args:
          image: 3D or 4D tensor of preprocessed image
  """
  image_size = []
  if len(image.shape) == 3:
    image_size = [image.shape[1], image.shape[0]]
  else:
    raise ValueError("Dimension mismatch. Can work only on single image.")

  image = tf.squeeze(
      tf.cast(
          tf.clip_by_value(image, 0, 255), tf.uint8))

  lr_image = np.asarray(
    Image.fromarray(image.numpy())
    .resize([image_size[0] // down_factor, image_size[1] // down_factor],
              Image.BICUBIC))

  lr_image = tf.expand_dims(lr_image, 0)
  lr_image = tf.cast(lr_image, tf.float32)
  return lr_image

