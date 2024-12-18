<template>
  <li class="record-item">
    <span class="time">{{ timeFormat }}</span>
    <span class="diff" v-if="props.diff > 0">{{ diffFormat }}</span>
    <span class="diff" v-else>&nbsp;</span>
    <input
      v-model="note"
      class="note-input"
      placeholder="Add a note"
      :contenteditable="true"
      @input="$emit('update-note', note)"
    />
    <DeleteButton @click="$emit('remove')" />
  </li>
</template>

<script setup>
import { ref, computed } from "vue";
import DeleteButton from "./DeleteButton.vue";

const props = defineProps({
  time: Date,
  diff: Number,
  note: String,
});

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
  if (props.diff <= 0) return "";
  const diff = props.diff / 1000;
  const hours = String(Math.floor(diff / 3600)).padStart(2, "0");
  const minutes = String(Math.floor((diff % 3600) / 60)).padStart(2, "0");
  const seconds = String(diff % 60).padStart(2, "0");
  return `+${hours}:${minutes}:${seconds}`;
});
</script>

<style scoped>
.record-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.4em;
}

.time {
  font-weight: bold;
  color: #333;
  margin-right: 0.4em;
}

.diff {
  color: green;
  font-size: 0.8em;
  text-align: right;
  margin-right: 0.8em;
  min-width: 5em;
}

.note-input {
  flex: 1 1 auto;
  font-size: 0.8em;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  cursor: text;
  border: 0px solid transparent;
  background-color: transparent;
}

@media (max-width: 360px) {
  .note-input {
    max-width: 30vw;
  }
}

@media (max-width: 280px) {
  .note-input {
    max-width: 20vw;
  }
}

@media (max-width: 240px) {
  .note-input {
    display: none;
  }
}

@media (max-width: 190px) {
  .diff {
    display: none;
  }
}

@media (max-width: 110px) {
  .time {
    font-size: calc(12vw);
  }

  .delete-btn {
    display: none;
  }
}

.note-input:focus {
  outline: none;
}

.note-input::placeholder {
  color: transparent;
}

.delete-btn {
  flex: 0 0 auto;
}

html.dark .time {
  color: #ddd;
}

html.dark .diff {
  color: lightgreen;
}

html.dark .note-input {
  color: #ddd;
  background-color: transparent;
}
</style>
