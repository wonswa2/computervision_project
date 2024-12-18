# 6-5.py : 파노라마 영상 및 얼굴 인식 프로젝트


# 1. 개발 목적
 이 프로젝트는 실시간 영상 스트림을 통해 얼굴을 인식하고, 얼굴 위에 오버레이 이미지를 필터처럼 적용하여 파노라마 영상을 만드는 프로그램입니다. 
얼굴 인식 기술을 활용하여 코 위치에 크리스마스 루돌프 코 이미지를 오버레이하고, 수집된 이미지를 합성하여 하나의 파노라마 영상을 생성하는 것이 주요 목표입니다.

# 2. 구체적 구현 내용
1) 얼굴 인식 및 오버레이 이미지 적용
 얼굴 인식: OpenCV의 Haar Cascade Classifier를 사용하여 실시간 영상에서 얼굴을 인식합니다. haarcascade_frontalface_default.xml을 이용해 얼굴을 감지합니다.
오버레이 이미지 적용: 얼굴 인식 후 코의 위치를 추출하고, 해당 위치에 지정된 이미지를 오버레이 필터처럼 적용합니다. 이 필터 이미지는 .png 형식으로 로드되며, 투명도를 처리하여 원본 영상 위에 자연스럽게 합성됩니다.

2) 영상 수집 및 파노라마 제작
 영상 수집: c 키를 눌러 영상 프레임을 수집하고, 수집이 완료되면 q 키로 영상 수집을 종료합니다. 수집된 영상은 imgs 리스트에 저장됩니다.
파노라마 제작: OpenCV의 Stitcher 모듈을 사용하여 수집된 이미지를 자동으로 합성하여 하나의 파노라마를 생성합니다.
합성된 파노라마는 화면에 표시되고, 성공적인 합성 여부를 사용자에게 알립니다.

3) 영상 저장 및 동영상 저장
 이미지 저장: 생성된 파노라마 이미지를 로컬 디스크에 .jpg 또는 .png 형식으로 저장할 수 있습니다.
 동영상 저장: 파노라마 이미지를 동영상으로 저장하는 기능도 제공합니다. 동영상은 output.avi 형식으로 저장됩니다.

# 3. 개발 환경
1) 운영 체제
 Windows 10 이상
2) 필수 라이브러리
 PyQt5: GUI 개발을 위한 프레임워크
 OpenCV: 이미지 처리 및 얼굴 인식을 위한 라이브러리
 NumPy: 이미지 배열을 처리하기 위한 라이브러리

 3) 라이브러리 설치 방법
다음 명령어를 사용하여 필수 라이브러리를 설치할 수 있습니다:
# pip install pyqt5 opencv-python numpy

# 4. 실행 방법
1) 코드에서 haarcascade_frontalface_default.xml 파일이 필요한데, 이 파일은 OpenCV의 Haar Cascade 분류기에서 제공하는 얼굴 인식 모델입니다. 이 파일은 OpenCV 설치 시 자동으로 제공됩니다.
2) 필터 이미지(nose.png)는 자신의 환경에 맞게 준비하고 경로를 수정해야 합니다.
3) 프로젝트 실행을 위해, 6-5.py 파일을 실행합니다.
# python 6-5.py
4) 프로그램 실행 후:
영상 수집: c 키를 눌러 여러 장의 영상을 수집합니다.
영상 보기: 영상 보기 버튼을 눌러 수집된 이미지를 확인합니다.
파노라마 봉합: 봉합 버튼을 눌러 파노라마를 생성합니다.
이미지 저장: 저장 버튼을 눌러 파노라마 이미지를 저장합니다.
동영상 저장: 동영상 저장 버튼을 눌러 파노라마 이미지를 동영상으로 저장합니다.

# 5. 주의 사항
카메라 연결: 카메라가 연결되어 있어야 하며, 연결되지 않으면 프로그램이 종료됩니다.
필터 이미지 경로: 필터 이미지는 .png 형식이어야 하며, 투명도를 포함한 이미지를 사용해야 합니다.
파노라마 생성: 충분히 다양한 각도에서 이미지를 수집해야 파노라마 합성이 잘 이루어집니다.
