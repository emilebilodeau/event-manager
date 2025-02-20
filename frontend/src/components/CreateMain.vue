<script setup lang="ts">
import { reactive } from "vue";

interface InputData {
  [key: string]: string | number;
}

const eventQuestions: { [key: string]: string }[] = [
  { display: "Event Name", name: "name" },
  { display: "Description", name: "description" },
  { display: "Date", name: "date" },
  { display: "Location", name: "location" },
];

const data: InputData = reactive({});

eventQuestions.forEach((obj) => {
  data[obj.name] = "";
});

// TODO: install and use axios before implenting functionality
const submitData = () => {
  console.log(data);
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
        <div
          v-for="question in eventQuestions"
          :key="question.name"
          class="mb-6"
        >
          <label
            class="block text-black text-sm font-bold mb-2"
            :for="question.name"
          >
            {{ question.display }}
          </label>
          <input
            v-model="data[question.name]"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            :id="question.name"
            type="text"
            placeholder="Type here..."
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-900 hover:bg-blue-950 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
