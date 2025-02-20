<script setup lang="ts">
import { ref, onMounted } from "vue";
import type { Ref } from "vue";

interface EventsData {
  events: string[];
  test: string;
}

interface Data {
  [key: string]: string[] | string;
}

const data: Ref<Data> = ref({});

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/events/test");
    const res: EventsData = await response.json();
    console.log("Status Code:", response.status);
    console.log(res);
    data.value["events"] = res.events;
    data.value["test"] = res.test;
  } catch (error) {
    console.log(error);
  }
});
</script>

<template>
  <main>
    <section>
      <h1 class="text-2xl">Event List</h1>
      <p>List of events goes here: {{ data.test }}</p>
      <p v-for="event in data.events" :key="event">
        {{ event }}
      </p>
    </section>
  </main>
</template>
