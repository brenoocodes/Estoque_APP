import flet as ft

estilo_botao_principal = ft.ButtonStyle(
    animation_duration=2000,
    elevation=None,
    color={
      ft.MaterialState.DEFAULT: '#ffffff',
      ft.MaterialState.HOVERED: '#ffffff' 
    },
    bgcolor={
        ft.MaterialState.DEFAULT: ft.colors.BLUE,
        ft.MaterialState.HOVERED: '#410088',
        ft.MaterialState.DISABLED: ft.colors.GREY
    }

)