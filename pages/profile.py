import flet as ft


def profile_view(page):
    
    profile_page_view = ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Image(
                                                src=f"./assets/component/images/logo.JPG",
                                                fit=ft.ImageFit.COVER,
                                                ),
                                                
                                                title=ft.Column(
                                                    [
                                                        ft.Text(f"Name: Biswajeet Behera", size=20),
                                                        ft.Text("Uid: 14325978", size=20),
                                                        ft.Text("Age: 21" ,size=20),
                                                    ], spacing=0     
                                                )
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    margin = 0,
                                    bgcolor=ft.colors.DEEP_PURPLE_100,
                                ),
                                
                            ], expand=True,scroll=ft.ScrollMode.HIDDEN,)

    return profile_page_view