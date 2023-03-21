import torch
import sys

sys.path.append('./detect')
from detection import Detection


# models의 가중치(best.pt)의 경로.
model_path = './models/my_yolov5s.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False, trust_repo=True)


# 검증 할 영상의 경로를 입력하세요. 샘플영상이 없다면 sample폴더의 영상을 사용하세요.
input_video = './samples/sample1.mp4'


# 결과영상의 저장이름을 지정해주세요.(results폴더에 저장 됨)
output_video = './results/output_video1.mp4'


detect = Detection(model=model)

detect.get_video(input_video, output_video)



# 결과영상 파일은 /results 폴더에 있습니다.