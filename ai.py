import base64
from openai import OpenAI
from sense_hat import SenseHat
import cv2
import time
import os

from background import generate_background, combine_colors
from foreground import generate_foreground

apikey = "sk-None-2TyATAfIKO0R48r8c0k0T3BlbkFJIgUM3IA4gUujQRUsdkxM"
client = OpenAI(api_key=apikey)

ERROR_RATING = -1

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

while True:
  cap = cv2.VideoCapture(0)
  if cap.isOpened():
    ret, frame = cap.read()
    if ret:
      print("Frame captured")
      os.remove("./out/image.jpg")
      cv2.imwrite("./out/image.jpg", frame)
      image_path = "./out/image.jpg"
      base64_image = encode_image(image_path)

      response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "Rate the health of this plant from 1-8. If there is no plant in the image, give me back -1. Only give me a number back. Do not give me back ANYTHING else",
              },
              {
                "type": "image_url",
                "image_url": {
                  "url":  f"data:image/jpeg;base64,{base64_image}"
                },
              },
            ],
          }
        ],
      )

      rating = int(response.choices[0].message.content)
      print("GPT Response: " + str(rating))
      background = generate_background(rating)
      foreground = generate_foreground(rating)

      if rating == ERROR_RATING:
        display = background
      else:
        display = combine_colors(background, foreground)

      sense = SenseHat()
      sense.set_pixels(display)

    else:
      print("Failed to capture frame")
  cap.release()
  time.sleep(10)

