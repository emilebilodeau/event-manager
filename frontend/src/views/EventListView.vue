<script setup lang="ts">
import { ref, onMounted } from "vue";

interface EventsData {
  events: [];
  message: string;
}

const data = ref([]);

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/event/test");
    const res: EventsData = await response.json();
    console.log(res);
    data.value = res.events;
  } catch (error) {
    console.log(error);
  }
});
</script>

<template>
  <main>
    <section>
      <h1 class="text-2xl">Event List</h1>
      <p>List of events goes here</p>
      <p v-for="event in data" :key="event">
        {{ event }}
      </p>
    </section>
  </main>
</template>
