import flet as ft
from pages.home import Home_view
from pages.bgmi import bgmi_page_view
from pages.profile import profile_view

def app_connect(page):
    
    home_content = Home_view(page)
    bgmi_content = bgmi_page_view(page)
    profile_content =  profile_view(page)

    def on_nav_change(e):
            mynav_index = e.control.selected_index
            navbar_contents = [home_content, bgmi_content, profile_content]
            for index, navbar_content in enumerate(navbar_contents):
                navbar_content.visible = mynav_index == index
            page.update()

        

        
    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            ft.View(
                    "/home",
                    [
                        home_content,
                        bgmi_content,
                        profile_content,
                        ft.NavigationBar(
                            destinations=[
                                ft.NavigationDestination(icon=ft.icons.HOME_FILLED, label="Home"),
                                ft.NavigationDestination(icon=ft.icons.GAMES, label="Bgmi"),
                                ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile",),
                            ],
                            selected_index=0,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            on_change= on_nav_change,
                        )
                        
                    ]
                )
            )
        
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        if len(page.views) > 1:
            page.views.pop()
            top_view_route = page.views[-1].route
            if top_view_route != "/home" and top_view_route.startswith("/"):
                page.go("/home")
        else:
            page.go("/home")
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_settings(e):
        page.go("/settings")
        
    bgmi_content.visible = False
    profile_content.visible = False
    page.go(page.route)