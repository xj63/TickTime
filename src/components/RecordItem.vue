<template>
  <li class="record-item">
    <span>{{ timeFormat }}</span>
    <span>{{ diffFormat }}</span>
    <input v-model="note" />
    <button @click="$emit('remove')">Delete</button>
  </li>
</template>

<script setup>
const props = defineProps({
  time: Date,
  diff: Number,
  note: String,
});

import { ref, computed } from "vue";

const note = ref(props.note);

const timeFormat = computed(() => {
  return props.time.toLocaleTimeString("en-US", {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
});

const diffFormat = computed(() => {
  return props.diff > 0 ? `+${props.diff}` : "";
});
</script>

<style scoped></style>
