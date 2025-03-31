<template>
  <div class="pagination">
    <button 
      :disabled="currentPage === 1" 
      @click="$emit('page-change', currentPage - 1)"
    >Anterior</button>
    <span>Página {{ currentPage }} de {{ totalPages }}</span>
    <button 
      :disabled="currentPage === totalPages" 
      @click="$emit('page-change', currentPage + 1)"
    >Próximo</button>
  </div>
</template>

<script>
export default {
  name: 'PaginationComponent',
  props: {
    currentPage: {
      type: Number,
      required: true
    },
    totalPages: {
      type: Number,
      required: true
    }
  }
}
</script>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}

.pagination button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: var(--border-radius);
  background-color: var(--primary-color);
  color: var(--white);
  cursor: pointer;
  transition: var(--transition);
  font-weight: 500;
}

.pagination button:hover:not(:disabled) {
  background-color: var(--primary-hover);
  transform: translateY(-1px);
}

.pagination button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  background-color: var(--text-light);
}

.pagination span {
  color: var(--text-light);
  font-size: 0.9rem;
}
</style>