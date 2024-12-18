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
      <DeleteButton @click="clearRecords" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, watch, onMounted, useTemplateRef } from "vue";
import RecordItem from "./RecordItem.vue";
import DeleteButton from "./DeleteButton.vue";

const records = ref([]);
const recordList = useTemplateRef("recordList");

const timediff = (now, last) => (last ? now.time - last.time : 0);

const removeRecord = (index) => records.value.splice(index, 1);

const scrollToBottom = () => {
  if (recordList.value)
    recordList.value.scrollTop = recordList.value.scrollHeight;
};

watch(records, () => {
  nextTick(scrollToBottom);
});

const clearRecords = () => {
  records.value = [];
};

onMounted(() => {
  scrollToBottom();
});

const addRecord = () => {
  records.value.push({ time: new Date(), note: "" });
  nextTick(scrollToBottom);
};
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
  scrollbar-width: none;
}

.records-list::-webkit-scrollbar {
  display: none;
}

.clear-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
