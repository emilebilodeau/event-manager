<script setup lang="ts">
import { ref, defineProps } from "vue";

defineProps({
  title: {
    type: String,
    default: "Test",
  },
});
</script>

<template>
  <h1>{{ title }}</h1>
</template>
