<script setup lang="ts">
defineProps({
  title: String,
  defaultExample: {
    type: String,
    default: "Default string",
  },
});
</script>

<template>
  <h1 class="text-2xl">{{ title }}</h1>
  <p>{{ defaultExample }}</p>
</template>
