<template>
  <div class="quote">{{ quote }}</div>
</template>

<script setup>
import { ref } from "vue";

const defaultQuote = "The best way to predict the future is to create it.";
const quote = ref(defaultQuote);
</script>

<style scoped>
.quote {
  font-size: calc(2vw);
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  max-width: 90%;
  margin: 0 auto;
}
</style>
