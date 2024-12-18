<template>
  <div class="time-records">
    <ul class="records-list" ref="recordList">
      <RecordItem v-for="(record, index) in records" :key="record.time" :time="record.time"
        :diff="timediff(record, records[index - 1])" :note="record.note" @remove="removeRecord(index)"
        @update-note="updateRecordNote(index, $event)" />
    </ul>
    <div class="clear-button-container">
      <DeleteButton @click="clearRecords" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, watch, onMounted } from "vue";
import RecordItem from "./RecordItem.vue";
import DeleteButton from "./DeleteButton.vue";

const records = ref([]);
const recordList = ref(null);

const timediff = (now, last) => (last ? now.time - last.time : 0);

const scrollToBottom = () => {
  if (recordList.value) {
    recordList.value.scrollTop = recordList.value.scrollHeight;
  }
};

const formatRecord = (record) => {
  const timeString =
    record.time.toISOString().split(".")[0].replace(/:/g, ".") + "Z";
  return record.note ? `${timeString}_${record.note}` : `${timeString}`;
};

const parseRecord = (recordStr) => {
  const [timeString, ...noteParts] = recordStr.split("_");
  try {
    const time = new Date(timeString.replace(/\./g, ":"));
    if (isNaN(time.getTime())) throw new Error("Invalid date");
    return { time, note: noteParts.join("") || "" };
  } catch {
    return null;
  }
};

const updateUrl = () => {
  const queryParams = new URLSearchParams(window.location.search);
  const formattedRecords = records.value.map(formatRecord).join("|");
  if (records.value.length === 0) queryParams.delete("records");
  else queryParams.set("records", formattedRecords);
  const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
  window.history.replaceState({}, "", newUrl);
};

const initializeRecordsFromUrl = () => {
  const queryParams = new URLSearchParams(window.location.search);
  if (queryParams.has("records")) {
    const recordsStr = queryParams.get("records");
    try {
      const parsedRecords = recordsStr
        .split("|")
        .map(parseRecord)
        .filter((record) => record !== null);
      if (parsedRecords.length > 0) {
        records.value = parsedRecords;
      } else {
        records.value = [];
        queryParams.delete("records");
        const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
        console.log(newUrl);
        window.history.replaceState({}, "", newUrl);
      }
    } catch (error) {
      console.error("Failed to parse records from URL:", error);
      records.value = [];
      queryParams.delete("records");
      const newUrl = `${window.location.pathname}?${queryParams.toString()}`;
      console.log(newUrl);
      window.history.replaceState({}, "", newUrl);
    }
  }
};

const removeRecord = (index) => {
  records.value.splice(index, 1);
  updateUrl()
};

const updateRecordNote = (index, newNote) => {
  records.value[index].note = newNote;
  updateUrl();
};

watch(records, () => {
  nextTick(scrollToBottom);
  updateUrl();
});

const clearRecords = () => {
  records.value = [];
  updateUrl();
};

onMounted(() => {
  initializeRecordsFromUrl();
  scrollToBottom();
});

const addRecord = () => {
  records.value.push({ time: new Date(), note: "" });
  nextTick(scrollToBottom);
  updateUrl();
};

const isEmpty = computed(() => records.value.length === 0);

defineExpose({ addRecord, isEmpty });
</script>

<style scoped>
.time-records {
  text-align: center;
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

@media (max-width: 360px) {
  .time-records {
    max-width: 100%;
  }
}

@media (max-height: 576px) {
  .records-list {
    max-height: 35vh;
  }

  .clear-button-container {
    margin-top: 0px;
  }
}

@media (max-height: 140px) {
  .clear-button-container {
    display: none;
  }
}
</style>
