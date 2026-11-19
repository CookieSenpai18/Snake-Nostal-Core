"""All of the file accessing code are written here so other modules doesn't have to."""
# Import necessary libraries
import pygame, json, os, inspect


class GetSavedData:
    """Retrieve the save data locally"""
    def __init__(self):
        # List of retrievable datas
        self.version = 'Version 0.1 Build 4'    # Version code
        self.username = str() or "Player"
        self.bgm_volume = float() or 0.4
        self.sfx_volume = float() or 0.4
        self.high_score = int() or 0
        self.first_time = int() or 0
        self.game_size = int() or 50
        self.ground_index = int() or 0
        self.data_path = 'game_data/snake_gamedata.json'    # Data collection path

        self.load_data()


    def load_data(self):
        """Update the global variables based on local data"""
        try:
            if os.path.exists(self.data_path):
                with open(self.data_path, 'r') as f:
                    data = json.load(f)
                    self.username = data['username']
                    self.bgm_volume = data['bgm_volume']
                    self.sfx_volume = data['sfx_volume']
                    self.high_score = data['high_score']
                    self.first_time = data['first_time']
                    self.game_size = data['game_size']
                    self.ground_index = data['ground_index']
                    print(f"{inspect.currentframe().f_lineno} Save data successfully loaded")

            else:
                 self.save_data()
                 print("No saved data detected...\nA new one was created")

        except:
            self.save_data()
            return f"{inspect.currentframe().f_lineno} There was a problem on save data.\nAttempting to create a new one..."


    def save_data(self):
        """Create new save data if it doesn't exist"""
        data = dict()
        data['username'] = self.username
        data["bgm_volume"] = self.bgm_volume
        data["sfx_volume"] = self.sfx_volume
        data["high_score"] = self.high_score
        data["first_time"] = self.first_time
        data["game_size"] = self.game_size
        data["ground_index"] = self.ground_index

        with open(self.data_path, 'w') as f:
            json.dump(data, f, indent=4)


class Sounds:
    """Initialize bgm and sfx"""
    def __init__(self):

        self.saved_data = GetSavedData()    # Collect retrieved data

        # Get the initial volumes from local data
        self.bgm_vol = self.saved_data.bgm_volume
        self.sfx_vol = self.saved_data.sfx_volume
        pygame.mixer.init()

        self.REDUCE_VOL = 0.75      # Reduce the Home BGM volume intensity cause it's louder than Game BGM

        # Homepage BGM setup
        self.bgm_home = pygame.mixer.Sound('Audio/homepage.wav')
        self.bgm_home.set_volume(self.bgm_vol * self.REDUCE_VOL)

        # Game BGM setup
        self.bgm_game = pygame.mixer.Sound('Audio/gameplay.wav')
        self.bgm_game.set_volume(self.bgm_vol)


        # Click SFX setup
        self.click_sfx = pygame.mixer.Sound('Audio/click.mp3')
        self.click_sfx.set_volume(self.sfx_vol)

        # Snake bite SFX setup
        self.bite_sfx = pygame.mixer.Sound('Audio/bite_sfx.mp3')
        self.bite_sfx.set_volume(self.sfx_vol)

        # Speed increase SFX
        self.level_up_sfx = pygame.mixer.Sound('Audio/lvlup.mp3')
        self.level_up_sfx.set_volume(self.sfx_vol)

        # Game Over SFX setup
        self.game_over = pygame.mixer.Sound('Audio/gameover.mp3')
        self.game_over.set_volume(self.sfx_vol)



    # Below are the sound logics
    def update_bgm(self, intensity):
        """Update bgm volume intensity when setting adjusted"""
        self.bgm_vol = intensity / 100
        self.bgm_home.set_volume(self.bgm_vol * self.REDUCE_VOL)
        self.bgm_game.set_volume(self.bgm_vol)


    def update_sfx(self, intensity):
        """Update sfx volume intensity when setting adjusted"""
        self.sfx_vol = intensity / 100
        self.click_sfx.set_volume(self.sfx_vol)
        self.bite_sfx.set_volume(self.sfx_vol)
        self.level_up_sfx.set_volume(self.sfx_vol)
        self.game_over.set_volume(self.sfx_vol)


    def update_data(self):
        """Update volume data with new adjusted one"""
        with open(self.saved_data.data_path, 'r') as f:
            temp_data = json.load(f)

            temp_data['bgm_volume'] = self.bgm_vol
            temp_data['sfx_volume'] = self.sfx_vol

        with open(self.saved_data.data_path, 'w') as f:
            json.dump(temp_data, f, indent=4)


class GameAttr:
    """Initialize game attributes"""
    def __init__(self):
        self.destination = 1                # 1 => 0 Game | 0 => 1 Home | (Guide for loading page where to land)
        self.load_complete = False
        self.previous_geometry = (0, 0, 0, 0)

        # Collect retrieved data
        self.saved_data = GetSavedData()
        self.version = self.saved_data.version
        self.username = self.saved_data.username
        self.high_score = self.saved_data.high_score
        self.ground_size = self.saved_data.game_size
        self.ground_index = self.saved_data.ground_index

        # Names of environments
        self.ground_name = ['Grass', 'Drought', 'Molten', 'Cursed Silhouette', 'Crystic', 'Definitely not Earth', 'Dream']

        # Environment to use in game
        self.ground = f"Image/Grounds/ground{self.ground_index}.jpg"

    # Below are the game attr logics
    def update_username(self):
        """Save user profile"""
        if self.username == "CookieSenpai":
            self.high_score = 100

        with open(self.saved_data.data_path, 'r') as f:
            data = json.load(f)
            data['username'] = self.username
            data['high_score'] = self.high_score

        with open(self.saved_data.data_path, 'w') as f:
            json.dump(data, f, indent=4)


    def update_ground(self):
        """Update ground image to show in config info and in game"""
        if not self.username == "Autumn843y":
            self.ground = f"Image/Grounds/ground{self.ground_index}.jpg"

        else:
            self.ground = f"Image/Grounds/world.jpg"


    def save_game_config(self):
        """Save user game configuration"""
        with open(self.saved_data.data_path, 'r') as f:
            data = json.load(f)
            data['game_size'] = self.ground_size
            data['ground_index'] = self.ground_index

        with open(self.saved_data.data_path, 'w') as f:
            json.dump(data, f, indent=4)


    def update_score(self):
        """Update saved high score"""
        with open(self.saved_data.data_path, 'r') as f:
            data = json.load(f)
            data['high_score'] = self.high_score

        with open(self.saved_data.data_path, 'w') as f:
            json.dump(data, f, indent=4)


class WindowConfig:
    """Windows setup"""
    def __init__(self):
        self.background_image = 'Image/snake_bg.jpg'
        self.window_style = f"""QMainWindow {{border-image: url('{self.background_image}') stretch stretch 0 0 0 0;}}"""
        self.title_icon = 'Image/app_icon.png'

        self.snake_image = 'Image/snake_tran.png'
        self.home_title = 'Image/title_label.png'

        self.custom_label = 'Image/game_setup.png'
        self.ground_image = 'Image/Grounds/ground'

        self.about_title = 'Image/about_label.png'

        self.settings_label = 'Image/settings_frame.png'


# Create global instances
game_attr = GameAttr()
sounds = Sounds()
config = WindowConfig()