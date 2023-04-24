# Plano Nutricional AI

Este projeto utiliza a API GPT-3 da OpenAI para gerar planos nutricionais personalizados, levando em consideração as informações pessoais do usuário e seus objetivos específicos. O objetivo principal é fornecer opções de refeições e substituições para atender às necessidades nutricionais individuais de cada pessoa, levando em conta possíveis restrições alimentares.

## Requisitos

- Python 3.6 ou superior
- Flask
- Flask-Mail
- OpenAI
- python-dotenv

## Informações

Este projeto ainda está em andamento e eu ainda estou buscando uma maneira de padronizar os resultados da API de acordo com as especificações definidas no prompt. Infelizmente, às vezes, o retorno da API vem fora do padrão desejado. Embora a aparência do projeto ainda não seja a melhor, não foi o foco principal neste momento. Qualquer contribuição para melhorar o projeto será muito bem-vinda.

## Instalação

1. Clone este repositório:
`
git clone https://github.com/seu_usuario/Plano-Nutricional-AI.git
`
2. Navegue até o diretório do projeto:
`
cd Plano-Nutricional-AI
`
3. Crie um ambiente virtual (recomendado):
`
python -m venv venv
`
4. Ative o ambiente virtual:
- No Windows:
  ```
  .\venv\Scripts\activate
  ```
- No Linux ou macOS:
  ```
  source venv/bin/activate
  ```
5. Instale as dependências necessárias:
`
pip install -r requirements.txt
`
6. Edite o arquivo arquivo `.env` na raiz do projeto e adicione suas credenciais da API da OpenAI e informações de e-mail, conforme o exemplo abaixo:
```
OPENAI_API_KEY=sua_chave_da_api_openai
MAIL_USERNAME=seu_email_outlook
MAIL_PASSWORD=sua_senha_de_email_outlook
```

## Execução

1. Inicie o servidor
`
app.py
`
2. Acesse a aplicação em seu navegador usando o endereço `http://localhost:5000`

## Uso

1. Preencha o formulário com suas informações pessoais e objetivo nutricional.
2. Aceite os termos de uso e clique em "Enviar".
3. O plano nutricional personalizado será gerado e enviado para o endereço de e-mail fornecido.

## Aviso

Este projeto é apenas para fins educacionais e não substitui o aconselhamento de um profissional nutricionista. Consulte sempre um profissional de saúde antes de adotar qualquer plano nutricional.

