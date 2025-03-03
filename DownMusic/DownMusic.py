import flet as ft
from Script import download_API 
import time


def main(page: ft.Page):
    page.bgcolor = 'blue100'
    page.title = "DownMusic"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 700
    page.window.height = 600
    page.padding = 20
    page.window.min_width = 400
    page.window.min_height = 600
    
    avisor = download_API().aviso
    
    def baixar(e):
        aviso.color = 'black'
        aviso.value = 'Carregando...'
        botao.disabled = True
        page.update()
        time.sleep(1)
        if link_music.value == "":
            aviso.color = 'blacK'
            aviso.value = "Digite o link para realizar o download!"
            botao.disabled = False
            page.update()
            
        elif download_API().audio(link_music.value) == "COMPLETE":
            aviso.color = "green"
            aviso.value = "Download Completo."
            botao.disabled = False
            page.update()
            
        else:
            aviso.color = "RED"
            aviso.value = f'Não foi possível localizar o endereço.'
            botao.disabled = False
            page.update()

    link_music = ft.TextField(hint_text='Digite o link aqui...', text_align=ft.TextAlign.LEFT, width=350, bgcolor="white")
    
    aviso = ft.Text(avisor, size=25, font_family="Arial", weight=ft.FontWeight.BOLD)
    
    intro_text = ft.Container(
                        content = ft.Text('Baixar vídeos do youtube rapidamente, convertidos em mp3', size=25, weight = ft.FontWeight.BOLD, font_family="Arial", text_align=ft.TextAlign.CENTER, color='black'),
                        margin = ft.margin.only(bottom=50),
                        alignment = ft.alignment.center,
                        #bgcolor = "pink"          
                    )
    
    botao = ft.CupertinoButton("Download", on_click=baixar, bgcolor='blue', color='white', width = 250)
    
    campos = ft.Container(
        content = ft.Row(
            [link_music, botao],
            alignment = ft.MainAxisAlignment.CENTER 
        ),
        alignment = ft.alignment.center,
        #bgcolor = 'green',
        padding = 10
    )

    aviso_container = ft.Container(
        content = aviso,
        alignment = ft.alignment.center
    )
    
    def update_layout(width, campos):
        if page.width <= 600:
            campos.content = ft.Column(
                    [link_music, botao],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    
                    
                )

        else:
            campos.content = ft.Row(
                    [link_music, botao],
                    alignment = ft.MainAxisAlignment.CENTER,
                )
        page.update()
        
    
    page.on_resized = lambda e: update_layout(page.window.width, campos)
    update_layout(page.window.width, campos)
    
    page.add(
            intro_text   
        )
    
    page.add(
            campos    
        )

    page.add(
            aviso_container
        )    
    
ft.app(host='0.0.0.0', target=main)