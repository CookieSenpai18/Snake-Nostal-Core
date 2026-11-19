# Import necessary libraries and modules
import random
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGraphicsView, QGraphicsScene,
    QGraphicsRectItem, QGraphicsEllipseItem, QFrame, QPushButton
    )
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QBrush, QColor, QFont, QIcon
from components import sounds, game_attr, config


class SnakeSegment(QGraphicsRectItem):
    """Snake body fragment"""
    def __init__(self, x, y, size, color):
        super().__init__(0, 0, size, size)
        self.setPos(x, y)
        self.setBrush(QBrush(QColor(color)))


class Food(QGraphicsEllipseItem):
    """Food setup"""
    def __init__(self, width, height, size, color):
        # Generate a random spawn location on x and y axis
        x = random.randint(0, width // size - 1) * size
        y = random.randint(0, height // size - 1) * size

        super().__init__(0, 0, size, size)
        self.setPos(x, y)
        self.setBrush(QColor(color))

        self.coordinates = [x, y]   # Food spawn location



class SnakeGame(QMainWindow):
    """Snake Game window class"""
    def closeEvent(self, event):
        """Handle window close event"""
        event.accept()

    def __init__(self):
        super().__init__()

        # Window Setup
        self.setWindowTitle("Snake Game")
        self.setWindowIcon(QIcon(config.title_icon))
        self.setStyleSheet(config.window_style)
        self.setFixedSize(760, 820)

        # Game settings
        self.width = 700
        self.height = 700
        self.size = game_attr.ground_size
        self.head_color = 'green'
        self.body_color = 'yellow'
        self.speed = 300
        self.score = 0
        self.direction = "down"
        self.paused = True
        self.hasEnded = False

        game_attr.destination = 1   # Tells loading page to return Home page when closed


        # Score label setup
        self.score_label = QLabel("Press [Space] to Start", self)
        self.score_label.setFont(QFont("Consolas", 20, QFont.Bold))
        self.score_label.setStyleSheet("color: yellow; background-color: black;")
        self.score_label.setGeometry(130, 15, 500, 50)
        self.score_label.setAlignment(Qt.AlignCenter)

        # Background frame for visible deadend border
        self.frame = QLabel(self)
        self.frame.setStyleSheet("background-color: red;")
        self.frame.setGeometry(18, 80, self.width + 20, self.height + 20)


        # Below is the game board initialization
        # Container for all game objects
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.width, self.height)

        # Creates a visible game area
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(28, 90, self.width, self.height)
        self.view.setStyleSheet(f"border-image: url('{game_attr.ground}') stretch stretch 0 0 0 0;")
        self.view.setFixedSize(self.width, self.height)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFrameShape(QFrame.NoFrame)


        # Below are the game over elements
        # Game over label setup
        self.game_over_label = QLabel("Game Over", self)
        self.game_over_label.setStyleSheet("font-family: Consolas;"
                                           "font-weight: bold;"
                                           "font-size: 130px;"
                                           "color: red;"
                                           "background-color: black;"
                                           "padding: 0 0 250px 0;")
        self.game_over_label.setGeometry(28, 90, self.width, self.height)
        self.game_over_label.setAlignment(Qt.AlignCenter)
        self.game_over_label.hide()

        # Show final score
        self.show_score = QLabel("Final Score: ###\n\nHigh Score: ###", self)
        self.show_score.setGeometry(250, 480, 250, 100)
        self.show_score.setAlignment(Qt.AlignCenter)
        self.show_score.setStyleSheet("background-color: black;"
                                      "color: lightgray;"
                                      "font-family: Consolas;"
                                      "font-weight: bold;"
                                      "font-size: 25px;")
        self.show_score.hide()

        # Restart button setup
        self.restart_button = QPushButton("[Restart]", self, clicked=self.restart_game)
        self.restart_button.setGeometry(225, 580, 300, 75)
        self.restart_button.setStyleSheet(f""" 
                                    QPushButton 
                                        {{
                                            background: transparent;
                                            border-radius: 8px;
                                            color: yellow;
                                            font-size: 50px;
                                            font-family: Consolas;
                                            font-weight: bold;
                                        }}
                                    QPushButton:hover
                                        {{
                                            font-size: 55px;
                                        }}    
                                    QPushButton:pressed
                                        {{
                                            font-size: 35px;
                                        }}
                                    """)
        self.restart_button.hide()

        # Main menu setup
        self.main_menu = QPushButton("[Main Menu]", self, clicked=self.close_game)
        self.main_menu.setGeometry(260, 675, 230, 50)
        self.main_menu.setStyleSheet(f""" 
                                            QPushButton 
                                                {{
                                                    background: transparent;
                                                    border-radius: 8px;
                                                    color: yellow;
                                                    font-size: 30px;
                                                    font-family: Consolas;
                                                    font-weight: bold;
                                                }}
                                            QPushButton:hover
                                                {{
                                                    font-size: 35px;
                                                }}    
                                            QPushButton:pressed
                                                {{
                                                    font-size: 25px;
                                                }}
                                            """)
        self.main_menu.hide()


        # Below are the pause panel elements
        # Frame panel for pause elements
        self.pause_panel = QLabel(self)
        self.pause_panel.setGeometry(150, 250, 450, 250)
        self.pause_panel.setStyleSheet("background-color: rgb(166, 227, 113);"
                                       "border-radius: 15px;"
                                       "border: 4px solid black;")
        # Pause title label setup
        self.pause_label = QLabel("[PAUSED]",self)
        self.pause_label.setGeometry(275, 260, 200, 50)
        self.pause_label.setAlignment(Qt.AlignCenter)
        self.pause_label.setStyleSheet("color: black;"
                                       "font: bold 35px Comic Sans MS, Arial;")

        # Resume button setup
        self.resume_button = QPushButton("Resume", self, clicked=self.toggle_pause)
        self.resume_button.setGeometry(275, 340, 200, 50)
        self.resume_button.setStyleSheet(f"""
                                    QPushButton 
                                        {{
                                            background-color: rgb(51, 126, 245);
                                            border: 3px solid black;
                                            border-radius: 15px;
                                            font-family: Comic Sans MS, Arial;
                                            font-weight: bold;
                                            font-size: 25px;
                                        }}
                                    QPushButton:hover
                                        {{
                                            background-color: rgb(42, 104, 201);
                                            font-size: 29px;
                                            border: 2px solid black;
                                            padding-bottom: 3px;
                                        }}
                                    QPushButton:pressed
                                        {{
                                            background-color: rgb(38, 87, 170);
                                            font-size: 20px;
                                            border: 5px solid black;
                                        }}
                                        """)

        # Manu button setup
        self.menu_button = QPushButton("Main Menu", self, clicked=self.close_game)
        self.menu_button.setGeometry(275, 415, 200, 50)
        self.menu_button.setStyleSheet(f"""
                                    QPushButton 
                                        {{
                                            background-color: rgb(51, 126, 245);
                                            border: 3px solid black;
                                            border-radius: 15px;
                                            font-family: Comic Sans MS, Arial;
                                            font-weight: bold;
                                            font-size: 22px;
                                        }}
                                    QPushButton:hover
                                        {{
                                            background-color: rgb(42, 104, 201);
                                            font-size: 26px;
                                            border: 2px solid black;
                                            padding-bottom: 3px;
                                        }}
                                    QPushButton:pressed
                                        {{
                                            background-color: rgb(38, 87, 170);
                                            font-size: 17px;
                                            border: 5px solid black;
                                        }}
                                        """)


        # Below is the creation of snake
        # Creating snake model
        self.snake_segments = []
        self.snake_coordinates = [[0, 0] for _ in range(3)]
        for x, y in self.snake_coordinates:
            seg = SnakeSegment(x, y, self.size, self.head_color)
            self.scene.addItem(seg)
            self.snake_segments.append(seg)
        self.snake_segments[1].setBrush(QColor(self.body_color))


        # Create and spawn food randomly
        self.food = Food(self.width, self.height, self.size, "red")
        self.scene.addItem(self.food)


        # This timer acts as game speed
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_turn)
        self.timer.start(self.speed)    # Game speed, lower value = faster game


        self.hide_pause()

        # Prevents the QGraphicsView from interrupting arrow keys from being use
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()



    # Below are the game logic
    def toggle_pause(self):
        """Open/Close pause panel"""
        self.paused = not self.paused
        if self.paused and not self.hasEnded:
            self.score_label.setText(f"Score: {self.score}   [PAUSED]")
            self.score_label.setGeometry(125, 15, 500, 50)
            self.show_pause()

        else:
            self.score_label.setText(f"Score: {self.score}")
            self.score_label.setGeometry(250, 15, 250, 50)
            self.hide_pause()


    def show_pause(self):
        """Show pause panel"""
        self.pause_panel.show()
        self.pause_label.show()
        self.resume_button.show()
        self.menu_button.show()

    def hide_pause(self):
        """Hide pause panel"""
        self.pause_panel.hide()
        self.pause_label.hide()
        self.resume_button.hide()
        self.menu_button.hide()


    def keyPressEvent(self, event):
        """Detects user key press"""
        key = event.key()   # User keypress

        if key == Qt.Key_Space:     # <Space>
            self.toggle_pause()

        elif key in (Qt.Key_Left, Qt.Key_A):    # <A> or <Left arrow>
            self.change_direction("left")

        elif key in (Qt.Key_Right, Qt.Key_D):   # <B> or <Right arrow>
            self.change_direction("right")

        elif key in (Qt.Key_Up, Qt.Key_W):      # <W> or <Up arrow>
            self.change_direction("up")

        elif key in (Qt.Key_Down, Qt.Key_S):    # <S> or <Down arrow>
            self.change_direction("down")


    def change_direction(self, new_dir):
        """Change the direction of the snake"""
        opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}    # Prevent the snake from moving backwards directly
        if new_dir != opposites[self.direction]:
            self.direction = new_dir


    def next_turn(self):
        """Switch frame for snake animation"""
        if self.paused:     # Prevent the snake moving when paused
            return

        x, y = self.snake_coordinates[0]
        # Snake move direction based on keypress
        if self.direction == "up":
            y -= self.size
        elif self.direction == "down":
            y += self.size
        elif self.direction == "left":
            x -= self.size
        elif self.direction == "right":
            x += self.size

        # Create a new snake head based on direction
        self.snake_coordinates.insert(0, [x, y])
        new_seg = SnakeSegment(x, y, self.size, self.head_color)
        self.scene.addItem(new_seg)
        self.snake_segments.insert(0, new_seg)
        self.snake_segments[1].setBrush(QColor(self.body_color))

        # Eat food on snake collision
        if [x, y] == self.food.coordinates:
            sounds.bite_sfx.play()
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")

            self.scene.removeItem(self.food)   # Remove the food
            self.food = Food(self.width, self.height, self.size, "red")     # Create a new food with random pos
            self.scene.addItem(self.food)    # Spawn the new food

            self.update_speed()     # Notify the function that the score increased

        else:
            # Remove the last tail fragment
            tail = self.snake_segments[-1]
            self.scene.removeItem(tail)
            self.snake_segments.pop()
            self.snake_coordinates.pop()

        # Check for walls/self collision
        if self.check_collision():
            self.game_over()


    def check_collision(self):
        """Checks if snake collide with itself or walls"""
        x, y = self.snake_coordinates[0]

        # Wall collision
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True

        # Self collision
        if [x, y] in self.snake_coordinates[1:]:
            return True

        return False


    def update_speed(self):
        """Update snake speed"""
        if self.score in {5, 10, 15, 20}:   # Increase snake speed every 5 pts
            self.speed -= 50
            sounds.level_up_sfx.play()

        elif self.score == 35:              # Increase the speed slightly when reached 35 pts
            self.speed -= 20
            sounds.level_up_sfx.play()

        self.timer.setInterval(self.speed)


    def game_over(self):
        """Game over frame"""
        sounds.bgm_game.stop()
        sounds.game_over.play()

        # Stops the timer and mark the game ended
        self.timer.stop()
        self.hasEnded = True

        # Show game over elements
        self.game_over_label.show()
        self.score_label.hide()
        self.restart_button.show()
        self.show_score.show()
        self.main_menu.show()

        # Display the player final score
        if self.score > game_attr.high_score:       # Show new highest if current score > high score
            self.show_score.setText(f"New High Score: {self.score}")
            print("New High")
            game_attr.high_score = self.score
            game_attr.update_score()

        else:       # Shows normal result if current score < high score
            self.show_score.setText(f"Final Score: {self.score}\n\nHigh Score: {game_attr.high_score}")
            print("Usual Score")


    def restart_game(self):
        """Reopen loading page and return in this page"""
        sounds.click_sfx.play()
        game_attr.destination = 3   # Tells Home page not to open
        self.close()

    def close_game(self):
        """Reopen loading page and return to Home page"""
        sounds.click_sfx.play()
        self.timer.stop()
        self.close()