# Busca de Operadoras

Este projeto é uma aplicação Vue.js para buscar operadoras de planos de saúde, utilizando uma API externa para retornar os dados e exibi-los em uma tabela interativa.

## 📌 Tecnologias Utilizadas
- Vue.js 3
- Vite
- Fetch API
- CSS (Scoped Styles)

---

## 📥 Como Instalar o Projeto

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Acesse a pasta do projeto:**
   ```sh
   cd nome-do-projeto
   ```

3. **Instale as dependências:**
   ```sh
   npm install
   ```

---

## 🚀 Como Rodar o Projeto

1. **Defina a URL da API no arquivo `.env`** (crie um arquivo `.env` na raiz se ele não existir):
   ```sh
   VITE_API_URL=https://sua-api.com
   ```

2. **Inicie o servidor de desenvolvimento:**
   ```sh
   npm run dev
   ```

3. **Acesse o projeto no navegador:**
   Normalmente disponível em `http://localhost:5173`.

---

## 📂 Estrutura do Projeto

```
📁 src/
 ├── 📁 components/      # Componentes reutilizáveis
 │    ├── SearchBar.vue  # Barra de pesquisa
 │    ├── DataTable.vue  # Tabela de exibição de resultados
 │    ├── Pagination.vue # Paginação dos resultados
 │
 ├── 📄 App.vue          # Componente principal
 ├── 📄 main.js          # Entrada da aplicação
 │
```

---

## 🛠 Funcionalidades

- **Buscar operadoras** digitando o nome na barra de pesquisa.
- **Exibir os resultados** em uma tabela organizada.
- **Ordenação** dos dados clicando nos cabeçalhos das colunas.
- **Paginação** para navegar entre os resultados.
- **Mensagens de erro** e estado de carregamento interativo.

---

## 📌 Comandos Úteis

- **Iniciar o servidor:**
  ```sh
  npm run dev
  ```
- **Compilar para produção:**
  ```sh
  npm run build
  ```
- **Executar preview da build:**
  ```sh
  npm run preview
  ```

---

## ⚠️ Possíveis Erros e Soluções

- **Erro:** `sh: vite: command not found`
  - **Solução:** Execute `npm install vite --save-dev` para instalar o Vite.

- **Erro:** `Cannot read properties of undefined (reading 'data')`
  - **Solução:** Verifique se a URL da API no `.env` está correta e se o backend está rodando.

- **Erro:** `Network Error` ou `CORS policy issue`
  - **Solução:** Confirme que o backend permite requisições da origem do frontend.

---
