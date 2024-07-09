import flet as ft
from src.style.botao import estilo_botao_principal
from src.components.textinput import TextInput
def logar_com_google(e):
    print('Olá mundo')

def logar_com_apple(e):
    print('Olá mundo')

nome = TextInput(label='Nome', hint_text='Digite seu nome: ', prefix_icon=ft.icons.PERSON, keyboard_type=ft.KeyboardType.TEXT)

email = TextInput(label='E-mail', hint_text='Digite seu email: ', prefix_icon=ft.icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL)


senha = TextInput(label='Senha', hint_text='Digite seu senha: ', password=True, can_reveal_password=True, prefix_icon=ft.icons.PASSWORD_SHARP, keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD)

confirme_senha = TextInput(label='Confirme sua senha', hint_text='Digite sua senha novamente: ', password=True, can_reveal_password=True, prefix_icon=ft.icons.PASSWORD_SHARP, keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD)

botao = ft.ResponsiveRow(
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        ft.ElevatedButton(
            text='Cadastrar',
            col=5,
            style=estilo_botao_principal
        )
    ]
)



def coluna(page: ft.Page): 
    linha = ft.ResponsiveRow(
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=0,
    run_spacing=0,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[
        ft.Text(value='Já tem conta criada ? faça ',color=ft.colors.BLACK, col=7, text_align=ft.TextAlign.RIGHT),
        ft.TextButton(text='login', col=2, on_click=lambda _: page.go('/login') , style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: ft.colors.BLUE,
                ft.MaterialState.HOVERED: ft.colors.BLUE_200
            },
            bgcolor=ft.colors.TRANSPARENT,
            padding=0,
            
        ))
    ]
)
    return ft.Column(
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Text(value='CRIE SUA CONTA', weight=ft.FontWeight.W_900, color=ft.colors.BLACK),
            nome,
            email,
            senha,
            confirme_senha,
            botao,
            linha
        ]
    )