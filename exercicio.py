import flet as ft

def main(page: ft.Page):
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def mostrar_mensagem(e):
        page.add(ft.Text("Capa💀"))

    page.add(
        ft.Text("Olá, jogador de Free Fire!"),
        ft.Image(
            src="images/Free Fire.jpg",
            height=200
        ),
        ft.Button(
            content="Seja um capudo",
            on_click=mostrar_mensagem
        )
    )

ft.app(main)