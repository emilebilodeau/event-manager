<script setup lang="ts">
import { RouterLink, useRoute } from "vue-router";

const isActiveLink = (routePath: string) => {
  const route = useRoute();
  return route.path === routePath;
};
</script>

<template>
  <header>
    <nav class="bg-blue-700 border-b border-blue-500">
      <div
        class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8 flex h-20 items-center justify-between"
      >
        <div class="flex space-x-2 ml-auto">
          <RouterLink
            to="/"
            :class="[isActiveLink('/') ? 'bg-blue-900' : '', 'link-element']"
            >Home</RouterLink
          >
          <RouterLink
            to="/events"
            :class="[
              isActiveLink('/events') ? 'bg-blue-900' : '',
              'link-element',
            ]"
            >Events</RouterLink
          >
        </div>
      </div>
    </nav>
  </header>
</template>

<style lang="css">
.link-element {
  @apply hover:bg-gray-900 text-white px-3 py-2 rounded-md;
}
</style>
