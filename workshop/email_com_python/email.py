"""
1 - Criar nova conta somente para o envio de email com python;
2 - Ativar verificação de duas etapas e criar chave de segurança;
3 - Seguir orientação do Notion;
LINK: https://overjoyed-track-d88.notion.site/Envio-de-e-mails-com-Python-269537d0cec3482dac06fa8d373851d2
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# port para criar o serve 'SMTP'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# email e chave de acesso
smtp_username = 'enviaremailpython8@gmail.com'
smtp_password = 'sobr atpn utqt tlzo'

# criando e iniciando o serve
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# fazer login com a chave de acesso
server.login(smtp_username, smtp_password)

# criando a estrutura do email
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'gabrielsantos031bh@gmail.com'
msg['Subject'] = 'Assunto do e-mail'

# criando o email com a estrutura definida
body = 'Este é um e-mail enviado via Python!'
msg.attach(MIMEText(body, 'plain'))

# enviando o email atravez do sertv
server.sendmail(smtp_username, 'gabrielsantos031bh@gmail.com', msg.as_string())

# fechando o serve
server.quit()

print('E-mail enviado com sucesso!')
