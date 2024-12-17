<template>
  <div class="time">{{ currentTime }}</div>
</template>

<script setup>
import { ref } from "vue";

const currentTime = ref(new Date().toLocaleTimeString());

setInterval(() => {
  currentTime.value = new Date().toLocaleTimeString();
}, 1000);
</script>

<style scoped>
.time {
  font-size: 5em;
  font-weight: bold;
}
</style>
