<template>
  <div class="container">
    <header class="header">
      <h1>Busca de Operadoras</h1>
      <SearchBar @search="handleSearch" />
    </header>

    <main>
      <div v-if="loading" class="loading">Carregando...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else>
        <DataTable 
          :results="results" 
          :current-sort="sortBy" 
          :current-order="order" 
          @sort="handleSort"
          v-if="results.length > 0" 
        />
        <div v-else class="no-results">Nenhum resultado encontrado</div>
        <Pagination
          :current-page="currentPage"
          :total-pages="totalPages"
          @page-change="changePage"
          v-if="results.length > 0"
        />
      </div>
    </main>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import DataTable from './components/DataTable.vue'
import Pagination from './components/Pagination.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
    DataTable,
    Pagination
  },
  data() {
    return {
      searchQuery: '',
      results: [],
      loading: false,
      error: null,
      currentPage: 1,
      perPage: 10,
      totalPages: 1,
      sortBy: '',
      order: 'asc'
    }
  },
  created() {
    this.handleSearch('')
  },
  methods: {
    async handleSearch(query) {
      this.searchQuery = query
      this.loading = true
      this.error = null
      this.results = []
      
      try {
        const baseURL = import.meta.env.VITE_API_URL
        const url = `${baseURL}/api/search?q=${encodeURIComponent(this.searchQuery)}&page=${this.currentPage}&per_page=${this.perPage}${this.sortBy ? `&sort_by=${this.sortBy}&order=${this.order}` : ''}`
        
        const response = await fetch(url)
        
        if (!response.ok) {
          throw new Error(`Erro na busca: ${response.statusText}`)
        }
        
        const data = await response.json()
        console.log('Resposta da API (busca geral):', data)
        this.results = Array.isArray(data.data) ? data.data : []
        this.totalPages = data.meta?.total_pages || 1
      } catch (err) {
        this.error = 'Ocorreu um erro ao buscar os dados: ' + err.message
        console.error(err)
      } finally {
        this.loading = false
      }
    },
    handleSort(column) {
      if (this.sortBy === column) {
        if (this.order === 'asc') {
          this.order = 'desc'
        } else {
          this.sortBy = ''
          this.order = 'asc'
        }
      } else {
        this.sortBy = column
        this.order = 'asc'
      }
      this.currentPage = 1
      this.handleSearch(this.searchQuery)
    },
    changePage(newPage) {
      this.currentPage = newPage
      this.handleSearch(this.searchQuery)
    }
  }
}
</script>

