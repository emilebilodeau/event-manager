import { ref, computed } from "vue";
import { defineStore } from "pinia";

// NOTE: don't know what this is, i assume it's pinia related
export const useCounterStore = defineStore("counter", () => {
  const count = ref(0);
  const doubleCount = computed(() => count.value * 2);
  function increment() {
    count.value++;
  }

  return { count, doubleCount, increment };
});
