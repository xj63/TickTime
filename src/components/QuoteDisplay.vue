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
  font-size: 1.5em;
  margin-top: 1em;
  color: #666;
}
</style>
