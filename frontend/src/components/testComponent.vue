<script setup lang="ts">
import { ref } from "vue";

defineProps({
  title: {
    type: String,
    default: "Test",
  },
});
</script>

<template>
  <h1 class="text-2xl">{{ title }}</h1>
</template>
