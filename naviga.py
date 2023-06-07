from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.tooltip import MDTooltip

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<ExtendedButton>
    elevation: 3.5
    shadow_radius: 12
    shadow_softness: 4
    -height: "56dp"
<TooltipMDIconButton@MDIconButton+MDTooltip>
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout:
                        adaptive_height: True
                        md_bg_color: "#fffcf4"
                        padding: "12dp"
                    MDBoxLayout:
                        MDNavigationRail:
                            
                            type: "unselected"
                            id: navigation_rail
                            md_bg_color: "#fffcf4"
                            selected_color_background: "#e7e4c0"
                            ripple_color_item: "#e7e4c0"
                            on_item_release: app.switch_screen(*args)
                            MDNavigationRailFabButton:
                                tooltip_text: "Leaderboard"
                                icon:'home'
                                md_bg_color: "#b0f0d6"
                            
                            MDNavigationRailItem:
                                tooltip_text: "Leaderboard"
                                icon: "account-supervisor"

                            MDNavigationRailItem:
                                text: "Settings"
                                icon: "cog-outline"

                            MDNavigationRailItem:
                                text: "Reference"
                                icon: "search-web"

                            MDNavigationRailItem:
                                text: "Exit"
                                icon: "exit-to-app"
                            
                            MDNavigationRailItem:
                                text: "Log out"
                                icon: "exit-to-app"
                            

                        ScreenManager:
                            id: screen_manager
                            transition:
                                FadeTransition(duration=.2, clearcolor=app.theme_cls.bg_dark)


'''


class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item
    ):
        self.root.ids.screen_manager.current = (
            instance_navigation_rail_item.icon.split("-")[1].lower()
        )

    def on_start(self):
        '''Creates application screens.'''

        navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            name_screen = widget.icon.split("-")[1].lower()
            screen = MDScreen(
                name=name_screen,
                md_bg_color="#edd769",
                radius=[18, 0, 0, 0],
            )
            box = MDBoxLayout(padding="12dp")
            label = MDLabel(
                text=name_screen.capitalize(),
                font_style="H1",
                halign="right",
                adaptive_height=True,
                shorten=True,
            )
            box.add_widget(label)
            screen.add_widget(box)
            self.root.ids.screen_manager.add_widget(screen)

Example().run()