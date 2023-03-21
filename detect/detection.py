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

        codec =cv2.VideoWriter_fourcc(*'mp4v')

        vid_size = (round(vfile.get(cv2.CAP_PROP_FRAME_WIDTH)),round(vfile.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        vid_fps = vfile.get(cv2.CAP_PROP_FPS)

        vid_writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size) 
        
        frame_cnt = int(vfile.get(cv2.CAP_PROP_FRAME_COUNT))
        print('총 Frame 갯수:', frame_cnt)

        with tqdm(total=frame_cnt, desc="Processing", unit="frame") as pbar:
            while vfile.isOpened(): # 비디오캡쳐 객체가 열렸는지 확인
                ret, frame = vfile.read() 
                # 재생되는 비디오의 한 프레임씩 읽음. 프레임을 읽었다면 ret : True, 읽은 프레임 : frame
                if not ret: # 새로운 프레임을 못 받아 왔을때 break (ret이 False면 중지)
                    break
                results = self.model(frame)
                result_frame = results.render()[0]
                vid_writer.write(result_frame) # 프레임 저장
                pbar.update(1)

        # while True:
        #     vret, img = vfile.read()
        #     if not vret:
        #         print('더 이상 처리할 frame이 없습니다.')
        #         break
        #     img = self.model(img)
        #     result_img = img.render()[0]
        #     vid_writer.write(result_img)
        
        vid_writer.release()
        vfile.release()
        cv2.destroyAllWindows()
        