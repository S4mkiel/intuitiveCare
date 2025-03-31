<template>
  <div class="search-container">
    <input
      v-model="localQuery"
      @keyup.enter="emitSearch"
      placeholder="Digite para buscar por nome..."
      class="search-input"
    />
    <button @click="emitSearch" class="search-button">Buscar</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      localQuery: ''
    }
  },
  methods: {
    emitSearch() {
      this.$emit('search', this.localQuery)
    }
  }
}
</script>

<style scoped>
.search-container {
  display: flex;
  gap: 0.5rem;
  max-width: 600px;
  margin: 0 auto;
  width: 100%;
}

.search-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid #dee2e6;
  border-radius: var(--border-radius);
  font-size: 1rem;
  transition: var(--transition);
  box-shadow: var(--box-shadow);
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(67, 97, 238, 0.2);
}

.search-button {
  padding: 0.75rem 1.5rem;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  font-weight: 500;
  box-shadow: var(--box-shadow);
}

.search-button:hover {
  background-color: var(--primary-hover);
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .search-container {
    flex-direction: column;
  }
  
  .search-button {
    width: 100%;
  }
}
</style>