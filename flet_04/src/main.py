import flet as ft


def main(page: ft.Page):
    page.title = "Minha Primeira Tela com Flet"
    page.bgcolor = ft.Colors.BLACK
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    nome = ft.Text(
        value="Luiz Gustavo Fernandes Ferreira",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    descricao = ft.Text(
        value="Técnico em Informática - Turma 2º Ano | Aprender Python está sendo interessante, desafiador e divertido!",
        size=16,
        color=ft.Colors.GREY_400,
        text_align=ft.TextAlign.CENTER,
    )

    banner = ft.Image(
        src="https://instagram.fplu19-1.fna.fbcdn.net/v/t51.82787-19/761168339_17950587876241495_4546494401563751053_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_cat=107&ccb=7-5&_nc_sid=f7ccc5&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=nFBlsY52rIsQ7kNvwH42izY&_nc_oc=AdpbNqxmf8A9-UWidvaNVO74fbg8P31a0K3K6Ly2yczPHT1PiRKM4XPwohMbHu6QexljIIzXSyCDfNnbRsnTbbHx&_nc_zt=24&_nc_ht=instagram.fplu19-1.fna&_nc_gid=Jn1C59ipub3tXpYQw9yq5g&_nc_ss=7b6a8&oh=00_AQJxHnFD3PaE0tXmH5vN67R6o8mm9M9c4u6g3hzFCV1saA&oe=6AB0CC8F",
        width=350,
        height=350,
        fit=ft.BoxFit.CONTAIN,
        border_radius=16,
    )

    botao_perfil = ft.ElevatedButton(
        content="Meu Perfil",
        style=ft.ButtonStyle(
            bgcolor={ft.ControlState.DEFAULT: ft.Colors.RED_700, ft.ControlState.HOVERED: ft.Colors.RED_400},
            color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
            padding=ft.Padding.all(20),
        ),
    )

    botao_projetos = ft.OutlinedButton(
        content="Projetos",
        style=ft.ButtonStyle(
            side={ft.ControlState.DEFAULT: ft.BorderSide(width=2, color=ft.Colors.RED_400)},
            color={ft.ControlState.DEFAULT: ft.Colors.RED_400, ft.ControlState.HOVERED: ft.Colors.WHITE},
            bgcolor={ft.ControlState.HOVERED: ft.Colors.RED_400},
            padding=ft.Padding.all(20),
        ),
    )

    botoes = ft.Row(
        controls=[botao_perfil, botao_projetos],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    layout = ft.Column(
        controls=[
            nome,
            descricao,
            ft.Container(height=20),
            banner,
            ft.Container(height=20),
            botoes,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)