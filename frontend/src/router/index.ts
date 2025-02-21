import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import EventListView from "@/views/EventListView.vue";
import NotFoundView from "@/views/NotFoundView.vue";
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
    {
      path: "/:catchAll(.*)",
      name: "not-found",
      component: NotFoundView,
    },
  ],
});

export default router;
