import flet as ft


def Home_view(page):
    
    
    home_content = ft.Column([
                        ft.Column([
                            ft.Image(
                                src=f"../assets/component/images/bgmi_5.jpg",
                                width=400,
                                height= 140,
                                fit=ft.ImageFit.COVER,
                            ),
                        ], spacing=1),
                        
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.GAMEPAD_OUTLINED),
                                                title=ft.Text("Bgmi Events"),
                                                subtitle=ft.Text(
                                                    "Join your favorite bgmi event and win your reward!"
                                                ),
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.CHAT_ROUNDED),
                                                title=ft.Text("Community chat"),
                                                subtitle=ft.Text(
                                                    "Join our community chat to share your thoughts with us."
                                                ),
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.GROUP),
                                                title=ft.Text("Public groups"),
                                                subtitle=ft.Text(
                                                    "Join the public groups to share your messages to other users"
                                                ),
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.PODCASTS),
                                                title=ft.Text("Review the public post"),
                                                subtitle=ft.Text(
                                                    "Join with us to review the creators post"
                                                ),
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ), 
                                
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.VIDEO_CALL),
                                                title=ft.Text("Podcast"),
                                            ),
                                        ]
                                    ),
                                    width=170,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.STREAM_OUTLINED),
                                                title=ft.Text("Go Live"),
                                            ),
                                        ]
                                    ),
                                    width=170,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                    border_radius=10
                                ),
                                
                            ]
                        ),
                    ], expand=True, scroll=True)

    return home_content
