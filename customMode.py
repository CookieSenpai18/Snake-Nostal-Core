"""This s where game configuration occur"""
# Import necessary libraries and modules
import sys
from components import *
from loadingPage import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QLineEdit, QGraphicsOpacityEffect)


class GameConfig(QMainWindow):
    """Game config window class"""
    def closeEvent(self, event):
        """Handle window close event"""
        event.accept()

    def __init__(self):
        super().__init__()
        # Window setup
        self.setWindowTitle("Snake Game")
        self.setWindowIcon(QIcon(config.title_icon))
        self.setStyleSheet(config.window_style)
        self.setFixedSize(760, 820)


        # Below are the page elements
        # Title config label
        self.title_label = QLabel(self)
        self.title_label.setStyleSheet(f"border-image: url('{config.custom_label}');")
        self.title_label.setGeometry(0, 25, self.width(), 170)


        # Configured info frame
        frame1_opacity = QGraphicsOpacityEffect(self)
        frame1_opacity.setOpacity(0.8)
        self.frame1 = QLabel(self)
        self.frame1.setStyleSheet("background-color: darkgray;"
                                  "border-radius: 10px;"
                                  "border: 3px solid black;")
        self.frame1.setGraphicsEffect(frame1_opacity)
        self.frame1.setGeometry(60, 200, 640, 100)

        # Background frame
        frame2_opacity = QGraphicsOpacityEffect(self)
        frame2_opacity.setOpacity(0.8)
        self.frame2 = QLabel(self)
        self.frame2.setStyleSheet("background-color: grey;"
                                  "border: 4px solid black;"
                                  "border-radius: 10px")
        self.frame2.setGraphicsEffect(frame2_opacity)
        self.frame2.setGeometry(60, 320, 640, 475)

        # Game sizes frame
        frame3_opacity = QGraphicsOpacityEffect(self)
        frame3_opacity.setOpacity(0.7)
        self.frame3 = QLabel(self)
        self.frame3.setStyleSheet("background-color: grey;"
                                  "border: 4px solid black;"
                                  "border-radius: 10px")
        self.frame3.setGraphicsEffect(frame3_opacity)
        self.frame3.setGeometry(80, 350, 600, 125)

        # Environment selection frame
        frame4_opacity = QGraphicsOpacityEffect(self)
        frame4_opacity.setOpacity(0.7)
        self.frame4 = QLabel(self)
        self.frame4.setStyleSheet("background-color: grey;"
                                  "border: 4px solid black;"
                                  "border-radius: 10px")
        self.frame4.setGraphicsEffect(frame4_opacity)
        self.frame4.setGeometry(80, 490, 600, 285)


        # Description of content
        self.size_label = QLabel("Select Ground Size",self)
        self.size_label.setGeometry(80, 335, 600, 80)
        self.size_label.setAlignment(Qt.AlignCenter)
        self.size_label.setStyleSheet("background: transparent;"
                                      "font: bold 35px Comic Sans MS;")

        # Description of content
        self.ground_label = QLabel("Select Environment",self)
        self.ground_label.setGeometry(80, 475, 600, 80)
        self.ground_label.setAlignment(Qt.AlignCenter)
        self.ground_label.setStyleSheet("background: transparent;"
                                      "font: bold 30px Comic Sans MS;")


        # Selection of ground sizes
        self.size_1 = QPushButton("14x14\n(Default)", self, clicked=self.size14)
        self.size_1.setGeometry(140, 410, 100, 45)
        self.size_1.setStyleSheet("""
                            QPushButton 
                                {
                                    background-color: rgb(154, 222, 82);
                                    border-radius: 10px;
                                    border: 2px solid black;
                                    font-family: Comic Sans MS, Arial;
                                    font-weight: bold;
                                    font-size: 16px;
                                    padding-bottom: 2px;
                                }
                            QPushButton::hover
                                {
                                    font-size: 19px;
                                    background-color: rgb(134, 202, 62);    
                                    border: 1px solid black;
                                }
                            QPushButton::pressed
                                {
                                    font-size: 13px;
                                    background-color: rgb(94, 162, 22);   
                                    border: 5px solid black;
                                }
                                    """)

        self.size_2 = QPushButton("20x20", self, clicked=self.size20)
        self.size_2.setGeometry(270, 410, 100, 45)
        self.size_2.setStyleSheet("""
                            QPushButton 
                                {
                                    background-color: rgb(154, 222, 82);
                                    border-radius: 10px;
                                    border: 2px solid black;
                                    font-family: Comic Sans MS, Arial;
                                    font-weight: bold;
                                    font-size: 20px;
                                }
                            QPushButton::hover
                                {
                                    font-size: 23px;
                                    background-color: rgb(134, 202, 62);    
                                    border: 1px solid black;
                                }
                            QPushButton::pressed
                                {
                                    font-size: 15px;
                                    background-color: rgb(94, 162, 22);   
                                    border: 5px solid black;
                                }
                                    """)

        self.size_3 = QPushButton("25x25", self, clicked=self.size25)
        self.size_3.setGeometry(395, 410, 100, 45)
        self.size_3.setStyleSheet("""
                            QPushButton 
                                {
                                    background-color: rgb(154, 222, 82);
                                    border-radius: 10px;
                                    border: 2px solid black;
                                    font-family: Comic Sans MS, Arial;
                                    font-weight: bold;
                                    font-size: 20px;
                                }
                            QPushButton::hover
                                {
                                    font-size: 23px;
                                    background-color: rgb(134, 202, 62);    
                                    border: 1px solid black;
                                }
                            QPushButton::pressed
                                {
                                    font-size: 15px;
                                    background-color: rgb(94, 162, 22);   
                                    border: 5px solid black;
                                }
                                    """)

        self.size_4 = QPushButton("35x35", self, clicked=self.size35)
        self.size_4.setGeometry(520, 410, 100, 45)
        self.size_4.setStyleSheet("""
                            QPushButton 
                                {
                                    background-color: rgb(154, 222, 82);
                                    border-radius: 10px;
                                    border: 2px solid black;
                                    font-family: Comic Sans MS, Arial;
                                    font-weight: bold;
                                    font-size: 20px;
                                }
                            QPushButton::hover
                                {
                                    font-size: 23px;
                                    background-color: rgb(134, 202, 62);    
                                    border: 1px solid black;
                                }
                            QPushButton::pressed
                                {
                                    font-size: 15px;
                                    background-color: rgb(94, 162, 22);   
                                    border: 5px solid black;
                                }
                                    """)


        # Selection of environments
        self.land1 = QPushButton(self, clicked=self.land1_click)                  # Default
        self.land1.setGeometry(180, 540, 100, 100)
        self.land1.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: black;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-image: url('{config.ground_image + '0.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: white;
                                        }}        
                                        """)

        self.land2 = QPushButton("🔒\nAchieve\n10 Score",self, clicked=self.land2_click)       # 10 Score
        self.land2.setGeometry(328, 540, 100, 100)
        self.land2.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: black;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-image: url('{config.ground_image + '1.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: white;
                                        }}        
                                        """)

        self.land3 = QPushButton("🔒\nAchieve\n20 Score",self, clicked=self.land3_click)       # 20 Score
        self.land3.setGeometry(475, 540, 100, 100)
        self.land3.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: black;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-image: url('{config.ground_image + '2.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: white;
                                        }}        
                                        """)

        self.land4 = QPushButton("🔒\nAchieve\n30 Score",self, clicked=self.land4_click)       # 30 Score
        self.land4.setGeometry(180, 660, 100, 100)
        self.land4.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: black;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-image: url('{config.ground_image + '3.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: white;
                                        }}        
                                        """)

        self.land5 = QPushButton("🔒\nAchieve\n40 Score",self, clicked=self.land5_click)       # 40 Score
        self.land5.setGeometry(328, 660, 100, 100)
        self.land5.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: yellow;
                                            font-weight: bold;
                                            border: 3px solid black;
                                            border-image: url('{config.ground_image + '4.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: black;
                                        }}        
                                        """)

        self.land6 = QPushButton("🔒\nAchieve\n50 Score",self, clicked=self.land6_click)       # 50 Score
        self.land6.setGeometry(475, 660, 100, 100)
        self.land6.setStyleSheet(f"""
                                    QPushButton
                                        {{
                                            font-size: 18px;
                                            color: yellow;
                                            font-weight: bold;
                                            border: 3px solid black;   
                                            border-image: url('{config.ground_image + '5.jpg'}') stretch stretch;
                                        }}
                                    QPushButton::hover
                                        {{
                                            border: 2px solid black;
                                        }}
                                    QPushButton::pressed
                                        {{
                                            border: 7px solid black;
                                        }}
                                    QPushButton::disabled
                                        {{
                                            color: white;
                                        }}        
                                        """)


        # Bellow are the game configuration info
        # Image of selected environment
        self.info_ground = QLabel(self)
        self.info_ground.setStyleSheet(f"border-image: url('{game_attr.ground}') stretch stretch;")
        self.info_ground.setGeometry(100, 207, 85, 85)

        # Details of configuration
        self.game_info = QLabel("Game Info\n"
                                "Environment: ####\n"
                                "Ground Size: ##x##",
                                self)
        self.game_info.setGeometry(225, 200, 350, 100)
        self.game_info.setStyleSheet("font-size: 20px;"
                                     "font-weight: bold;"
                                     "font-family: Comic Sans MS;"
                                     "background: transparent;")

        # Start button setup
        self.start = QPushButton("Start", self, clicked=self.start_click)
        self.start.setGeometry(580, 225, 100, 50)
        self.start.setStyleSheet(f"""
                                        QPushButton
                                            {{
                                                background-color: rgb(100, 255, 0);
                                                font-size: 30px;
                                                font-weight: bold;
                                                font-family: Comic Sans MS;
                                                border-radius: 10px;
                                                border: 3px solid black;
                                            }}
                                        QPushButton::hover
                                            {{
                                                background-color: rgb(80, 240, 0);
                                                font-size: 35px;
                                                padding-bottom: 5px;
                                                border: 2px solid black;
                                            }}
                                        QPushButton::pressed
                                            {{
                                                background-color: rgb(40, 200, 0);
                                                font-size: 25px;
                                                padding-top: 5px;
                                                border: 6px solid black;
                                            }}
                                            """)


        # Back button setup
        button_opacity = QGraphicsOpacityEffect(self)
        button_opacity.setOpacity(0.7)
        self.back_button = QPushButton("x", self, clicked=self.back_clicked)
        self.back_button.setGeometry(685, 10, 50, 50)
        self.back_button.setGraphicsEffect(button_opacity)
        self.back_button.setStyleSheet(f"""QPushButton
                                                    {{
                                                        background: white;
                                                        font-size: 45px;
                                                        font-weight: bold;
                                                        padding: 0px 0px 10px 0px;
                                                        border-radius: 25px
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


        self.check_score()      # Unlocks environments based on user high score
        self.update_info()      # Initialize the config info at startup
        self.loop_score()       # To prevent anomaly when saved data explicitly manipulated



    # Below are the config logics
    # Environment selections
    def land1_click(self):
        """Updates the selected environment to Default (Grass)"""
        game_attr.ground_index = 0
        self.update_info()
        sounds.click_sfx.play()

    def land2_click(self):
        """Updates the selected environment to Drought"""
        game_attr.ground_index = 1
        self.update_info()
        sounds.click_sfx.play()

    def land3_click(self):
        """Updates the selected environment to Molten"""
        game_attr.ground_index = 2
        self.update_info()
        sounds.click_sfx.play()

    def land4_click(self):
        """Updates the selected environment to Cursed Silhouette"""
        game_attr.ground_index = 3
        self.update_info()
        sounds.click_sfx.play()

    def land5_click(self):
        """Updates the selected environment to Crystic"""
        game_attr.ground_index = 4
        self.update_info()
        sounds.click_sfx.play()

    def land6_click(self):
        """Updates the selected environment to Alienized"""
        game_attr.ground_index = 5
        sounds.click_sfx.play()
        self.update_info()


    # Ground size selections
    def size14(self):
        """Updates the ground size to 14x14"""
        sounds.click_sfx.play()
        game_attr.ground_size = 50
        self.update_info()

    def size20(self):
        """Updates the ground size to 20x20"""
        sounds.click_sfx.play()
        game_attr.ground_size = 35
        self.update_info()

    def size25(self):
        """Updates the ground size to 25x25"""
        sounds.click_sfx.play()
        game_attr.ground_size = 28
        self.update_info()

    def size35(self):
        """Updates the ground size to 35x35"""
        sounds.click_sfx.play()
        game_attr.ground_size = 20
        self.update_info()


    def update_info(self):
        """Updates the config info based on user selections"""
        if game_attr.username == 'Autumn843y':
            self.game_info.setText(f"Game Info\nEnvironment: {game_attr.ground_name[6]}\n"
                                   f"Ground Size: {int(700 / game_attr.ground_size)}x{int(700 / game_attr.ground_size)}")

        else:
            self.game_info.setText(f"Game Info\nEnvironment: {game_attr.ground_name[game_attr.ground_index]}\n"
                                   f"Ground Size: {int(700 / game_attr.ground_size)}x{int(700 / game_attr.ground_size)}")

        game_attr.update_ground()
        self.info_ground.setStyleSheet(f"border-image: url('{game_attr.ground}') stretch stretch;")
        game_attr.save_game_config()


    def check_score(self):
        """Checker in-case the saved high score and selected environment don't match"""
        self.land2.setDisabled(True)
        self.land3.setDisabled(True)
        self.land4.setDisabled(True)
        self.land5.setDisabled(True)
        self.land6.setDisabled(True)

        if game_attr.high_score >= 10:
            self.land2.setDisabled(False)
            self.land2.setText("")

        elif game_attr.high_score <= 10 and game_attr.ground_index == 1:
            game_attr.ground_index = 0
            game_attr.update_ground()
            self.update_info()


        if game_attr.high_score >= 20:
            self.land3.setDisabled(False)
            self.land3.setText("")

        elif game_attr.high_score <= 20 and game_attr.ground_index == 2:
            game_attr.ground_index = 1
            game_attr.update_ground()
            self.update_info()


        if game_attr.high_score >= 30:
            self.land4.setDisabled(False)
            self.land4.setText("")

        elif game_attr.high_score <= 30 and game_attr.ground_index == 3:
            game_attr.ground_index = 2
            game_attr.update_ground()
            self.update_info()


        if game_attr.high_score >= 40:
            self.land5.setDisabled(False)
            self.land5.setText("")

        elif game_attr.high_score <= 40 and game_attr.ground_index == 4:
            game_attr.ground_index = 3
            game_attr.update_ground()
            self.update_info()


        if game_attr.high_score >= 50:
            self.land6.setDisabled(False)
            self.land6.setText("")

        elif game_attr.high_score <= 50 and game_attr.ground_index == 5:
            game_attr.ground_index = 4
            game_attr.update_ground()
            self.update_info()

    def loop_score(self):
        """Loops the checker_score to realign the selected environment with high score"""
        ct = 0
        while ct < 5:
            self.check_score()
            ct += 1


    def back_clicked(self):
        self.close()


    def start_click(self):
        """Opens the loading page leading to game page"""
        sounds.click_sfx.play()
        game_attr.destination = 0
        self.load_page = LoadingPage()
        self.load_page.setGeometry(self.geometry())
        self.load_page.show()
        self.close()