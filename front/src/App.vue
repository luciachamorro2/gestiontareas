<template>
  <v-app>
    <Header />
        <v-main> 
    <v-container>
      <tabla-tareas
        :tasks="tasks"
        @editar="editarTarea"
      />

       <tabla-usuarios
          :usuarios="usuarios"
          @editar="editarUsuario"
        />

    </v-container>
    </v-main>


  </v-app>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Header from "@/components/Header.vue";
import TablaTareas from "@/components/TablaTareas.vue";
import TablaUsuarios from "@/components/TablaUsuarios.vue";
import { getTasks, getUsers } from "@/services/api";


const tasks = ref([]);
const usuarios = ref([]);

const editarTarea = (tarea) => {
  console.log("Editar tarea:", tarea);
  alert(`Editar tarea: ${tarea.titulo}`);
};


// Acción al editar usuario
const editarUsuario = (usuario) => {
  console.log("Editar usuario:", usuario);
  alert(`Editar usuario: ${usuario.nombre}`);
};

onMounted(async () => {
  try {
    const tasksRes = await getTasks();
    tasks.value = tasksRes.data;

    const usersRes = await getUsers();
    usuarios.value = usersRes.data;
  } catch (error) {
    console.error("Error al cargar datos:", error);
  }
});

</script>

