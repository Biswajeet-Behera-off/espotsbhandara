import flet as ft


def bgmi_page_view(page):
    
    
    bgmi_event_view = ft.Column(
                        [
                        ft.Container(
                                content=ft.Text("Hello"),
                                padding=10,
                                expand=True,
                            )
                        ], expand=2)

    return bgmi_event_view