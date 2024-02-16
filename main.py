import flet as ft
from connect.application import app_connect

def main(page: ft.Page):
    
    page.theme_mode= "light"
    page.padding=0
    page.window_title_bar_hidden=True
    page.window_width = 380
    page.window_height = 740
    page.horizontal_alignment = "start"
         
    connecting = app_connect(page)
    
    page.add(connecting)
    page.update()
    
ft.app(target=main, assets_dir="assets")
