<script setup lange="ts"></script>

<template>
  <section class="bg-blue-300 py-20 min-h-svh">
    <div class="container-xl lg:container lg:max-w-7xl m-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg">
        <!-- card 1 -->
        <div class="p-6 rounded-lg shadow-md bg-blue-400">
          <h2 class="text-2xl font-bold">Create New Event</h2>
          <p class="mt-2 mb-4">
            Click here to create a new event (coming soon)
          </p>
          <RouterLink
            to="/soon"
            class="inline-block bg-blue-900 text-white rounded-lg px-4 py-2 hover:bg-gray-900"
          >
            +
          </RouterLink>
        </div>
        <!-- end card 1 -->
        <div class="p-6 rounded-lg shadow-md bg-blue-400">
          <h2 class="text-2xl font-bold">Find New Events</h2>
          <p class="mt-2 mb-4">
            Click here to find events near you (coming soon)
          </p>
          <RouterLink
            to="/soon"
            class="inline-block bg-blue-900 text-white rounded-lg px-4 py-2 hover:bg-gray-900"
          >
            Search Events
          </RouterLink>
        </div>
      </div>
    </div>
  </section>
</template>
