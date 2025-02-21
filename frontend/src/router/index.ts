import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import EventListView from "@/views/EventListView.vue";
import TempView from "@/views/TempView.vue";
import CreateEventView from "@/views/CreateEventView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/events",
      name: "events",
      component: EventListView,
    },
    {
      path: "/create",
      name: "create",
      component: CreateEventView,
    },
    // NOTE: temporary routing, replace with real component
    {
      path: "/soon",
      name: "soon",
      component: TempView,
    },
  ],
});

export default router;
