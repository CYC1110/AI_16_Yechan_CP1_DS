# 과적 탐지 모델 

## 과적 차량을 인식하여 단속하는 서비스
화물차의 과적운행은 고속도로의 안전과 보수에 문제를 일으키기 때문에 단속이 필요합니다.

저는 ‘YOLOv5를 이용하여 영상에서 과적 차량을 박스로 표시하는 서비스를 만드는 프로젝트’를 해보았습니다.


### 폴더 설명

- samples : 이후 모델 검증에 사용할 샘플 영상이 들어있습니다.

- models : 사전학습 모델인 my_yolov5s.pt와 이를 ONNX형태로 저장한 my_yolov5.onnx가 있습니다.

- detect : models 내 모델을 통해 영상 내 객체를 탐지하는 object detection을 진행하고 결과를 .mp4 형태로 생성하는 detection 모듈이 저장되어 있습니다.

- results : test.py혹은 test.ipynb에 의해 생성된 결과 영상이 해당 폴더에 저장되게 됩니다.

- test : 해당 패키지가 정상적으로 작동하는지 확인하는 test.py와 test.ipynb 파일을 포함하고 있습니다. test.ipynb는 아직 미완성입니다.


### 패키지를 이용해 과적차량(불법차량)을 감지해봅시다. 

1. 먼저 이 레포지토리를 클론해주세요.

  -  `git clone https://github.com/CYC1110/AI_16_Yechan_CP1_DS.git`

2. 해당폴더에 들어간 후(`cd AI_16_Yechan_CP1_DS`) python=3.8로 가상환경을 만들고,

  - `pip install -r requirements.txt` 필요한 라이브러리와 모듈을 설치합니다.

3. test.py 파일을 연 후 검증할 영상의 경로와 결과영상의 저장이름을 지정해주고 실행합니다.

4. 결과영상은 results 폴더에 있습니다.
