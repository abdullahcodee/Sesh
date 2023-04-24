<template>
  <div class="loading-spinner" v-if="loading">
    <i class="fa fa-spinner fa-spin"></i> Loading...
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    convertVideo() {
      this.loading = true;
      // Perform video conversion logic here
      // After conversion is complete, set loading back to false
      setTimeout(() => {
        this.loading = false;
      }, 3000); // Set the timeout to the duration of the actual conversion process
    },
  },
};
</script>

<style scoped>
.loading-spinner {
  animation: spin 2s infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>




