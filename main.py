import flet as ft

def main(page: ft.Page):
    page.title = "Meu app"
    page.add(
        ft.Text(
        "Bem-vindo ao meu app!",
        size=24,
        weight=ft.FontWeight.W_600,
        color="red",

    ),
        ft.Text("Eu me chamo Guilhermy."),
        ft.Button(
            content="botão ativado"
        ),
        ft.Button(
            content="botão desativado",
            disabled=True
        ),
        ft.Button(
            content="botão colorido",
            bgcolor="blue",
            color="white"
        ),
        ft.Image(
            src="https://www.sp.senai.br/images/senai.svg",
            width=150,
            height=150
        )
    )

ft.app(main)