# Import libraries as well as the other necessary modules
import sys
from PyQt5.QtCore import Qt
from components import config
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGraphicsOpacityEffect


class AboutPg(QMainWindow):
    """About page window class"""
    def closeEvent(self, event):
        """Handle window close event"""
        event.accept()

    def __init__(self):
        super().__init__()
        # Initialize window
        self.setWindowTitle("About")
        self.setWindowIcon(QIcon(config.title_icon))
        self.setStyleSheet(config.window_style)
        self.setFixedSize(760, 820)


        # Below are the page elements
        # About title label
        self.title = QLabel(self)
        self.title.setGeometry(30, 0, 700, 250)
        self.title.setStyleSheet(f"""QLabel 
                                    {{
                                        border-image: url('{config.about_title}') stretch stretch 0 0 0 0;
                                    }}
                                    """)
        # Background frame for text contents
        frame_opacity = QGraphicsOpacityEffect(self)
        frame_opacity.setOpacity(0.7)
        self.frame = QLabel(self)
        self.frame.setGeometry(60, 250, 640, 480)
        self.frame.setGraphicsEffect(frame_opacity)
        self.frame.setStyleSheet(f"""QLabel 
                                    {{
                                        background-color: grey;
                                        border-radius: 15px;
                                        border: 5px solid black;
                                    }}
                                    """)
        # Content title
        self.game_title = QLabel("Snake Nostal-Core",self)
        self.game_title.setAlignment(Qt.AlignCenter)
        self.game_title.setGeometry(200, 240, 350, 100)
        self.game_title.setStyleSheet(f"""QLabel
                                        {{
                                            color: yellow;
                                            font-size: 35px;
                                            font-weight: bold;
                                            font-family: Comic Sans MS, Georgia;
                                        }}
                                        """)
        # Content message setup
        self.content = QLabel(self)
        self.content.setGeometry(90, 300, 580, 400)
        self.content.setAlignment(Qt.AlignCenter)
        self.content.setStyleSheet(f"""QLabel
                                        {{
                                            background: transparent;
                                            font: bold 23px Comic Sans MS;
                                        }}
                                        """)
        # Content message
        self.content.setText(
                            "App Developed by Team Nostalics\n\n"
                            "This Snake Nostal-Core was built to bring back the\n"
                            "true retro experience with slightly modern touch.\n"
                            "Straightforward controls, old-school mechanics,\n"
                            "and that familiar nostalgic charm from the early\n"
                            "mobile and arcade days.\n\n"
                            "Enjoy the throwback!"
                            )

        # Back Button
        button_opacity = QGraphicsOpacityEffect(self)
        button_opacity.setOpacity(0.7)
        self.back_button = QPushButton("x",self, clicked=self.back_clicked)
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

        # Copyright Label
        self.copyright = QLabel(self)
        self.copyright.setGeometry(80, 650, 600, 100)
        self.copyright.setAlignment(Qt.AlignCenter)
        self.copyright.setText("© 2025-2026 BSIT 3J. All rights reserved.")
        self.copyright.setStyleSheet("font: bold 15px Comic Sans MS, Arial;")



    def back_clicked(self):
        """Handle back button when clicked."""
        self.close()