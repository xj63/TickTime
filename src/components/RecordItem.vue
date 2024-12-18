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
  const hours = String(Math.floor(props.diff / 3600)).padStart(2, '0');
  const minutes = String(Math.floor((props.diff % 3600) / 60)).padStart(2, '0');
  const seconds = String(props.diff % 60).padStart(2, '0');
  return props.diff > 0 ? `+${hours}:${minutes}:${seconds}` : "";
});
</script>

<style scoped>
.record-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5em;
  margin-bottom: 0.5em;
}

.time {
  font-weight: bold;
  color: #333;
  margin-right: 1em;
}

.diff {
  color: green;
  font-size: 0.8em;
  width: 60px;
  text-align: right;
  margin-right: 2em;
}

.note-input {
  flex: 1;
  font-size: 0.8em;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
  margin-right: 1em;
  cursor: text;
  border: 1px solid transparent;
  background-color: transparent;
}

.note-input:focus {
  outline: none;
  border: 1px solid #007bff;
  background-color: #fff;
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

html.dark .note-input:focus {
  border: 1px solid #555;
  background-color: #444;
}
</style>
