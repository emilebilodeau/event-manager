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
      <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="flex h-20 items-center justify-between">
          <div
            class="flex flex-1 items-center justify-center md:items-stretch md:justify-start"
          >
            <div class="md:ml-auto">
              <div class="flex space-x-2">
                <RouterLink
                  to="/"
                  :class="[
                    isActiveLink('/') ? 'bg-blue-900' : '',
                    'hover:bg-gray-900',
                    'text-white',
                    'px-3',
                    'py-2',
                    'rounded-md',
                  ]"
                  >Home</RouterLink
                >
                <RouterLink
                  to="/events"
                  :class="[
                    isActiveLink('/events') ? 'bg-blue-900' : '',
                    'hover:bg-gray-900',
                    'text-white',
                    'px-3',
                    'py-2',
                    'rounded-md',
                  ]"
                  >Events</RouterLink
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<style></style>
