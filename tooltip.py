'''MDNavigationDrawer:
id: nav_drawer
radius: (0, 16, 16, 0)
MDNavigationDrawerMenu:
MDNavigationDrawerHeader:

title: 'df'
title_color: "#4a4939"
text: "Header text"
spacing: "4dp"
padding: "12dp", 0, 0, "56dp"

DrawerClickableItem:
icon: "account-supervisor"
text: "Leaderboard"
on_release:
root.manager.transition.direction = 'right'
root.manager.current = 'leaderboard'

DrawerClickableItem:
icon: "cog-outline"
text: "Settings"
on_release:
root.manager.transition.direction = 'up'
root.manager.current = 'settings'
DrawerClickableItem:
icon: "search-web"
text: "References"
DrawerClickableItem:
icon: "exit-to-app"
text: "Exit"
on_release:
Window.close()
MDNavigationDrawerDivider:
DrawerClickableItem:
text: "Log Out"
icon: 'logout'
on_release:
app.SNO += 1
root.manager.transition.direction = 'down'
root.manager.current = 'welcome' '''



from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

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


Example().run()