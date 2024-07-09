import flet as ft


def TextInput(label: str, hint_text: str, prefix_icon: ft.icons, keyboard_type: ft.KeyboardType, password: bool = False, can_reveal_password: bool = False):
    return ft.TextField(
        label=label,
        bgcolor=ft.colors.BLACK12,
        password= password,
        can_reveal_password=can_reveal_password,
        label_style=ft.TextStyle(size=15, color=ft.colors.BLACK),
        hint_text=hint_text,
        hint_style=ft.TextStyle(size=15, color=ft.colors.BLACK54),
        focused_border_color=ft.colors.GREY_800,
        cursor_color=ft.colors.GREY_800,
        text_style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.W_600),
        prefix_icon=prefix_icon,
        keyboard_type=keyboard_type,
        
    )