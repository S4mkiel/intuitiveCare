# README - Teste de Nivelamento (Steps 1 & 2)

Este repositório contém a implementação dos Steps 1 e 2 do teste de nivelamento, incluindo Web Scraping para baixar e compactar PDFs e a extração de dados de tabelas em arquivos CSV.

## 📌 Pré-requisitos

- Python 3.8+
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

## **Instalação do Poetry**
Para gerenciar dependências, utilizei o Poetry. Siga as instruções abaixo para instalá-lo no seu sistema operacional.

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

---

## **Instalação das Dependências**
```

## 📂 Estrutura do Projeto
```
📁 step1&2
│-- 📂 adapters
│   │-- pdf_downloader.py  # Código para baixar PDFs
│   │-- pdf_parser.py      # Código para extrair dados de tabelas em PDFs
│   │-- zip_handler.py     # Código para compactar arquivos
│-- 📂 ports
│   │-- pdf_downloader_port.py  # Interface para download de PDFs
│   │-- pdf_parser_port.py      # Interface para extração de dados de tabelas em PDFs
│   │-- zip_handler_port.py     # Interface para compactação de arquivos
│-- 📂 use_cases
│   │-- download_and_zip.py               # Use Case para Web Scraping
│   │-- download_extract_transform.py     # Use Case para extração de dados
│-- poetry.lock     # Gerenciamento de dependências
│-- pyproject.toml  # Configuração do Poetry
│-- main.py         # Script principal
```

## 🔧 Instalação das Dependências
Dentro do diretório do projeto, execute:

```
```bash
poetry shell
```

```bash
poetry install
```

## 🚀 Como Executar os Scripts

### Navegue até o diretório do projeto:
```bash
cd step1&2
```

### Step 1: Web Scraping (Baixar e Compactar PDFs)
```bash
python main.py
```
O script irá:
1. Acessar o site da ANS e buscar os links para os PDFs.
2. Baixar os arquivos Anexo I e Anexo II.
3. Armazenar os PDFs na pasta `outputs/step_1`.
4. Compactar os PDFs em `anexos.zip`.
5. Ler o arquivo `Anexo I.pdf` e extrair os dados das tabelas.
6. Salvar os dados estruturados em um arquivo CSV na pasta `output/step_2`.
7. Compactar o CSV em um arquivo ZIP denominado `Teste_Roberto_Barreto_Ferraz_Filho.zip`.

## 📌 Observações
- Certifique-se de que os PDFs foram baixados corretamente antes de rodar o Step 2.
- O script de extração pode levar alguns minutos dependendo do tamanho do PDF.