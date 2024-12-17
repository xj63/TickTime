<template>
  <div class="time">{{ currentTimeFormatted }}</div>
</template>

<script setup>
import { ref, computed } from "vue";

const currentTime = ref(new Date());

const currentTimeFormatted = computed(() => {
  return currentTime.value.toLocaleTimeString("en-US", {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
});

setInterval(() => {
  currentTime.value = new Date();
}, 1000);
</script>

<style scoped>
.time {
  font-family: "Courier New", "Lucida Console", "Monaco", "Consolas", monospace,
    "Helvetica", "Arial", sans-serif;
  font-size: calc(16vw);
  font-weight: bold;
  text-align: center;
  margin: 0 auto;
}
</style>
