import cv2
import torch
import numpy as np
from PIL import ImageGrab

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/bismutoso/Documentos/MedusaVision100.pt')

while True:
    screen = ImageGrab.grab(bbox=(1450, 80, 1870, 816))
    results = model(screen)

    #  Squeeze remove 1 channel, which makes readable to cv2
    array = np.squeeze(results.render())
    rgb = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)

    cv2.imshow("Medusa Vision", rgb)
    cv2.moveWindow("Medusa Vision", 1020, 10)

    key = cv2.waitKey(20) & 0xFF
    if key == ord("x"):
        break
