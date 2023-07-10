from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.pickers import MDColorPicker
from kivymd.uix.dialog import MDDialog

from typing import Union
from qr_me import create_qr


class MainScreen(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = None

    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.45, 0.85))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    def update_color(self, color: list) -> None:
        # self.root.current = MainScreen
        self.ids.ze_label.md_bg_color = color

    def get_selected_color(
            self,
            instance_color_picker: MDColorPicker,
            type_color: str,
            selected_color: Union[list, str],
    ):
        """Return selected color."""


        self.update_color(selected_color[:-1] + [1])

    def on_select_color(self, instance_gradient_tab, color: list):
        """Called when a gradient image is clicked."""
        print("color selected")

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="QR code created !",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=(lambda x: self.dialog.dismiss())
                    ),
                ],
            )
        self.dialog.open()

    def qr_creation(self, link="https://youtu.be/dQw4w9WgXcQ", back_col="white", fill_col="black"):
        """Create the qr code from the app's settings"""
        create_qr(qr_infos=link, back_col=back_col, fill_col=fill_col)
        self.show_alert_dialog()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Red"


MyApp().run()
