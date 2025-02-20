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
    <div class="max-w-7xl m-auto w-1/3">
      <form
        @submit.prevent="submitData"
        class="bg-blue-400 shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
        <div v-for="question in eventQuestions" :key="question" class="mb-4">
          <label
            class="block text-black text-sm font-bold mb-2"
            :for="question"
          >
            {{ question }}
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            :id="question"
            type="text"
            placeholder="Type here"
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-900 hover:bg-blue-950 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
