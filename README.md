# Science Quiz

Este projeto consiste em um quiz de ciências que oferece perguntas sobre diferentes categorias. O jogo é executado em Python com a biblioteca Pygame e interage com um banco de dados para armazenar perguntas e respostas.

## Autor
Thiago Lima Silva de Souza - 

## Configuração do Banco de Dados

Para executar o jogo, é necessário configurar um banco de dados que armazene as perguntas e categorias. Certifique-se de ter um sistema de banco de dados instalado na sua máquina (MySQL, PostgreSQL, SQLite, etc.) e siga os passos abaixo:

1. **Execução do Banco de Dados:**
   - Consulte o arquivo `app.py` para verificar as configurações de conexão com o banco de dados.
   - Execute o script SQL fornecido no arquivo `create_tables.sql` para criar as tabelas e inserir dados iniciais, se aplicável.

### Funcionalidades

### Principais Arquivos
- **`src/__init__.py`:** Inicializa a aplicação Flask e configura o SQLAlchemy e Flask-Migrate.
- **`src/app.py`:** Inicia a aplicação Flask, define as rotas e importa os controllers e funcionalidades necessárias.
- **`src/config.py`:** Contém as configurações do banco de dados PostgreSQL e diferentes ambientes de configuração.
- **`src/game_init.py`:** Inicia o jogo chamando a função `show_main_screen()` do módulo `view`.

### Estrutura de Diretórios
- **`controllers/`:** Controladores para lidar com a lógica das rotas.
- **`entities/`:** Entidades do jogo, como perguntas e categorias.
- **`services/`:** Serviços para interações mais complexas entre os componentes.
- **`view/`:** Contém as telas e a lógica de apresentação do jogo.

## Executando o Projeto

### Pré-requisitos
- Python 3.x instalado
- PostgreSQL (ou outro banco de dados compatível) instalado e configurado
## Observações

Este projeto foi desenvolvido como parte de um desafio ou para fins de aprendizado, e pode ser expandido e modificado conforme necessário.
