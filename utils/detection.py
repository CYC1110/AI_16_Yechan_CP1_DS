import cv2
import torch
from tqdm import tqdm


def detection(input_video, output_video, model):
    cap = cv2.VideoCapture(input_video)
    width, height, fps, total_frames = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(
        cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FPS)), int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(model(frame).render()[0])
            pbar.update(1)
            
    cap.release()
    out.release()
    cv2.destroyAllWindows()
