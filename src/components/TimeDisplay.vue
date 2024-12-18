<template>
  <div class="time" :class="{ small }">{{ currentTimeFormatted }}</div>
</template>

<script setup>
defineProps({
  small: { type: Boolean, default: false },
});

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
  cursor: pointer;
  user-select: none;
  transition:
    font-size 0.5s ease-in-out,
    transform 0.5s ease-in-out;
}

@media (min-width: 1024px) {
  .time.small {
    font-size: calc(12vw);
  }
}
</style>
