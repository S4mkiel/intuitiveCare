# 📌 Teste de API

## 📖 Sobre o Projeto
Este projeto é uma API desenvolvida em Python utilizando Flask, Poetry e arquitetura **Ports and Adapters**. A API permite buscar e consultar operadoras de planos de saúde a partir de um arquivo CSV. 

---ç

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Flask
- Pandas
- Poetry
- Flask-CORS
- Dotenv
- Colorama

---

## 📦 Instalação

### 🔹 1. Instalar o Poetry (caso não tenha)

### **Windows**
1. Abra o PowerShell como Administrador e execute:
   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
   ```
2. Adicione o Poetry ao PATH (se necessário):
   ```powershell
   $env:PATH += ";$env:APPDATA\Python\Scripts"
   ```
3. Verifique a instalação:
   ```sh
   poetry --version
   ```

### **macOS**
1. Execute o comando:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```
2. Adicione ao PATH (caso necessário):
    ```sh
    export PATH="$HOME/.local/bin:$PATH"
    ```
3. Verifique a instalação:
    ```sh
    poetry --version
    ```

#### **Alternativa com Homebrew**
1. Instale o Poetry utilizando o Homebrew:
    ```sh
    brew install poetry
    ```
2. Verifique a instalação:
    ```sh
    poetry --version
    ```

### **Linux**
1. Execute o comando:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Adicione ao PATH (se necessário):
   ```sh
   export PATH="$HOME/.local/bin:$PATH"
   ```
3. Verifique a instalação:
   ```sh
   poetry --version
   ```

### 🔹 3. Instalar as Dependências
```bash
$ poetry install
```

---

## ⚙️ Configuração

Antes de rodar a aplicação, configure o arquivo **.env** com as variáveis de ambiente necessárias:

```ini
# Configurações do CSV
CSV_FILE_PATH=Relatorio_cadop.csv
CSV_SEPARATOR=;
CSV_ENCODING=utf-8

# Configuração do Servidor
APP_PORT=3000
APP_HOST=0.0.0.0
APP_DEBUG=True
CORS_ENABLED=True
```

Caso precise modificar o caminho do CSV, edite o valor da variável `CSV_FILE_PATH`.

---

## ▶️ Execução

### 🔹 1. Ativar o Ambiente Virtual
```bash
$ poetry shell
```

### 🔹 2. Rodar a API
```bash
$ python main.py
```

Por padrão, a API será iniciada em **http://0.0.0.0:3000**.

---

## 🔍 Endpoints Disponíveis

### 🔹 Buscar Operadoras
```http
GET /api/search?q={termo}&page={número}&per_page={quantidade}
```
📌 **Exemplo:** `GET /api/search?q=saude&page=1&per_page=5`

🔹 **Parâmetros:**
- `q` → Termo de busca (obrigatório)
- `page` → Número da página (padrão: 1)
- `per_page` → Quantidade de itens por página (padrão: 10)

🔹 **Resposta:**
```json
{
  "data": [
    {
      "Registro_ANS": "123456",
      "CNPJ": "12.345.678/0001-90",
      "Razao_Social": "Saúde Total LTDA",
      "Nome_Fantasia": "Saúde Total",
      ...
    }
  ],
  "meta": {
    "total": 50,
    "page": 1,
    "per_page": 5,
    "total_pages": 10
  }
}
```

---

### 🔹 Buscar Operadora por Registro ANS
```http
GET /api/operators/{registro_ans}
```
📌 **Exemplo:** `GET /api/operators/123456`

🔹 **Resposta:**
```json
{
  "data": {
    "Registro_ANS": "123456",
    "CNPJ": "12.345.678/0001-90",
    "Razao_Social": "Saúde Total LTDA",
    "Nome_Fantasia": "Saúde Total",
    ...
  }
}
```

---

## 🛠 Estrutura do Projeto

```
📂 step4/
├── 📂 domain/              # Modelos de domínio
├── 📂 ports/               # Interfaces e abstrações
├── 📂 adapters/            # Implementações concretas (Repository, Controller)
├── 📂 use_cases/           # Casos de uso
├── 📂 utils/               # Ferramentas auxiliares (Logger, etc.)
├── .env                   # Configuração de variáveis de ambiente
├── pyproject.toml         # Configuração do Poetry
├── main.py                # Inicialização da aplicação
└── README.md              # Documentação do projeto
```



