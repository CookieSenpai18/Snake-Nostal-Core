"""This is the Main Page that connects all modules and local library"""
# Import necessary libraries and modules
import sys
from customMode import *
from SettingsPage import *
from AboutPage import AboutPg
from components import sounds, config
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer, QPropertyAnimation,QSequentialAnimationGroup, QRect

class HomePage(QMainWindow):
    """Home page window class"""
    def __init__(self):
        super().__init__()
        # Window setup
        self.setFixedSize(760, 820)
        self.setWindowTitle("Snake Game")
        self.setStyleSheet(config.window_style)
        self.setWindowIcon(QIcon(config.title_icon))

        # Plays the BGM home music
        sounds.bgm_home.play(-1)

        # Timer to check if the window is ready to reopen
        self.delay = QTimer()
        self.delay.timeout.connect(self.detect_return)
        self.delay.start(5)

        # Below are the home page elements
        # Moving snake image setup
        self.snake_image = QLabel(self)
        self.snake_image.setGeometry(QRect(-35, -35,self.width()+50, self.height()+50))
        self.snake_image.setStyleSheet(f"""QLabel {{
                                                border-image: url('{config.snake_image}') stretch stretch 0 0 0 0;
                                            }}""")
        self.animate_snake()    # Animate the snake

        # Game title image
        self.title_label = QLabel(self)
        self.title_label.setGeometry(0, 50, 760, 300)
        self.title_label.setStyleSheet(f"""QLabel {{
                                                border-image: url('{config.home_title}') stretch stretch 0 0 0 0;
                                            }}""")

        # Start button setup
        self.start_button = QPushButton("PLAY", self, clicked=self.game_config)
        self.start_button.setGeometry(225, 375, 300, 75)
        self.start_button.setStyleSheet(f"""QPushButton 
                                        {{
                                            background-color: rgb(255, 46, 46);
                                            border-radius: 25px;
                                            font: bold 40px Comic Sans MS, Arial;
                                            border: 5px solid black;
                                        }}
                                            QPushButton:hover
                                        {{
                                            background-color: rgb(200, 46, 46);
                                            font-size: 17pt;
                                            border: 2px solid black;
                                        }}
                                            QPushButton:pressed
                                        {{
                                            background-color: rgb(100, 100, 100);
                                            font-size: 10pt;
                                            border: 8px solid black;
                                        }}
                                            QPushButton::disabled
                                        {{
                                            color: black;
                                        }}
                                            """)

        # Settings button setup
        self.settings_button = QPushButton("Settings", self, clicked=self.settings_clicked)
        self.settings_button.setGeometry(225, 500, 300, 75)
        self.settings_button.setStyleSheet(f"""QPushButton 
                                        {{
                                            background-color: rgb(232, 180, 53);
                                            border-radius: 25px;
                                            font: bold 40px Comic Sans MS, Arial;
                                            border: 5px solid black;
                                            padding-bottom: 5px;
                                        }}
                                            QPushButton:hover
                                        {{
                                            background-color: rgb(232, 140, 53);
                                            font-size: 17pt;
                                            border: 2px solid black;
                                        }}
                                            QPushButton:pressed
                                        {{
                                            background-color: rgb(100, 100, 100);
                                            font-size: 10pt;
                                            border: 8px solid black;
                                        }}
                                            QPushButton::disabled
                                        {{
                                            color: black;
                                        }}
                                            """)

        # About button setup
        self.about_button = QPushButton("About", self, clicked=self.about_clicked)
        self.about_button.setGeometry(225, 625, 300, 75)
        self.about_button.setStyleSheet(f"""QPushButton 
                                        {{
                                            background-color: rgb(232, 180, 53);
                                            border-radius: 25px;
                                            font: bold 40px Comic Sans MS, Arial;
                                            border: 5px solid black;
                                            padding-bottom: 5px;
                                        }}
                                            QPushButton:hover
                                        {{
                                            background-color: rgb(232, 140, 53);
                                            font-size: 17pt;
                                            border: 2px solid black;
                                        }}
                                            QPushButton:pressed
                                        {{
                                            background-color: rgb(125, 125, 125);
                                            font-size: 10pt;
                                            border: 8px solid black;
                                        }}
                                            QPushButton::disabled
                                        {{
                                            color: black;
                                        }}
                                            """)

        # Version code label
        self.show_version = QLabel(game_attr.version, self)
        self.show_version.setGeometry(555, 790, 200, 25)
        self.show_version.setAlignment(Qt.AlignCenter)
        self.show_version.setStyleSheet("font: bold 18px Comic Sans MS, Arial;")

        # Below are the profile editing elements
        # Profile toggle button in window
        self.profile = QPushButton(game_attr.username, self, clicked=self.show_profile)
        self.profile.setGeometry(10, 15, 175, 40)
        self.profile.setStyleSheet(f"""
                                            QPushButton 
                                                {{
                                                    background-color: rgb(166, 227, 113);
                                                    font: bold 20px Comic Sans MS, Arial;
                                                    text-align: left;
                                                    padding-left: 10px;
                                                    padding-bottom: 5px;
                                                    border: 2px solid black;
                                                    border-radius: 10px;
                                                }}
                                            QPushButton:hover
                                                {{
                                                    font-size: 23px;
                                                    border: 1px solid black;
                                                }}
                                            QPushButton:pressed
                                                {{
                                                    font-size: 18px;
                                                    border: 5px solid black;
                                                    padding-top: 3px;
                                                }}
                                            """)

        # Profile editing frame
        self.profile_panel = QLabel(self)
        self.profile_panel.setGeometry(153, 275, 450, 250)
        self.profile_panel.setStyleSheet("background-color: rgb(166, 227, 113);"
                                         "border-radius: 20px;"
                                         "border: 4px solid black;")

        # Profile title/label
        self.profile_title = QLabel("Enter user name", self)
        self.profile_title.setGeometry(251, 280, 250, 50)
        self.profile_title.setAlignment(Qt.AlignCenter)
        self.profile_title.setStyleSheet("font: bold 25px Comic Sans MS, Arial;")

        # User input field for username
        self.edit_name = QLineEdit(game_attr.username, self)
        self.edit_name.setGeometry(251, 352, 250, 50)
        self.edit_name.setPlaceholderText("Username")
        self.edit_name.setTextMargins(10, 0, 0, 0)
        self.edit_name.setStyleSheet(f"""
                                            QLineEdit 
                                                {{
                                                    background-color: lightgray;
                                                    border: 2px solid black;
                                                    font: bold 20px Comic Sans MS, Arial;
                                                }}
                                            """)

        # Save button setup
        self.save_button = QPushButton("Save", self, clicked=self.save_profile)
        self.save_button.setGeometry(303, 460, 150, 35)
        self.save_button.setStyleSheet(f"""
                                        QPushButton
                                            {{
                                                background-color: rgb(100, 255, 0);
                                                border-radius: 15px;
                                                font: bold 20px Comic Sans MS, Arial;
                                                border: 3px solid black;
                                                padding-bottom: 4px;
                                            }}
                                        QPushButton:hover
                                            {{
                                                background-color: rgb(80, 240, 0);
                                                border: 2px solid black;
                                                font: bold 23px Comic Sans MS, Arial;
                                                padding-bottom: 4px;
                                            }}
                                        QPushButton:pressed
                                            {{
                                                background-color: rgb(40, 200, 0);
                                                border: 6px solid black;
                                                font: bold 17px Comic Sans MS, Arial;
                                                padding-top: 4px;
                                            }}
                                        """)

        # Profile saving status label
        self.save_status = QLabel(self)
        self.save_status.setGeometry(251, 415, 250, 25)
        self.save_status.setAlignment(Qt.AlignCenter)
        self.save_status.setStyleSheet("font: bold 20px Comic Sans MS, Arial;")

        # Profile close button
        self.close_profile = QPushButton("x", self, clicked=self.hide_profile)
        self.close_profile.setGeometry(535, 290, 50, 50)
        self.close_profile.setStyleSheet(f"""
                                        QPushButton 
                                            {{
                                                background: transparent;
                                                font: bold 40px Comic Sans MS, Arial;
                                            }}
                                        QPushButton:hover
                                            {{
                                                font-size: 47px;
                                            }}
                                        QPushButton:pressed
                                            {{
                                                font-size: 35px;
                                            }}
                                        """)

        self.hide_profile()



    # Below are the home page logics
    def animate_snake(self):
        """Animate the snake image"""
        # 1st animation
        animation1 = QPropertyAnimation(self.snake_image, b'geometry', self)
        animation1.setDuration(7000)
        animation1.setStartValue(QRect(-35, -35, self.width() + 50, self.height() + 50))
        animation1.setEndValue(QRect(20, 20, self.width() + 50, self.height() + 50))

        # 2nd animation
        animation2 = QPropertyAnimation(self.snake_image, b'geometry', self)
        animation2.setDuration(7000)
        animation2.setStartValue(QRect(20, 20, self.width() + 50, self.height() + 50))
        animation2.setEndValue(QRect(-35, 20, self.width() + 50, self.height() + 50))

        # 3rd animation
        animation3 = QPropertyAnimation(self.snake_image, b'geometry', self)
        animation3.setDuration(7000)
        animation3.setStartValue(QRect(-35, 20, self.width() + 50, self.height() + 50))
        animation3.setEndValue(QRect(20, -35, self.width() + 50, self.height() + 50))

        # 4th animation
        animation4 = QPropertyAnimation(self.snake_image, b'geometry', self)
        animation4.setDuration(7000)
        animation4.setStartValue(QRect(20, -35, self.width() + 50, self.height() + 50))
        animation4.setEndValue(QRect(-35, -35, self.width() + 50, self.height() + 50))

        # Convert all 4 different anims into a single sequential anim
        anim_group = QSequentialAnimationGroup(self)
        anim_group.addAnimation(animation1)
        anim_group.addAnimation(animation2)
        anim_group.addAnimation(animation3)
        anim_group.addAnimation(animation4)
        anim_group.setLoopCount(-1)
        anim_group.start()


    def save_profile(self):
        """Save user name if field not empty"""
        sounds.click_sfx.play()
        if self.edit_name.text() == "":
            self.save_status.setText("Name cannot be empty")

        else:
            game_attr.username = self.edit_name.text()
            self.save_status.setText("Saved profile")
            self.profile.setText(game_attr.username)
            game_attr.update_username()


    def show_profile(self):
        """Show profile editing panel/elements"""
        sounds.click_sfx.play()
        self.profile_panel.show()
        self.save_button.show()
        self.close_profile.show()
        self.edit_name.show()
        self.save_status.show()
        self.profile_title.show()

        # Disable main buttons
        self.start_button.setEnabled(False)
        self.settings_button.setEnabled(False)
        self.about_button.setEnabled(False)
        self.profile.setEnabled(False)

        # Clean label and inputs in-case the panel reopened
        self.edit_name.setText(game_attr.username)
        self.save_status.setText("")

    def hide_profile(self):
        """Hide profile editing panel/elements"""
        if not self.profile.isEnabled():
            sounds.click_sfx.play()
        self.profile_panel.hide()
        self.save_button.hide()
        self.close_profile.hide()
        self.edit_name.hide()
        self.save_status.hide()
        self.profile_title.hide()

        # Enable main buttons
        self.start_button.setEnabled(True)
        self.settings_button.setEnabled(True)
        self.about_button.setEnabled(True)
        self.profile.setEnabled(True)


    def game_config(self):
        """Opens game config page"""
        sounds.click_sfx.play()
        self.hide()
        self.cust = GameConfig()
        self.cust.setGeometry(self.geometry())
        self.cust.show()

        def reopen_main(event):
            """Reopen home page if destination value is 1 else it's heading to Game page"""
            if game_attr.destination == 1:
                self.show()
                self.setGeometry(self.cust.geometry())
                sounds.click_sfx.play()
                event.accept()

        self.cust.closeEvent = reopen_main    # Close event listener on config page


    def detect_return(self):
        """Destination listener from Game Page > Loading > Home"""
        if game_attr.load_complete:
            self.setGeometry(game_attr.previous_geometry)
            self.show()
            game_attr.load_complete = False


    def settings_clicked(self):
        """Opens settings page"""
        sounds.click_sfx.play()
        self.hide()
        self.settings = SettingsPg()
        self.settings.setGeometry(self.geometry())
        self.settings.show()

        def reopen_main(event):
            """Reopen home page"""
            self.setGeometry(self.settings.geometry())
            sounds.click_sfx.play()
            self.show()
            event.accept()

        self.settings.closeEvent = reopen_main      # Close event listener from settings page


    def about_clicked(self):
        """Opens About page"""
        sounds.click_sfx.play()
        self.hide()
        self.about = AboutPg()
        self.about.setGeometry(self.geometry())
        self.about.show()

        def reopen_main(event):
            """Reopen home page"""
            self.show()
            self.setGeometry(self.about.geometry())
            sounds.click_sfx.play()
            event.accept()

        self.about.closeEvent = reopen_main     # Close event listener from about page



# Launch the home page
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())