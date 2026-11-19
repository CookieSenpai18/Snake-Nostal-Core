# Import necessary libraries and modules
import sys
from SnakeGame import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt
from components import config, game_attr, sounds
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar


class LoadingPage(QMainWindow):
    """Loading window class"""
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


        # Timer for Loading text delay
        self.timer_label = QTimer(self)
        self.timer_label.timeout.connect(self.update_loading_label)
        self.timer_label.start(1000)
        self.count = 0

        # Delay/Speed of filling Loading bar
        self.tick = QTimer(self)
        self.tick.timeout.connect(self.update_bar)
        self.tick.start(50)


        # Below are the loading page elements
        # Game title image
        self.title_label = QLabel(self)
        self.title_label.setGeometry(0, 100, 760, 300)
        self.title_label.setStyleSheet(f"""
                                        QLabel 
                                            {{
                                                border-image: url('{config.home_title}');
                                            }}
                                            """)
        # Loading text
        self.loading_label = QLabel("Loading...",self)
        self.loading_label.setGeometry(250, 590, 250, 75)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setStyleSheet("background: transparent;"
                                         "font: bold 45px Comic Sans MS;"
                                         "color: yellow;")

        # Loading Bar setup
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setRange(0, 100)
        self.loading_bar.setValue(0)
        self.loading_bar.setGeometry(30, 550, 700, 30)
        self.loading_bar.setStyleSheet(f"""QProgressBar
                                                {{
                                                    background-color: rgb(50, 50, 50);
                                                    border: 4px solid black;
                                                    qproperty-textVisible: false;
                                                    border-radius: 15px;
                                                }}
                                            QProgressBar::chunk 
                                                {{
                                                        border-radius: 10px;
                                                        background-color: qlineargradient(
                                                        spread:pad,
                                                        x1:0, y1:0, x2:1, y2:0,
                                                        stop:0 yellow,
                                                        stop:1 red);

                                                }}
                                                """)


    # Below are the loading page logics
    def update_loading_label(self):
        """Update the loading text animation"""
        if self.count == 0:
            self.loading_label.setText("Loading")
            self.count += 1

        elif self.count == 1:
            self.loading_label.setText("Loading.")
            self.count += 1

        elif self.count == 2:
            self.loading_label.setText("Loading..")
            self.count += 1

        elif self.count == 3:
            self.loading_label.setText("Loading...")
            self.count = 0


    def update_bar(self):
        """Increment the loading bar value"""
        if self.loading_bar.value() < 100:
            self.loading_bar.setValue(self.loading_bar.value() + 1)

        elif self.loading_bar.value() == 100:
            self.tick.stop()
            self.timer_label.stop()
            self.load_complete()


    def load_complete(self):
        """Opens the game page | Opens the home page"""
        if game_attr.destination == 0 or game_attr.destination == 3:    # If 1 then open Game page, or if 3 then restart Game page
            sounds.bgm_home.stop()
            sounds.bgm_game.stop()
            sounds.bgm_game.play(-1)

            self.tick.stop()
            self.timer_label.stop()
            self.loading_bar.setValue(0)

            self.load_game = SnakeGame()        # Initialize SnakeGame instance
            self.load_game.setGeometry(self.geometry())
            self.load_game.show()
            self.hide()

            def reopen_page(event):
                """Reopen the loading screen"""
                if game_attr.destination != 3:
                    game_attr.destination = 1

                sounds.bgm_game.stop()
                sounds.bgm_home.play()

                self.setGeometry(self.load_game.geometry())
                self.show()

                self.timer_label.start()
                self.tick.start()
                event.accept()

            self.load_game.closeEvent = reopen_page    # Close event listener for SnakeGame page

        # Return to home page if destination value is 1
        if game_attr.destination == 1 and self.loading_bar.value() == 100:
            game_attr.destination = 1
            game_attr.load_complete = True
            game_attr.previous_geometry = self.geometry()
            self.close()