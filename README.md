# PersonalBotDiscord 🤖

#### Bot criado para aprendizado e memes

## Enviroment and tools

- [Python3](https://www.python.org/)
- [Discord developer](https://discord.com/developers/applications)
- [Heroku](https://dashboard.heroku.com/apps)

## Steps to run and debug

* instalar os pacotes do python
    ~~~bash
        pip install -r requirements.txt
    ~~~
* (PARA RODAR LOCALMENTE) criar um arquivo com o nome `secret_keys.py` e, dentro dele, inserir a variável `TOKEN` com a string do token. Exemplo: 
    ~~~python
        TOKEN = 'codigo token'
    ~~~
    depois disso, executar o arquivo `main.py` normalmente
* o deploy automático só funciona na branch `main`. Para deploy de outras branchs, é necessário entrar no site do Heroku (após pull request) e realizar o deploy manualmente.
* para confirar o deploy no Herolu basta configurar o método de deploy, localizado na aba 'Deploy'. Depois, deve-se inserir as `Config Vars`, localizadas na aba 'Settings'. O nome da `Key` deve ser igual ao da variável no código.