import flet as ft

def Login(page: ft.Page):
    container = ft.Container(
        width=page.width,
        bgcolor=ft.colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Text(
            value='Página Login',
            color=ft.colors.BLACK,
            size=50
        )
    )
    return container