from cv2 import cv2 as cv
import argparse
import glob
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--video_dir")
args = parser.parse_args()
params = vars(args)

videoList = glob.glob(os.path.join(params['video_dir'], '*.mp4'))
videoList += glob.glob(os.path.join(params['video_dir'], '*.avi'))
videoList.sort()
frame = []

for video in videoList:
    cap = cv.VideoCapture(video)
    frame.append(cap.get(7))

print('median frame num:', np.median(frame))
print('average frame num:', np.mean(frame))
