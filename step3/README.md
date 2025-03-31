# 📊 Script SQL para Análise de Operadoras de Saúde

Este script SQL cria e estrutura um banco de dados para armazenar e analisar informações sobre operadoras de planos de saúde e suas demonstrações contábeis. Ele inclui a importação de dados de arquivos CSV e consultas analíticas para extrair insights relevantes.

---

## 📌 Pré-requisitos

Antes de executar o script, certifique-se de ter:
- **MySQL Server** instalado
- **Arquivos CSV** necessários disponíveis no sistema de arquivos
- **Permissão** para executar comandos `LOAD DATA LOCAL INFILE` no MySQL

---

## 🏗 Estrutura do Banco de Dados

O banco de dados é composto por duas tabelas principais:

### 📂 `operadoras`
- Armazena informações cadastrais das operadoras de saúde.
- **Principais campos:**
  - `registro_ans` (chave primária)
  - `cnpj`
  - `razao_social`
  - `nome_fantasia`
  - Dados de endereço e contato

### 💰 `demonstracoes_contabeis`
- Registra os dados financeiros das operadoras por período.
- **Principais campos:**
  - Dados financeiros com saldos iniciais e finais
  - Vincula-se à operadora através do `registro_ans`

---

## 🚀 Instruções de Execução

### 📂 1. Preparar os Arquivos CSV
- Certifique-se de que os arquivos CSV estão no sistema de arquivos.
- Os arquivos devem estar nos seguintes formatos:
  - `Relatorio_cadop.csv` → Dados cadastrais das operadoras
  - `XTYYYY.csv` → Dados contábeis (onde `X` é o trimestre e `YYYY` o ano)

### ✏ 2. Modificar o Script
- Substitua os **caminhos de arquivo** no script para refletir a localização real dos arquivos CSV no seu sistema. Nas linhas:
  - **35, 72, 103, 131, 159, 187, 215, 243, 271**

### 🖥 3. Executar o Script
1. Conecte-se ao **servidor MySQL**.
2. Execute o script completo ou por partes conforme necessário.

---

## 🔄 Processo de Importação

O script executa os seguintes passos:
✅ Criação das tabelas
✅ Importação dos dados cadastrais das operadoras
✅ Importação dos dados contábeis trimestrais (8 trimestres no total)
✅ Transformação de dados durante a importação:
   - Conversão de formatos de data
   - Ajuste de formatos numéricos (substituição de vírgulas por pontos)
   - Tratamento de valores nulos

---

## 📈 Consultas Analíticas

O script inclui consultas prontas para análise:

### 🔝 **Top 10 operadoras com maiores despesas no último trimestre de 2024**
- Filtra por eventos/sinistros de assistência à saúde.
- Ordena pelo valor total decrescente.

### 🔝 **Top 10 operadoras com maiores despesas no ano de 2024**
- Utiliza o mesmo critério de filtro, mas considerando todo o ano.

---

## ⚠ Observações Importantes

- O script assume que os arquivos CSV estão formatados corretamente com **delimitador `;`** e **encoding `latin1`**.
- O MySQL deve ter a opção `LOCAL_INFILE` habilitada para permitir a importação de arquivos CSV.
- Os caminhos dos arquivos **DEVEM** ser ajustados conforme a estrutura de diretórios do seu sistema.

---

🎯 **Agora, basta executar o script e analisar os dados!** 🚀

