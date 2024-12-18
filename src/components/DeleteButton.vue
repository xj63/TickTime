<template>
  <button class="delete-btn">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M6 18L18 6M6 6l12 12"
      />
    </svg>
  </button>
</template>

<script setup></script>

<style scoped>
.delete-btn {
  background-color: transparent;
  color: #999;
  border: none;
  border-radius: 50%;
  font-size: 1.5em;
  cursor: pointer;
  transition:
    color 0.2s,
    background-color 0.2s;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete-btn:hover {
  color: red;
  background-color: #ffecec;
}

.dark .delete-btn {
  color: #ccc;
}

.dark .delete-btn:hover {
  color: red;
  background-color: #333;
}

.icon {
  width: 1em;
  height: 1em;
}
</style>
