<script setup lang="ts">
import { ref, onMounted } from "vue";

const data: any = ref();

onMounted(async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/test");
    const res: any = await response.json();
    // map returns an array with the result of calling provided function...
    // ... on every element of the calling array
    data.value = res;
    console.log(data);
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
    </section>
  </main>
</template>
