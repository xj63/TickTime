<template>
  <div
    class="quote"
    contenteditable="true"
    @click="deleteQuote"
    @blur="updateQuote"
    @keydown.enter.prevent="handleEnter"
  >
    {{ quote }}
  </div>
</template>

<script setup>
import { ref } from "vue";

const defaultQuote = "The best way to predict the future is to create it.";
const quote = ref(defaultQuote);

const deleteQuote = () => (quote.value = "");
const updateQuote = (event) => {
  quote.value = event.target.innerText.trim() || defaultQuote;
};

const handleEnter = (event) => event.target.blur();
</script>

<style scoped>
.quote {
  font-size: calc(2vw);
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
  max-width: 90%;
  margin: 0 auto;
  cursor: text;
  border: 1px solid transparent;
}

.quote[contenteditable="true"]:focus {
  outline: none;
}
</style>
