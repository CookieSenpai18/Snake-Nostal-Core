# Import necessary libaries and modules
import sys
from components import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QLabel, QSlider, QGraphicsOpacityEffect)


class SettingsPg(QMainWindow):
    """BGM and SFX volume intensity configuration page"""
    def closeEvent(self, event):
        """Handle window close event"""
        event.accept()

    def __init__(self):
        super().__init__()
        # Window setup
        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon(config.title_icon))
        self.setStyleSheet(config.window_style)
        self.setFixedSize(760, 820)


        # Local variable for future reference
        self.bgm_vol = int(sounds.bgm_vol * 100)
        self.sfx_vol = int(sounds.sfx_vol * 100)


        # Delay before updating save data
        self.update_schedule = QTimer()
        self.update_schedule.timeout.connect(self.update_data)
        self.update_schedule.start(1500)    # 1.5 sec delay

        # Below are the windows elements
        # Page title image
        self.title = QLabel(self)
        self.title.setGeometry(0, 50, self.width(), 200)
        self.title.setStyleSheet("background: transparent;"
                                 f"border-image: url('{config.settings_label}') stretch stretch 0 0 0 0;"
                                 "color: black;"
                                 "font: bold 35px;")


        # Frame panel for elements visibility
        frame_opacity = QGraphicsOpacityEffect(self)
        frame_opacity.setOpacity(0.6)
        self.frame = QLabel(self)
        self.frame.setGeometry(60, 300, 640, 400)
        self.frame.setGraphicsEffect(frame_opacity)
        self.frame.setStyleSheet("background-color: grey;"
                                 "border-radius: 15px;"
                                 "border: 3px solid black;")


        # BGM label setup
        self.bgm_label = QLabel("BGM Volume",self)
        self.bgm_label.setGeometry(100, 335, 200, 50)
        self.bgm_label.setStyleSheet("background: transparent;"
                                     "color: yellow;"
                                     "font: bold 30px Comic Sans MS;")
        # BGM slider setup
        self.bgm_slider = QSlider(Qt.Horizontal, self)
        self.bgm_slider.setRange(0, 100)
        self.bgm_slider.setValue(self.bgm_vol)      # Set initial value based on save data if exist
        self.bgm_slider.setGeometry(80, 400, 600, 50)
        self.bgm_slider.setStyleSheet("""QSlider::groove:horizontal
                                                    {   
                                                        background: black;
                                                        border-radius: 5px;
                                                        height: 10px;
                                                        margin: 10px;
                                                    }
                                                QSlider::handle:horizontal
                                                    {
                                                        background: white;
                                                        border-radius: 15px;
                                                        height: 30px;
                                                        width: 30px;
                                                        margin: -10px;
                                                    }
                                                     """)
        self.bgm_slider.valueChanged.connect(self.bgm_adjust)


        # SFX label setup
        self.sfx_label = QLabel("SFX Volume",self)
        self.sfx_label.setGeometry(100, 515, 200, 50)
        self.sfx_label.setStyleSheet("background: transparent;"
                                     "color: yellow;"
                                     "font: bold 30px Comic Sans MS;")

        # SFX slider setup
        self.sfx_slider = QSlider(Qt.Horizontal, self)
        self.sfx_slider.setRange(0, 100)
        self.sfx_slider.setValue(self.sfx_vol)      # Set initial value based on save data if exist
        self.sfx_slider.setGeometry(80, 580, 600, 50)
        self.sfx_slider.setStyleSheet("""QSlider::groove:horizontal
                                            {   
                                                background: black;
                                                border-radius: 5px;
                                                height: 10px;
                                                margin: 10px;
                                            }
                                        QSlider::handle:horizontal
                                            {
                                                background: white;
                                                border-radius: 15px;
                                                height: 30px;
                                                width: 30px;
                                                margin: -10px;
                                            }
                                             """)
        self.sfx_slider.valueChanged.connect(self.sfx_adjust)
        self.sfx_slider.sliderReleased.connect(self.test_sfx)   # Plays a sound as sample


        # Back button setup
        button_opacity = QGraphicsOpacityEffect(self)
        button_opacity.setOpacity(0.7)
        self.back_button = QPushButton("x", self, clicked=self.back_clicked)
        self.back_button.setGeometry(675, 25, 65, 65)
        self.back_button.setGraphicsEffect(button_opacity)
        self.back_button.setStyleSheet(f"""QPushButton
                                                {{
                                                    background: white;
                                                    font-size: 45px;
                                                    font-weight: bold;
                                                    padding: 0px 0px 10px 0px;
                                                    border-radius: 30px
                                                }}
                                            QPushButton::hover
                                                {{
                                                    font-size: 49px;
                                                    border: 3px solid black;
                                                }}
                                            QPushButton::pressed
                                                {{
                                                    font-size: 40px;
                                                    border: 7px solid black;
                                                }}
                                                """)



    # Below are the settings logic
    def bgm_adjust(self):
        """Adjust the volume intensity og BGM"""
        sounds.update_bgm(intensity=self.bgm_slider.value())


    def sfx_adjust(self):
        """Adjust the volume intensity og SFX"""
        sounds.update_sfx(intensity=self.sfx_slider.value())

    def test_sfx(self):
        """Test the SFX volume"""
        sounds.bite_sfx.play()


    def update_data(self):
        """Update save data with new settings"""
        sounds.update_data()


    def back_clicked(self):
        self.close()