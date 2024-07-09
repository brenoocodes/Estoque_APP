import flet as ft
import time
from src.pages.cadastro.colunas_itens import coluna

def Cadastro(page: ft.Page):
    container_login = ft.Container(
        width=page.width,
        bgcolor=ft.colors.WHITE,
        height=page.height * 4 / 5,
        padding=ft.padding.symmetric(vertical=20, horizontal=15),
        margin=0,
        border_radius=ft.border_radius.only(top_left=50),
        animate_offset=ft.animation.Animation(1000),
        content=coluna(page=page)
    )
        

    container_principal = ft.Container(
        width=page.width,
        image_src='images/capa.png',
        image_fit=ft.ImageFit.COVER,
        padding=0,
        expand=True,
        alignment=ft.alignment.bottom_center,
        content=container_login
    )
    
    return container_principal