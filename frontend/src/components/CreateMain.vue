<script setup lang="ts">
import { ref } from "vue";
import type { Ref } from "vue";

interface InputData {
  [key: string]: string | number;
}

const eventQuestions: Ref<string[]> = ref([
  "Event Name",
  "Description",
  "Date",
]);

const data: Ref<InputData> = ref({});

const submitData = () => {
  alert("Event Created!");
};
</script>

<template>
  <section class="bg-blue-300 py-20 min-h-svh">
    <div class="container-xl lg:container lg:max-w-7xl m-auto">
      <form
        @submit.prevent="submitData"
        class="p-6 rounded-lg shadow-md bg-blue-400"
      >
        <div v-for="question in eventQuestions" :key="question" class="py-4">
          <h1 class="text-2xl font-extrabold py-2">{{ question }}</h1>
          <input type="text" />
        </div>
        <button
          type="submit"
          class="px-6 py-2 rounded-lg text-white bg-blue-900"
        >
          Create
        </button>
      </form>
    </div>
  </section>
</template>
