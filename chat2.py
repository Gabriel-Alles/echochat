# Para criar um sistema / aplicativo ou site você tem que pensar o que eu quero ter nele e pensar no que quer que o usuário veja quando entrar:


# Criar o EchoChat

# Titulo: EchoChat
# Botão: Iniciar Chat
    # quando eu clicar no botão:
    # Janela nomes que podem ser janela / Dialog / Modal / Popup
        # Titulo: Bem vindo ao EchoChat
        # Campo de texto : Escreva seu nome no chat
        # Botão: Entrar no chat
            # Clicou no botão:
            # Fechar o Dialog:  
                # Criar o chat
                # Criar o campo de mensagem: Digite sua mensagem 
                # Botão: Enviar     
                   # Quando clicar no botão:
                   # Envie a mensagme para o chat

# importar o flet

# importar o flet

import flet as ft

# criar a função principal (main) do seu aplicativo

def main(pagina):
    # criar os elementos
    titulo = ft.Text('EchoChat')

    titulo_janela = ft.Text('Bem vindo ao EchoChat')  

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # websocket -> tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = f'{campo_nome.value}: {campo_mensagem.value}'
        # enviar mensagem no tunel
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label='Escreva sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.pubsub.send_all(f'{campo_nome.value} entrou no chat')
        # fechar a janela / dialog
        janela.open = False
        pagina.update()
        # tirar o titulo
        pagina.remove(titulo)
        # tirar o botao iniciar
        pagina.remove(botao_iniciar)
        pagina.update()

        # criar o chat
        pagina.add(chat)
        # criar o campo digite sua mensagem
        # botão enviar
        pagina.add(linha_mensagem)
        pagina.update()

    campo_nome = ft.TextField(label='Digite o seu nome', on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)



    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome, actions=[botao_entrar])

    def abrir_dialog(evento):
        pagina.dialog = janela
        pagina.open(janela)
        pagina.update()



    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_dialog)


    # colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)



# rodar o seu aplicativo
ft.app(main, view=ft.WEB_BROWSER)

# sempre que você clica em qualquer botão -> o flet ele cria um evento do clique ou seja algo que o usuário fez algo na tela
