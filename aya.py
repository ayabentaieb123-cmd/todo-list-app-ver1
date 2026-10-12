# the to do list i wish i had:
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QHBoxLayout,QVBoxLayout,QPushButton,QCheckBox,QLabel,QWidget,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QFontDatabase
from PyQt5.QtCore import Qt,QTime,QTimer

class Mainwindow(QMainWindow):#the actual to do list
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("pink.jpg"))
        self.setWindowTitle("the to do list i wish i had")
        self.setGeometry(500 , 300 , 1000 , 600)
        #labels:
        self.label1 = QLabel("to do list:",self)
        self.label2 = QLabel("my notes:",self)
        self.label3 = QLabel("PRIORETIES:",self)
        self.label4 = QLabel("rendez_vous:",self)
        self.label5 = QLabel("00:00:00", self)
        self.label6 = QLabel("THE CLOCK:",self)

        #labels geometry:
        self.label1.setGeometry(110,40,200,50)
        self.label4.setGeometry(750,50,400,50)
        self.label3.setGeometry(440,50,400,50)
        self.label2.setGeometry(465,320,400,50)
        self.label5.setGeometry(720,395,254,100)
        self.label6.setGeometry(740,330,400,50)

        #calling the checkboxes:
        self.make_checklist(13,30,75,330,480)
        self.make_checklist(5,410,90,265,180)
        self.make_checklist(5,410,360,265,180)
        self.make_checklist(5,715,90,265,180)
        #your clock:
        self.clock()
        self.timer = QTimer()
        self.timer.timeout.connect(self.clock)
        self.timer.start(1000)

        self.initUI()

    def initUI(self):
        self.label1.setObjectName("label1")
        self.label2.setObjectName("label2")
        self.label3.setObjectName("label3")
        self.label4.setObjectName("label4")
        self.label5.setObjectName("label5")
        self.label6.setObjectName("label6")

        #tried to import a TTF file for my clock font but was too hard for me next time maybe
        font_id = QFontDatabase.addApplicationFont("ds_digital.TTF")
        #font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(font_id )
        #my_font = QFont(font_family,40)
        #self.label5.setFont(my_font)

        self.setStyleSheet("""
                            Mainwindow{
                                border-image: url("slid2.jpg");
                        
                            }
                            #label1,#label2,#label4{
                                font-family:Segoe Script;
                                font-size: 30px;
                                font-style: italic;
                                color: #c73487;
                                font-weight: bold;
                            }
                            #label3,#label6{

                                font-size: 30px;
                                font-style: italic;
                                font-family:Segoe Script;
                                color: #c73487;
                                font-weight: bold;
                                text-decoration: underline;
                            }
                            #label5{
                                font-size : 35px;
                                background-color: pink;
                                border-radius: 15px;
                                color: #e643b7;
                                font-weight: bold;
                                border-color: #e643b7;
                                border-style: solid;
                                border-width: 4px;

                            }
                            """)

    
    def make_checklist(self,count,x,y,w,h):
        container = QWidget(self)
        container.setGeometry(x,y,w,h)

        layout = QVBoxLayout()
        boxes = [] 
        for _ in range (count):
            row = QHBoxLayout()
            checkbox = QCheckBox()
            lineedit = QLineEdit()
            row.addWidget(checkbox)
            row.addWidget(lineedit)
            layout.addLayout(row)
            boxes.append(checkbox)
        container.setLayout(layout)
        return boxes

    def clock(self):
        current_time = QTime.currentTime()
        time = current_time.toString("hh:mm:ss AP")
        self.label5.setText(time)

class Firstwindow(QMainWindow):#the image that shows before
    def __init__(self):
        super().__init__()
        self.setWindowTitle("the to do list i wish i had")
        self.setWindowIcon(QIcon("pink.jpg"))
        self.setGeometry(500 , 300 , 1000 , 600)
        self.label1 = QLabel("Hello Beautiful angels",self)
        self.label2 = QLabel("WELCOME to the one and only",self)
        self.label3 = QLabel(" to do app",self)
        self.label4 = QLabel("you'll ever gonna need in your life: ",self)
        self.label5 = QLabel("whenever you feel ready to start: ",self)        

        self.start_button = QPushButton("start",self)

        self.start_button.clicked.connect(self.open_mainwindow)
        self.initUI()

    def initUI(self):
        self.label1.setObjectName("label1")
        self.label2.setObjectName("label2")
        self.label3.setObjectName("label3")
        self.label4.setObjectName("label4")
        self.label5.setObjectName("label5")
        self.start_button.setObjectName("start_button")


        self.label1.setGeometry(80,90,900,75)
        self.label2.setGeometry(150,-40,900,500)
        self.label3.setGeometry(360,30,900,500)
        self.label4.setGeometry(110,100,900,500)
        self.label5.setGeometry(150,250,900,500)
        self.start_button.setGeometry(700,475,125,50)
        self.setStyleSheet("""
                            Firstwindow{
                                border-image: url("slid1.jpg");
                            }
                            #label1{
                                font-size: 70px;
                                font-style: italic;
                                font-family:Segoe Script;
                                color:#de478d;
                            }  
                            #label3{
                                font-size: 40px;
                                font-style: italic;
                                font-family:Segoe Script;  
                                font-weight: bold; 
                                color:#de478d;  
                                text-decoration: underline                       
                            }
                            #label2,#label4{
                                font-size: 40px;
                                font-weight: bold; 
                                font-family:Segoe Script;
                            }
                            #label5{
                                font-size: 30px; 
                                font-family:Segoe Script;
                                text-decoration: underline    
                            } 
                            #start_button{
                                font-size : 35px;
                                background-color: pink;
                                border-radius: 15px;
                                color: #de478d; 
                                font-weight:bold;
                                font-style: italic;
                                
                            }                    
                            """)

    def open_mainwindow(self):
        self.main = Mainwindow()
        self.main.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Firstwindow()
    window.show()
    sys.exit(app.exec_())
























