<template>
  <div class="container">
    <main>
      <TimeDisplay @click="addTimeRecord" :small="RecordsNotEmpty" />
      <aside>
        <TimeRecords ref="records" v-show="RecordsNotEmpty" />
      </aside>
    </main>
    <footer>
      <QuoteDisplay />
    </footer>
  </div>
</template>

<script setup>
import { useTemplateRef, computed } from "vue";
import TimeRecords from "./components/TimeRecords.vue";
import TimeDisplay from "./components/TimeDisplay.vue";
import QuoteDisplay from "./components/QuoteDisplay.vue";

const childRecords = useTemplateRef("records");
const addTimeRecord = () => {
  if (childRecords.value) childRecords.value.addRecord();
};
const RecordsNotEmpty = computed(() =>
  childRecords.value ? !childRecords.value.isEmpty : false,
);
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  box-sizing: border-box;
}

main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
  flex-direction: column;
  width: 100%;
}

@media (min-width: 1024px) {
  main {
    flex-direction: row;
  }
}

aside {
  margin: 2em;
}

footer {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 1em;
  padding-bottom: 1em;
}
</style>
