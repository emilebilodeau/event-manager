<script setup lang="ts">
import { RouterLink, useRoute } from "vue-router";

const isActiveLink = (routePath: string) => {
  const route = useRoute();
  return route.path === routePath;
};
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/" :class="[isActiveLink('/') ? 'bg-gray-500' : '']"
        >Home</RouterLink
      >
      <RouterLink
        to="/events"
        :class="[isActiveLink('/events') ? 'bg-gray-500' : '']"
        >Events</RouterLink
      >
    </nav>
  </header>
</template>

<style></style>
