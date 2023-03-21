import cv2
import torch
from tqdm import tqdm
import numpy as np
import time


class Detection():
    def __init__(self, model):
        self.model = model
        
    def get_detected_img(self, img_path):
        img = cv2.imread(img_path)

        result = self.model(img)

        return result
    
    def get_video(self, video_path, output_path):

        vfile = cv2.VideoCapture(video_path)

        codec =cv2.VideoWriter_fourcc(*'XVID')

        vid_size = (round(vfile.get(cv2.CAP_PROP_FRAME_WIDTH)),round(vfile.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        vid_fps = vfile.get(cv2.CAP_PROP_FPS)

        vid_writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size) 
        
        frame_cnt = int(vfile.get(cv2.CAP_PROP_FRAME_COUNT))
        print('총 Frame 갯수:', frame_cnt)

        while True:
            vret, img = vfile.read()
            if not vret:
                print('더 이상 처리할 frame이 없습니다.')
                break
            img = self.model(img)
            result_img = img.render()[0]
            vid_writer.write(result_img)
        
        vid_writer.release()
        vfile.release()
        