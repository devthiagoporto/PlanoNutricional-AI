# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, jsonify
from flask_mail import Mail, Message
import openai
from model import Pessoa
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure a API GPT-3
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Configure o Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.office365.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    primeiro_nome = request.form.get('inputPrimeiroNome')
    segundo_nome =  request.form.get('inputSegundoNome')
    peso = request.form.get('inputPeso')
    altura = request.form.get('inputAltura')
    dt_nascimento = request.form.get('inputDtNascimento')
    objetivo = request.form.get('inputObjetivo')
    email = request.form.get('inputEmail')
    checkbox_value = request.form.get('flexCheckDefault')
    pessoa = Pessoa(primeiro_nome,segundo_nome,peso,altura,dt_nascimento,objetivo,email)

    if checkbox_value == 'on':
        refeicoes = ['Café da manhã','Lanche da manhã' ,'Almoço', 'Lanche da tarde','Jantar', 'Lanche da noite']
        respostas_gpt3 = []

        for refeicao in refeicoes:
            prompt = criar_prompt(refeicao, pessoa)
            resposta_gpt3 = gerar_resposta_gpt3(prompt)
            respostas_gpt3.append(f"#### {refeicao}\n\n{resposta_gpt3}\n\n")

        resposta_final = f"## Plano nutricional para {pessoa.primeiro_nome} {pessoa.segundo_nome}\n\n### Objetivo: {pessoa.objetivo}\n\nPeso: {pessoa.peso} kg\n\nAltura: {pessoa.altura} cm\n\nNascimento: {pessoa.dt_nascimento}\n\n" + ''.join(respostas_gpt3)
        
        msg = Message("Plano Nutricional", sender=os.environ.get('MAIL_USERNAME'), recipients=[email])
        msg.body = resposta_final
        mail.send(msg)

        return jsonify({"status": "success", "message": "E-mail enviado com sucesso!"})
    else:
        return jsonify({"status": "error", "message": "É necessário aceitar os termos de uso!"})

def gerar_resposta_gpt3(texto_prompt):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texto_prompt,
        max_tokens=1600,  # Diminua a quantidade de tokens para tornar a resposta mais focada e coerente
        n=1,
        stop=None,
        temperature=0.8,  # Diminua a temperatura para tornar a resposta mais focada e coerente
    )

    print("Resposta GPT-3:", response)

    resposta = response.choices[0].text.strip()
    return resposta

def criar_prompt(titulo, pessoa):
    return (f"Como um assistente de inteligência artificial, crie opções de refeições para o {titulo} de alguém que tem como objetivo {pessoa.objetivo}. "
            f"Considere que a pessoa pesa {pessoa.peso} kg, tem {pessoa.altura} cm de altura e nasceu em {pessoa.dt_nascimento}. "
            f"Liste opções de proteínas, gorduras e carboidratos separadas por vírgulas, juntamente com suas respectivas quantidades em gramas para a refeição. "
            f"Inclua opções de refeições e substituições para acomodar possíveis restrições alimentares. "
            f"Siga o formato:\n\n"
            f"Refeição\n\n"
            f"Carboidratos (escolha um): OPÇÃO(GRAMA), OPÇÃO(GRAMA)...\n\n"
            f"Proteina (escolha uma): OPÇÃO(GRAMA), OPÇÃO(GRAMA)...\n\n"
            f"Gordura (escolha uma): OPÇÃO(GRAMA), OPÇÃO(GRAMA). "
            f"Podem ser usadas unidades de medida como ML ou GRAMA, retornando exatamente no formato informado.\n\n"
            )

if __name__ == '__main__':
    app.run(debug=True)
