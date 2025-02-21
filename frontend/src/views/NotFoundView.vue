<script setup lang="ts"></script>

<template>
  <main>
    <section
      class="bg-blue-400 min-h-svh pt-8 text-center flex flex-col items-center"
    >
      <i class="pi pi-exclamation-triangle text-yellow-500 text-7xl mb-5"></i>
      <h1 class="text-6xl font-bold mb-4">404 Not Found</h1>
      <p class="text-xl mb-5">
        This page does not exist or feature is in progress
      </p>
      <RouterLink
        to="/"
        class="text-white bg-blue-900 hover:bg-blue-950 rounded-md px-3 py-2 mt-4"
        >Go Back</RouterLink
      >
    </section>
  </main>
</template>
