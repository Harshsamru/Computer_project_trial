from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton

KV = '''
MDScreen:
    md_bg_color: "#f7f2fa"

    MDBoxLayout:
        id: box1
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .75}
        
    MDBoxLayout:
        id: box2
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .75}
    MDBoxLayout:
        id: box3
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .75}
    MDBoxLayout:
        id: box4
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .68}
    MDBoxLayout:
        id: box5
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .68}
    MDBoxLayout:
        id: box6
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .68}
    MDBoxLayout:
        id: box7
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .61}
    MDBoxLayout:
        id: box8
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .61}
    MDBoxLayout:
        id: box9
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .61}
    MDBoxLayout:
        id: box10
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .53}
    MDBoxLayout:
        id: box11
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .53}
    MDBoxLayout:
        id: box12
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .53}
    MDBoxLayout:
        id: box13
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .46}
    MDBoxLayout:
        id: box14
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .46}
    MDBoxLayout:
        id: box15
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .46}
    MDBoxLayout:
        id: box16
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .39}
    MDBoxLayout:
        id: box17
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .39}
    MDBoxLayout:
        id: box18
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .39}
    MDBoxLayout:
        id: box19
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .31}
    MDBoxLayout:
        id: box20
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .31}
    MDBoxLayout:
        id: box21
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .31}
    MDBoxLayout:
        id: box22
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .24}
    MDBoxLayout:
        id: box23
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .24}
    MDBoxLayout:
        id: box24
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .24}
    MDBoxLayout:
        id: box25
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .33, "center_y": .17}
    MDBoxLayout:
        id: box26
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .17}
    MDBoxLayout:
        id: box27
        spacing: "3dp"
        adaptive_size: True
        pos_hint: {"center_x": .67, "center_y": .17}
    MDFloatingActionButton:
        id: profile
        icon:'account'
        type:'standard'
        md_bg_color:"#fefbff"
        theme_icon_color:"Custom"
        icon_color:"#6851a5"
        pos_hint: {"center_x": .034, "center_y": .89}
        on_release:
            icon_color='black'
        
                    
        
    
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        data={}
        for i in range(3):
            data['B'+str(i)]={"md_bg_color": "#fefbff", "text_color": "#6851a5"}

        for type_button in data.keys():
            self.root.ids.box1.add_widget(
                MDFloatingActionButton(
                    icon="1",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint= {"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],

                )
            )
            self.root.ids.box2.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box3.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box4.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box5.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box6.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box7.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box8.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box9.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box10.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box11.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box12.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box13.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box14.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box15.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box16.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box17.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box18.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box19.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box20.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box21.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box22.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box23.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box24.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box25.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box26.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )
            self.root.ids.box27.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type='small',
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    pos_hint={"center_x": .2, "center_y": .8},
                    icon_color=data[type_button]["text_color"],
                )
            )



Example().run()