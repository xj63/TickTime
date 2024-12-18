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
import { ref, watchEffect, onMounted } from "vue";

const defaultQuote = "The best way to predict the future is to create it.";
const quote = ref("");

function isAtLeastOneWhitespaceOnly(str) {
  return str.length > 0 && /^\s+$/.test(str);
}

const deleteQuote = () => (quote.value = "");
const handleEnter = (event) => event.target.blur();
const updateQuote = (event) => {
  const text = event.target.innerText;
  quote.value = isAtLeastOneWhitespaceOnly(text)
    ? ""
    : text.trim() || defaultQuote;
};

const updateUrl = (newQuote) => {
  const queryParams = new URLSearchParams(window.location.search);
  queryParams.set("quote", newQuote);
  const path = window.location.pathname.replace(/\/$/, "");
  const para = queryParams.toString().replace(/=$/, "");
  const newUrl = `${path}?${para}`;
  window.history.replaceState({}, "", newUrl);
};

onMounted(() => {
  const queryParams = new URLSearchParams(window.location.search);
  if (queryParams.has("quote")) quote.value = queryParams.get("quote");
  else quote.value = defaultQuote;
  watchEffect(() => updateUrl(quote.value));
});
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
