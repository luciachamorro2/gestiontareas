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

        <FormularioUsuarios @usuario-agregado="fetchUsers" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Header from "@/components/Header.vue";
import TablaTareas from "@/components/TablaTareas.vue";
import TablaUsuarios from "@/components/TablaUsuarios.vue";
import FormularioUsuarios from "@/components/FormularioUsuarios.vue";
import { getTasks, getUsers } from "@/services/api";

const tasks = ref([]);
const usuarios = ref([]);

// Función para recargar usuarios desde el backend
const fetchUsers = async () => {
  try {
    const usersRes = await getUsers();
    usuarios.value = usersRes.data;
  } catch (error) {
    console.error("Error al cargar usuarios:", error);
  }
};

// Cargar datos al montar el componente
onMounted(async () => {
  try {
    const tasksRes = await getTasks();
    tasks.value = tasksRes.data;

    await fetchUsers(); // Aquí usamos la misma función para usuarios
  } catch (error) {
    console.error("Error al cargar datos:", error);
  }
});

const editarTarea = (tarea) => {
  console.log("Editar tarea:", tarea);
  alert(`Editar tarea: ${tarea.titulo}`);
};

const editarUsuario = (usuario) => {
  console.log("Editar usuario:", usuario);
  alert(`Editar usuario: ${usuario.nombre}`);
};
</script>
