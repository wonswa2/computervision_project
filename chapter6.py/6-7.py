import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPixmap
import sys
import random
import math

class VideoSpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오 특수 효과')
        
        # 배경 이미지 설정
        self.background_image_path = 'C:/Users/82105/cv/chapter6.py/xmas.jpg'  # 배경 이미지 경로
        self.background_pixmap = QPixmap(self.background_image_path)
        
        # 배경 이미지 크기에 맞춰 창 크기 조정
        self.resize(self.background_pixmap.size())  # 창 크기를 배경 이미지 크기로 설정

        # 버튼 및 콤보박스
        videoButton = QPushButton('비디오 시작', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['홀로그램', '글리치', '디지털 비트맵', '수채화', '3D 물결', '타이포그래피'])
        quitButton = QPushButton('나가기', self)

        # 버튼 위치 설정
        videoButton.setGeometry(20, 40, 220, 60)  # 크기 조정 (넓히기)
        self.pickCombo.setGeometry(250, 40, 140, 40)
        quitButton.setGeometry(400, 40, 120, 60)  # 크기 조정 (넓히기)

        # 스타일 시트 적용
        self.applyChristmasStyle(videoButton, quitButton)

        # 버튼 클릭 시 함수 연결
        videoButton.clicked.connect(self.videoSpecialEffectFunction)
        quitButton.clicked.connect(self.quitFunction)

        # 비디오 캡처 객체 초기화 (None으로 설정)
        self.cap = None

    def applyChristmasStyle(self, videoButton, quitButton):
        # 창 배경 스타일
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f1f8f0;  /* 연한 녹색 */
            }
        """)

        # 버튼 스타일 (크리스마스 테마)
        videoButton.setStyleSheet("""
            QPushButton {
                background-color: #ff0000;  /* 크리스마스 빨강 */
                color: white;  /* 글자 색 */
                font-size: 20px;  /* 글씨 크기 */
                font-weight: bold;  /* 글씨 두껍게 */
                border: 3px solid #ffffff;  /* 흰색 테두리 */
                border-radius: 20px;  /* 둥근 모서리 */
                padding: 20px;
                width: 220px;
                font-family: 'Arial', sans-serif;
            }
            QPushButton:hover {
                background-color: #d70000;  /* 호버 시 색상 변경 */
            }
            QPushButton:pressed {
                background-color: #b20000;  /* 클릭 시 색상 변경 */
            }
        """)

        quitButton.setStyleSheet("""
            QPushButton {
                background-color: #00a000;  /* 크리스마스 초록 */
                color: white;
                font-size: 20px;
                font-weight: bold;
                border: 3px solid #ffffff;
                border-radius: 20px;
                padding: 20px;
                width: 120px;
                font-family: 'Arial', sans-serif;
            }
            QPushButton:hover {
                background-color: #008800;
            }
            QPushButton:pressed {
                background-color: #006600;
            }
        """)

        # 콤보박스 스타일 (크리스마스 느낌을 위한 색상 및 테두리)
        self.pickCombo.setStyleSheet("""
            QComboBox {
                background-color: #f7f7f7;  /* 밝은 색 배경 */
                color: #333333;  /* 글자 색 */
                font-size: 16px;
                padding: 10px;
                border-radius: 12px;
                border: 3px solid #cc0000;  /* 빨간색 테두리 */
                width: 140px;
                font-family: 'Arial', sans-serif;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                border: 2px solid #cc0000;
                color: #333333;
            }
            QComboBox::item:selected {
                background-color: #f2f2f2;
                color: #ff0000;  /* 선택된 항목 글자 색 */
            }
        """)

    # 창에 배경 이미지를 그리기 위한 메서드
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background_pixmap)  # 배경 이미지 그리기
        super().paintEvent(event)  # 나머지 위젯들도 그리기

    # 비디오 특수 효과 함수들
    def hologramEffect(self, frame):
        frame_holo = cv.applyColorMap(frame, cv.COLORMAP_JET)  # 컬러맵 적용
        frame_holo = cv.addWeighted(frame, 0.5, frame_holo, 0.5, 0)

        # 눈 내리는 효과 추가
        self.addSnowEffect(frame_holo)

        return frame_holo

    def glitchEffect(self, frame):
        rows, cols, _ = frame.shape
        num_glitches = random.randint(3, 7)
        for _ in range(num_glitches):
            start_row = random.randint(0, rows - 50)
            end_row = random.randint(start_row + 20, rows)
            start_col = random.randint(0, cols - 50)
            end_col = random.randint(start_col + 20, cols)
            frame[start_row:end_row, start_col:end_col] = cv.bitwise_not(frame[start_row:end_row, start_col:end_col])

        # 눈 내리는 효과 추가
        self.addSnowEffect(frame)

        # 조명 효과 추가
        self.addLightEffect(frame)

        return frame

    def digitalBitmapEffect(self, frame):
        small = cv.resize(frame, (16, 16), interpolation=cv.INTER_LINEAR)
        big = cv.resize(small, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)

        # 눈 내리는 효과 추가
        self.addSnowEffect(big)

        return big

    def watercolorEffect(self, frame):
        frame = cv.GaussianBlur(frame, (21, 21), 0)
        frame = cv.edgePreservingFilter(frame, flags=2, sigma_s=60, sigma_r=0.4)

        # 눈 내리는 효과 추가
        self.addSnowEffect(frame)

        # 조명 효과 추가
        self.addLightEffect(frame)

        return frame

    def waveEffect(self, frame):
        rows, cols, _ = frame.shape
        for i in range(rows):
            for j in range(cols):
                wave = int(20 * math.sin(i / 10.0))
                frame[i, j] = frame[i, (j + wave) % cols]

        # 눈 내리는 효과 추가
        self.addSnowEffect(frame)

        return frame

    def christmasTreeEffect(self, frame):
        # 트리의 각 레벨을 표현할 텍스트 문자열
        tree_levels = [
            "    *    ",
            "   ***   ",
            "  *****  ",
            " ******* ",
            "*********",
            "   | |   "
        ]

        # 트리의 텍스트 색상과 폰트 설정
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2

        # 텍스트 색상을 번갈아 가며 설정 (빨강, 초록)
        colors = [(0, 255, 0), (0, 0, 255)]  # 초록, 빨강
        color_index = 0  # 첫 번째 색상부터 시작

        # 텍스트 위치 (y값을 점차 증가시키며 텍스트 출력)
        x = 50  # x좌표 (고정)
        y_start = 100  # 시작 y좌표
        y_offset = 40  # 각 레벨 간의 y 간격

        # 트리 텍스트 그리기
        for i, line in enumerate(tree_levels):
            frame = cv.putText(frame, line, (x, y_start + i * y_offset), font, font_scale, colors[color_index], thickness, cv.LINE_AA)
            color_index = 1 - color_index  # 색상을 번갈아 가며 변경

        # 내 글자 추가
        my_text = "I love computer vision!"
        x = 50  # x좌표
        y = y_start + len(tree_levels) * y_offset + 40  # 트리 아래에 글자 표시

        # 글자 색상도 번갈아 가면서 빨강, 초록 적용
        color_index = 0  # 색상 초기화
        for char in my_text:
            frame = cv.putText(frame, char, (x, y), font, font_scale, colors[color_index], thickness, cv.LINE_AA)
            x += 25  # 글자 간격을 두어 이동
            color_index = 1 - color_index  # 색상을 번갈아 가며 변경

        return frame

    # 눈 내리는 효과 함수
    def addSnowEffect(self, frame):
        snowflakes = 100  # 눈송이 개수
        height, width, _ = frame.shape
        for _ in range(snowflakes):
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(1, 4)
            color = (255, 255, 255)  # 흰색
            cv.circle(frame, (x, y), radius, color, -1)  # 눈송이 그리기

    # 조명 효과 함수 (빨강, 초록 작은 동그라미)
    def addLightEffect(self, frame):
        lights = 50  # 조명 개수
        height, width, _ = frame.shape
        for _ in range(lights):
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(5, 10)
            color = random.choice([(0, 255, 0), (0, 0, 255)])  # 빨강, 초록
            cv.circle(frame, (x, y), radius, color, -1)  # 조명 그리기

    # 비디오 스트리밍 시작 함수
    def videoSpecialEffectFunction(self):
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 웹캠 연결

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # 비디오 효과 선택
            selected_effect = self.pickCombo.currentText()

            if selected_effect == '홀로그램':
                frame = self.hologramEffect(frame)
            elif selected_effect == '글리치':
                frame = self.glitchEffect(frame)
            elif selected_effect == '디지털 비트맵':
                frame = self.digitalBitmapEffect(frame)
            elif selected_effect == '수채화':
                frame = self.watercolorEffect(frame)
            elif selected_effect == '3D 물결':
                frame = self.waveEffect(frame)
            elif selected_effect == '타이포그래피':
                frame = self.christmasTreeEffect(frame)

            cv.imshow('Video', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()

    # 종료 함수
    def quitFunction(self):
        self.close()

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoSpecialEffect()
    window.show()
    sys.exit(app.exec_()) 