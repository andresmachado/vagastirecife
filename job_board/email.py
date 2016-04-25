from django.core.mail import EmailMessage

subject, from_email, to = 'Alerta de nova mensagem.', 'contato@vagastirecife.com.br', 'csantos.machado@gmail.com'
text_content = 'Uma nova vaga foi anunciada, para revisar e publicar visite o site.'

alert_mail = EmailMessage(subject, text_content, from_email, [to])