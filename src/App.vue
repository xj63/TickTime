<template>
  <div class="container">
    <main>
      <TimeDisplay />
    </main>
    <footer>
      <QuoteDisplay />
    </footer>
  </div>
</template>

<script setup>
import TimeDisplay from "./components/TimeDisplay.vue";
import QuoteDisplay from "./components/QuoteDisplay.vue";
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
  width: 100%;
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
