<template>
  <div class="time-records">
    <ul class="records-list" ref="recordList">
      <RecordItem
        v-for="(record, index) in records"
        :key="record.time"
        :time="record.time"
        :diff="timediff(record, records[index - 1])"
        :note="record.note"
        @remove="removeRecord(index)"
      />
    </ul>
    <div class="clear-button-container">
      <DeleteButton @click="records = []" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import RecordItem from "./RecordItem.vue";
import DeleteButton from "./DeleteButton.vue";

const records = ref([]);

const timediff = (now, last) => (last ? now.time - last.time : 0);

const removeRecord = (index) => records.value.splice(index, 1);

const addRecord = () => records.value.push({ time: new Date(), note: "" });
const isEmpty = computed(() => records.value.length === 0);

defineExpose({ addRecord, isEmpty });
</script>

<style scoped>
.time-records {
  text-align: center;
  margin: 2em;
  max-width: 600px;
}

.records-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  max-height: 40vh;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.records-list::-webkit-scrollbar {
  width: 0px;
  background: transparent;
}

.records-list::-webkit-scrollbar-track {
  background: transparent;
}

.records-list::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.records-list {
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.3) transparent;
}

.clear-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
