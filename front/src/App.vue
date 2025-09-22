<template>
  <v-app>
    <Header />
        <v-main> 
    <v-container>
      <tabla-tareas
        :tasks="tasks"
        @editar="editarTarea"
      />
    </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Header from "@/components/Header.vue";
import TablaTareas from "@/components/TablaTareas.vue";
import { getTasks } from "@/services/api";

const tasks = ref([]);

const editarTarea = (tarea) => {
  console.log("Editar tarea:", tarea);
  alert(`Editar tarea: ${tarea.titulo}`);
};

// Cargar tareas desde el backend al montar el componente
onMounted(async () => {
  try {
    const response = await getTasks();
    tasks.value = response.data;
  } catch (error) {
    console.error("Error al cargar tareas:", error);
  }
});
</script>

