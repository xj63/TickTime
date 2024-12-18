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

const quote = ref("");

const quotes = [
  "The best way to predict the future is to create it.",
  "The only way to do great work is to love what you do.",
  "Life is 10% what happens to us and 90% how we react to it.",
  "The only limit to our realization of tomorrow is our doubts of today.",
  "The purpose of our lives is to be happy.",
  "Get busy living or get busy dying.",
];

const randomQuote = () => quotes[Math.floor(Math.random() * quotes.length)];
async function fetchQuotes() {
  try {
    const response = await fetch("/quotes.txt");
    const text = await response.text();
    const newQuotes = text
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line.length > 0);
    quotes.push(...newQuotes);
  } catch (error) {
    console.error("Error fetching quotes:", error);
  }
}
fetchQuotes();

function isAtLeastOneWhitespaceOnly(str) {
  return str.length > 0 && /^\s+$/.test(str);
}

const deleteQuote = () => (quote.value = "");
const handleEnter = (event) => event.target.blur();
const updateQuote = (event) => {
  const text = event.target.innerText;
  quote.value = isAtLeastOneWhitespaceOnly(text)
    ? ""
    : text.trim() || randomQuote();
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
  else quote.value = randomQuote();
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
