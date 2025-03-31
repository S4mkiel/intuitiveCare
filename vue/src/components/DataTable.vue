<template>
  <div class="table-responsive-container">
    <table class="enhanced-data-table">
      <thead>
        <tr>
          <th v-for="column in columns" :key="column.key" 
              @click="$emit('sort', column.key)"
              :class="{ 'active-sort': currentSort === column.key }">
            <div class="column-header">
              <span>{{ column.label }}</span>
              <span class="sort-indicator" v-if="currentSort === column.key">
                <svg :class="currentOrder" width="12" height="12" viewBox="0 0 24 24">
                  <path d="M7 10l5 5 5-5z" />
                </svg>
              </span>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in results" :key="item.Registro_ANS + index">
          <td v-for="column in columns" :key="column.key" :title="item[column.key]">
            {{ item[column.key] || '-' }}
          </td>
        </tr>
        <tr v-if="results.length === 0">
          <td :colspan="columns.length" class="no-results">
            Nenhum resultado encontrado
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'EnhancedDataTable',
  props: {
    results: {
      type: Array,
      required: true,
      default: () => []
    },
    currentSort: {
      type: String,
      default: ''
    },
    currentOrder: {
      type: String,
      default: 'asc'
    }
  },
  data() {
    return {
      columns: [
        { key: 'Registro_ANS', label: 'Registro ANS' },
        { key: 'Razao_Social', label: 'Razão Social' },
        { key: 'Nome_Fantasia', label: 'Nome Fantasia' },
        { key: 'CNPJ', label: 'CNPJ' },
        { key: 'Modalidade', label: 'Modalidade' },
        { key: 'Logradouro', label: 'Logradouro' },
        { key: 'Numero', label: 'Número' },
        { key: 'Complemento', label: 'Complemento' },
        { key: 'Bairro', label: 'Bairro' },
        { key: 'Cidade', label: 'Cidade' },
        { key: 'UF', label: 'UF' },
        { key: 'CEP', label: 'CEP' },
        { key: 'DDD', label: 'DDD' },
        { key: 'Telefone', label: 'Telefone' },
        { key: 'Fax', label: 'Fax' },
        { key: 'Endereco_eletronico', label: 'Endereço Eletrônico' },
        { key: 'Representante', label: 'Representante' },
        { key: 'Cargo_Representante', label: 'Cargo Representante' },
        { key: 'Data_Registro_ANS', label: 'Data Registro ANS' }
      ],
      scrollPosition: 0
    }
  },
  methods: {
    handleSort(column) {
      this.scrollPosition = this.$refs.tableContainer.scrollLeft
      
      this.$emit('sort', column)
      
      this.$nextTick(() => {
        this.$refs.tableContainer.scrollLeft = this.scrollPosition
      })
    }
  },
  watch: {
    results() {
      this.$nextTick(() => {
        this.$refs.tableContainer.scrollLeft = this.scrollPosition
      })
    }
  },
}
</script>

<style scoped>
.table-responsive-container {
  overflow-x: auto;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  margin: 2rem 0;
  background: var(--white);
  position: relative;
}

.enhanced-data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 0.95rem;
  min-width: 1200px;
}

.enhanced-data-table th {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
  position: sticky;
  top: 0;
  transition: var(--transition);
}

.enhanced-data-table th:hover {
  background-color: var(--primary-hover);
}

.enhanced-data-table th.active-sort {
  background-color: var(--secondary-color);
}

.column-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sort-indicator {
  display: inline-flex;
  margin-left: 8px;
}

.sort-indicator svg {
  fill: white;
  transition: transform 0.2s;
}

.sort-indicator svg.asc {
  transform: rotate(0deg);
}

.sort-indicator svg.desc {
  transform: rotate(180deg);
}

.enhanced-data-table td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #e9ecef;
  color: var(--text-color);
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.enhanced-data-table tr:last-child td {
  border-bottom: none;
}

.enhanced-data-table tr:nth-child(even) {
  background-color: rgba(0, 0, 0, 0.02);
}

.enhanced-data-table tr:hover {
  background-color: rgba(67, 97, 238, 0.05);
}

.no-results {
  text-align: center;
  padding: 20px;
  color: var(--text-light);
  font-style: italic;
}

.table-responsive-container::-webkit-scrollbar {
  height: 8px;
}

.table-responsive-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 0 0 10px 10px;
}

.table-responsive-container::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}

.table-responsive-container::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

@media (prefers-color-scheme: dark) {
  .enhanced-data-table {
    background-color: var(--white);
  }
  
  .enhanced-data-table td {
    color: var(--text-color);
    border-bottom-color: #495057;
  }
  
  .enhanced-data-table tr:nth-child(even) {
    background-color: #2b3035;
  }
}
</style>