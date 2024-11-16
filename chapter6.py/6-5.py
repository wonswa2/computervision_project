from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파노라마 영상 및 얼굴 인식')
        self.setGeometry(200, 200, 800, 300)

        # Haar Cascades 초기화
        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.overlay_img = cv.imread('C:/Users/82105/cv/chapter6.py/nose.png', cv.IMREAD_UNCHANGED)

        # 버튼 및 레이블 생성
        collectButton = QPushButton('영상 수집', self)
        self.showButton = QPushButton('영상 보기', self)
        self.stitchButton = QPushButton('봉합', self)
        self.saveButton = QPushButton('저장', self)
        self.saveVideoButton = QPushButton('동영상 저장', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)

        # 버튼 위치 설정
        collectButton.setGeometry(10, 25, 120, 30)
        self.showButton.setGeometry(140, 25, 120, 30)
        self.stitchButton.setGeometry(270, 25, 120, 30)
        self.saveButton.setGeometry(400, 25, 120, 30)
        self.saveVideoButton.setGeometry(530, 25, 120, 30)
        quitButton.setGeometry(660, 25, 100, 30)
        self.label.setGeometry(10, 70, 700, 170)

        # 버튼 상태 초기화
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.saveVideoButton.setEnabled(False)

        # 버튼 클릭 시 연결할 함수 설정
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        self.saveVideoButton.clicked.connect(self.saveVideoFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.imgs = []  # 수집된 영상 리스트 초기화

    def overlay_image(self, background, overlay, pos, overlay_size):
        overlay = cv.resize(overlay, overlay_size)
        h, w, _ = overlay.shape
        x, y = pos[0] - w // 2, pos[1] - h // 2

        for i in range(h):
            for j in range(w):
                if x + j >= background.shape[1] or y + i >= background.shape[0]:
                    continue
                alpha = float(overlay[i][j][3] / 255.0)
                if alpha > 0:
                    background[y + i, x + j] = alpha * overlay[i, j][:3] + (1 - alpha) * background[y + i, x + j]
        return background

    def collectFunction(self):
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.saveVideoButton.setEnabled(False)

        self.cap = cv.VideoCapture(0)
        if not self.cap.isOpened():
            sys.exit('카메라 연결 실패')

        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

            for (x, y, w, h) in faces:
                nose_x = x + w // 2
                nose_y = y + h // 2
                frame = self.overlay_image(frame, self.overlay_img, (nose_x, nose_y), (50, 50))

            cv.imshow('Video Display', frame)

            key = cv.waitKey(1)
            if key == ord('c'):
                self.imgs.append(frame)
            elif key == ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()

        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButton.setEnabled(True)
            self.saveVideoButton.setEnabled(True)

    def showFunction(self):
        self.label.setText(f'수집된 영상은 {len(self.imgs)}장 입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            resized = cv.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)
            stack = np.hstack((stack, resized))
        cv.imshow('Image Collection', stack)

    def stitchFunction(self):
        try:
            stitcher = cv.Stitcher_create()
            status, self.img_stitched = stitcher.stitch(self.imgs)
            if status == cv.Stitcher_OK:
                cv.imshow('Stitched Panorama', self.img_stitched)
                self.label.setText('파노라마 제작 성공!')
            else:
                raise ValueError('Stitching 실패')
        except Exception as e:
            winsound.Beep(3000, 500)
            self.label.setText(f'파노라마 제작 실패: {e}')

    def saveFunction(self):
        if hasattr(self, 'img_stitched'):
            fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './', '이미지 파일 (*.jpg *.png)')
            if fname:
                cv.imwrite(fname, self.img_stitched)
                self.label.setText('이미지가 성공적으로 저장되었습니다.')

    def saveVideoFunction(self):
        if hasattr(self, 'img_stitched'):
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            out = cv.VideoWriter('output.avi', fourcc, 20.0, (self.img_stitched.shape[1], self.img_stitched.shape[0]))
            for _ in range(100):
                out.write(self.img_stitched)
            out.release()
            self.label.setText('동영상이 성공적으로 저장되었습니다.')

    def quitFunction(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Panorama()
    win.show()
    sys.exit(app.exec_())
