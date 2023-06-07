from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationrail import MDNavigationRail
from kivymd.uix.navigationrail import MDNavigationRailItem

KV = '''
Screen:

    MDNavigationRail:
        id: navrail
        md_bg_color: app.theme_cls.bg_dark
        color_normal: app.theme_cls.text_color
        color_active: app.theme_cls.accent_color
        elevation: 10
        # This item will move the MDNavigationDrawer from the left to the right
        MDNavigationRailItem:
            icon: "menu"
            on_release: app.root.toggle_nav_drawer()

    MDNavigationDrawer:
        id: navdrawer
        md_bg_color: app.theme_cls.bg_dark
        NavigationDrawerSubheader:
            text: "Navigation Drawer"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
        NavigationDrawerIconButton:
            icon: "android"
            text: "Item 1"
            on_release: app.root.nav_drawer.set_state("close")
        NavigationDrawerIconButton:
            icon: "apple"
            text: "Item 2"
            on_release: app.root.nav_drawer.set_state("close")
        NavigationDrawerIconButton:
            icon: "windows"
            text: "Item 3"
            on_release: app.root.nav_drawer.set_state("close")

    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Main Window"
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
        MDBottomAppBar:
            mode: "end"
            type: "bottom"
            icon: "plus"
            on_action_button: app.navigation_draw()
'''


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def navigation_draw(self):
        if self.root.ids.navdrawer.state == "open":
            self.root.ids.navdrawer.set_state("close")
        else:
            self.root.ids.navdrawer.set_state("open")

    def toggle_nav_drawer(self):
        if self.root.ids.navdrawer.state == "open":
            self.root.ids.navdrawer.set_state("close")
        else:
            self.root.ids.navdrawer.set_state("open")


if __name__ == "__main__":
    TestApp().run()