import flet as ft

def TextInput(label: str, hint_text: str, prefix_icon: ft.icons, password: bool, keyboard_type: ft.KeyboardType):
    return ft.TextField(
        label=label,
        password= password,
        label_style=ft.TextStyle(size=15, color=ft.colors.BLACK),
        hint_text=hint_text,
        hint_style=ft.TextStyle(size=15, color=ft.colors.BLACK87),
        focused_border_color=ft.colors.GREY_800,
        cursor_color=ft.colors.GREY_800,
        text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.W_600),
        prefix_icon=prefix_icon,
        keyboard_type=keyboard_type,
        
    )
email = TextInput(label='E-mail', hint_text='Digite seu email: ', prefix_icon=ft.icons.EMAIL, password=False, keyboard_type=ft.KeyboardType.EMAIL)
coluna = ft.Column(
    spacing=25,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[
        ft.Text(value='LOGIN', weight=ft.FontWeight.W_900, color=ft.colors.BLACK),
        email
    ]
)