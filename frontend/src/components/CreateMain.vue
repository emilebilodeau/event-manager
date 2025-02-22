<script setup lang="ts">
import { reactive } from "vue";
import axios from "axios";
import router from "@/router";

interface InputData {
  [key: string]: string | number | Record<string, string | number>;
  location: Record<string, string | number>;
}

const textQuestions: { [key: string]: string }[] = [
  { display: "Event Name", name: "name" },
  { display: "Description", name: "description" },
  // NOTE: date will need to be a timestamp, probably using a date picker...
  // ...might need to be moved somewhere else
  { display: "Date", name: "date" },
];

const locationQuestion: { [key: string]: string }[] = [
  { display: "Address", name: "address" },
  { display: "City", name: "city" },
  { display: "State", name: "state" },
];

const data: InputData = reactive({
  location: {},
});

textQuestions.forEach((obj) => {
  data[obj.name] = "";
});

// NOTE: location will be a subdocument, and will include a map later
locationQuestion.forEach((obj) => {
  data.location[obj.name] = "";
});

const submitData = async () => {
  console.log(data);

  try {
    const response = await axios.post(
      "http://127.0.0.1:5000/events/create",
      data
    );
    if ((response.status = 201)) {
      alert("Event successfully created!");
      router.push({ name: "home" });
      router.go(1);
    }
  } catch (err: any) {
    if (err.response) {
      // server responded with a status code outside 2xx
      console.error("Server Error:", err.response.data);
      alert(`Error: ${err.response.data.error}`);
    } else if (err.request) {
      // request was made but no response received
      console.error("No Response from Server:", err.request);
      alert("No response from server. Please try again.");
    } else {
      // something else happened (e.g., network issues)
      console.error("Unexpected Error:", err.message);
      alert("Unexpected error occurred. Please try again.");
    }
  }
};
</script>

<template>
  <section class="bg-blue-300 py-20 min-h-svh">
    <div class="max-w-7xl m-auto w-1/3">
      <form
        @submit.prevent="submitData"
        class="bg-blue-400 shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
        <h1 class="section-header">General Information</h1>
        <div
          v-for="question in textQuestions"
          :key="question.name"
          class="mb-6"
        >
          <label class="section-label" :for="question.name">
            {{ question.display }}
          </label>
          <input
            v-model="data[question.name]"
            class="input-element focus:outline-none focus:shadow-outline"
            :id="question.name"
            type="text"
            placeholder="Type here..."
          />
        </div>
        <h1 class="section-header">Location Information</h1>
        <div
          v-for="locationq in locationQuestion"
          :key="locationq.name"
          class="mb-6"
        >
          <label class="section-label" :for="locationq.name">
            {{ locationq.display }}
          </label>
          <input
            v-model="data.location[locationq.name]"
            class="input-element focus:outline-none focus:shadow-outline"
            :id="locationq.name"
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

<style scoped>
.section-header {
  @apply block text-2xl text-black font-bold mb-4;
}

.section-label {
  @apply block text-black text-lg font-bold mb-2;
}

.input-element {
  @apply shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight;
}
</style>
