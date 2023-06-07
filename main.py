from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.button import MDIconButton
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.factory import Factory
from kivymd.toast import toast
import mysql.connector
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
from kivymd.uix.behaviors import CommonElevationBehavior
Window.size = (1000,600)
List_of_emailid = []
database = mysql.connector.Connect(host='localhost', user='root', password='password', database='login')
cursor = database.cursor()
cursor.execute('select * from logindata')
Dictionary_of_login_details={}
for i in cursor.fetchall():
    List_of_emailid.append(i[0].lower())
    Dictionary_of_login_details[i[0].capitalize()] = i[1]
print(List_of_emailid)
print(Dictionary_of_login_details)
user = ['Gaming']
class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("C:\\Users\\sreej\\Downloads\\wake-up-to-the-renaissance-135540.mp3")
        self.sound.loop = True
        self.sound.play()

class WorldOfGaming(MDApp):
    database = mysql.connector.Connect(host='localhost', user='root', password='password', database='login')
    cursor = database.cursor(buffered=True)
    SNO = len(Dictionary_of_login_details)+1
    user_name=user[-1]
    video = 'TRUE'
    source='SUDOKU.png'
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('sudoku.kv'))
        screen_manager.add_widget(Builder.load_file('welcome.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('createaccount.kv'))
        screen_manager.add_widget(Builder.load_file('homepage.kv'))
        screen_manager.add_widget(Builder.load_file('resetpassword.kv'))
        screen_manager.add_widget(Builder.load_file('leaderboard.kv'))
        screen_manager.add_widget(Builder.load_file('settings.kv'))
        #screen_manager.add_widget(Builder.load_file('sudoku.kv'))
        screen_manager.add_widget(Builder.load_file('swiper.kv'))
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        """player = VideoPlayer(source="D:\Python programs\Winner.mp4")
        player.state = 'play'
        player.allow_stretch = True
        if self.video == 'TRUE':
            self.video = 'FALSE'
            return player
        else:
            return screen_manager"""
        return screen_manager

    def table(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.35, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(10)),
                ("Username", dp(25)),
                ("Points", dp(15)),
            ],
            row_data=[
                (f"{i + 1}", "1", "2") for i in range(50)
            ],
        )
        layout.add_widget(data_tables)
        return layout
    def send_data(self,username,Password,email,info):
        user.append(str(username.text).capitalize())
        print(user)
        if info == 'user':
            return self.variable
        elif info == 'login' and (username.text == '' or Password.text == ''):
            self.variable = 'notdone'
            toast('Please fill the fields')
        elif info != 'login'  and (username.text == '' or Password.text == ''or email.text==''):
            self.variable = 'notdone'
            toast('Please fill the fields')
        elif info == 'reset password':
            self.variable = 'notdone'
            if str(username.text).capitalize() in Dictionary_of_login_details.keys() and str(email.text).lower() in List_of_emailid:
                user.append(str(username.text).capitalize())
                self.variable = 'done'
                Dictionary_of_login_details[str(username.text).capitalize()] = str(Password.text)
                username.text = ''
                Password.text = ''
                email.text = ''
                #return MainLayout()
            elif str(username.text).capitalize() not in Dictionary_of_login_details.keys():
                self.variable = 'notdone'
                toast("Username doesn't exist")
            elif str(email.text).lower() not in Dictionary_of_login_details.keys():
                self.variable = 'notdone'
                toast("Wrong email-id")
        else:
            if str(username.text).capitalize() in Dictionary_of_login_details.keys() and info == 'create account':
                self.variable = 'notdone'
                toast('Username already exists')
                username.text = ''
                Password.text = ''
                email.text = ''
            elif str(username.text).capitalize() in Dictionary_of_login_details.keys() and info == 'login':
                if Password.text == Dictionary_of_login_details[str(username.text).capitalize()]:
                    user.append(str(username.text).capitalize())
                    self.variable = 'done'
                    username.text = ''
                    Password.text = ''
                    #return MainLayout()
                else:
                    self.variable = 'notdone'
                    toast('Incorrect password entered')
                    Password.text = ''
            elif str(username.text).capitalize() not in Dictionary_of_login_details.keys() and info == 'login':
                self.variable = 'notdone'
                toast("Username doesn't exist")
            else:
                username.text=(str(username.text).capitalize())
                user.append(str(username.text).capitalize())
                self.variable = 'done'
                self.cursor.execute(f"insert into logindata values('{username.text}','{Password.text}')")
                self.database.commit()
                cursor = database.cursor(buffered=True)
                cursor.execute('select * from logindata')
                Dictionary_of_login_details[str(username.text).capitalize()]=str(Password.text)
                username.text = ''
                Password.text = ''
                email.text=''
                #return MainLayout()
    def homescreen(self):
        pass
if __name__ == '__main__':
    LabelBase.register(name="MRoboto", fn_regular="D:\\Python programs\\Roboto\\Roboto-Medium.ttf")
    WorldOfGaming().run()