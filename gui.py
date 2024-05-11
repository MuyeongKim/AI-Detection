import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ex_gui import Ui_MainWindow
from tkinter import messagebox  # 파일 다이얼로그를 사용하기 위한 임포트, 메세지박스
from ultralytics import YOLO
import time





class gui_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(gui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_close.clicked.connect(self.exit_application) # 종료 버튼 메소드 연결
        self.pushButton_search.clicked.connect(self.browse_files)  # 검색 버튼에 메소드 연결
        self.comboBox_data.currentIndexChanged.connect(self.update_datasize) # 데이터사이즈 선택
        self.comboBox_source.currentIndexChanged.connect(self.update_source) #영t상소스 선택
        self.pushButton_enter.clicked.connect(self.submit)  # 검색 버튼에 메소드 연결
        self.lineEdit_juso.textChanged.connect(self.update_juso)  # lineEdit_juso의 textChanged 신호에 함수를 연결
        self.comboBox_percentage.currentIndexChanged.connect(self.option_percentage) # 옵션 임계값 선택
        self.comboBox_device.currentIndexChanged.connect(self.option_device) # 옵션 장치 선택
        self.comboBox_buffer.currentIndexChanged.connect(self.option_buffer) # 옵션 장치 선택
        self.comboBox_imgsz.currentIndexChanged.connect(self.option_imgsz) # 옵션 장치 선택
        # 초기화
        # 사용자 입력 주소를 저장할 변수
        self.juso = None
        self.percentage = None
        self.device = None
        self.imgsz = None
        self.buffer = None
    
    def exit_application(self, *args):
        # 프로그램 종료 확인 및 종료 처리
        if messagebox.askyesno("종료 확인", "정말로 종료하시겠습니까?"):
            self.close()
            
    def update_source(self, index):
        selection = self.comboBox_source.itemText(index)
        if selection == "선택하세요":
            return ""
        else:
            self.source = selection
        print(self.source)
        
    def update_datasize(self, index):
        selection = self.comboBox_data.itemText(index)
        if selection == "선택하세요":
            return ""
        else:
            size_dict = {'최대' : 'yolov8x.pt', '대': 'yolov8l.pt', '중': 'yolov8m.pt', '소': 'yolov8s.pt', '최소': 'yolov8n.pt'}
            self.datasize = size_dict[selection]   
        print(self.datasize)            

    def option_imgsz(self, index):
        selection = self.comboBox_imgsz.itemText(index)
        if selection == "해상도":
            self.imgsz = 640
        else:
            size_dict = {'640': 640, '1080': 1080, '1280': 1280, '1680': 1680, '1920(기본값)' : 1920, '3000' : 3000, '5000': 5000}
            self.imgsz = size_dict[selection]  
        print(self.imgsz)          
    
    def option_percentage(self, index):
        selection = self.comboBox_percentage.itemText(index)
        if selection == "임계값":
            self.percentage = 0.3
        else:
            size_dict = {'15%': 0.15, '30%(기본값)': 0.3, '50%': 0.5, '80%': 0.8}
            self.percentage = size_dict[selection]  
        print(self.percentage)                 
            
    def option_device(self, index):
        selection = self.comboBox_device.itemText(index)
        if selection == "사용장치":
            self.device = 'cpu'
        else:
            size_dict = {'CPU(기본값)': 'cpu', 'CUDA(GPU)': 0}
            self.device = size_dict[selection]   
        print(self.device)           

    def option_buffer(self, index):
        selection = self.comboBox_buffer.itemText(index)
        if selection == "버퍼":
            self.buffer = True
        else:
            size_dict = {'ON(기본값)': True, 'OFF': False}
            self.buffer = size_dict[selection]   
        print(self.buffer)    
                         
            
    def browse_files(self):
        # 파일 선택 다이얼로그 열기
        file_paths, _ = QFileDialog.getOpenFileNames(self, "파일 선택")
        if file_paths:  # 사용자가 파일을 선택하면 그 경로들을 lineEdit_juso에 설정
            self.lineEdit_juso.setText(", ".join(file_paths))
            self.juso = file_paths
            if len(self.juso) == 1:
                print(self.juso)
            else:
                print(len(self.juso),"개 선택")



            
    def update_juso(self, text):
        """사용자가 lineEdit_juso에 입력한 텍스트를 저장하는 함수"""
        self.juso = text
        
    def submit(self):       
        start_time = time.time()  # 시작 시간 기록
        percentage = self.percentage
        device = self.device
        stream_buffer = self.buffer
        imgsz = self.imgsz   
        
        if self.source == '유튜브(URL)':
            model = YOLO(self.datasize)
            source = self.juso
            # model.predict(source, stream_buffer=stream_buffer, save=False, show=True, conf=percentage, device=device) #유튜브
            results = model(source, stream=stream_buffer, imgsz=imgsz, save=False, show=True, conf=percentage, device=device)  # return a generator of Results objects

            # Process results generator
            for result in results:
                boxes = result.boxes  # Boxes object for bounding box outputs
                masks = result.masks  # Masks object for segmentation masks outputs
                keypoints = result.keypoints  # Keypoints object for pose outputs
                probs = result.probs  # Probs object for classification outputs
            #     # result.show()  # display to screen
            #     # result.save()  # save to disk

        elif self.source == '사진':
            model = YOLO(self.datasize)
            # source = self.juso
            for source in self.juso:         
                if len(self.juso) == 1:
                    model.predict(source, stream_buffer=stream_buffer, imgsz=imgsz, save=True, show=True, conf=percentage, device=device) #사진
                elif len(self.juso) != 1:
                    # model.predict(source, stream_buffer=stream_buffer, imgsz=imgsz, save=True, show=False, conf=percentage, device=device) #사진들
                    results = model(source, stream=stream_buffer, imgsz=imgsz, save=True, show=False, conf=percentage, device=device)  # return a generator of Results objects

                    # Process results generator
                    for result in results:
                        boxes = result.boxes  # Boxes object for bounding box outputs
                        masks = result.masks  # Masks object for segmentation masks outputs
                        keypoints = result.keypoints  # Keypoints object for pose outputs
                        probs = result.probs  # Probs object for classification outputs
                    #     # result.show()  # display to screen
                    #     # result.save()  # save to disk
                
        elif self.source == '영상':
            model = YOLO(self.datasize)
            source = self.juso[0]
            # model.predict(source, save=True, show=False, conf=0.3, device='cpu') #영상
            results = model(source, imgsz=imgsz, stream=True, save=True, show=True, conf=percentage, device=device)  # generator of Results objects
            for r in results:
                boxes = r.boxes  # Boxes object for bbox outputs
                masks = r.masks  # Masks object for segment masks outputs
                probs = r.probs  # Class probabilities for classification outputs
    
        elif self.source == '외부영상(캡쳐보드)':
            model = YOLO(self.datasize)
            source = self.juso            
            model.predict(source, stream_buffer=True, show=True, conf=percentage, device=device) #캡쳐보드
            
        end_time = time.time()  # 종료 시간 기록
        execution_time = end_time - start_time  # 실행 시간 계산
        print(f"실행 시간: {execution_time} 초")
        self.juso = None
        
        
    
if __name__ == "__main__":        
    app = QApplication(sys.argv)        
    window = gui_MainWindow()
    window.show()
    sys.exit(app.exec())            