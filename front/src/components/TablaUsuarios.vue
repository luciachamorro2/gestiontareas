<template>
  <v-card>
    <v-card-title class="text-h6">
      Lista de Usuarios
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="usuarios"
      :items-per-page="5"
      class="elevation-1"
    >
      <!-- Slot de Acciones (editar y eliminar) -->
      <template v-slot:[`item.acciones`]="{ item }">
        <v-icon size="small" class="me-2" @click="$emit('editar', item)">
          mdi-pencil
        </v-icon>
        <v-icon size="small" color="red" @click="eliminarUsuario(item.id)">
          mdi-delete
        </v-icon>
      </template>

      <!-- Slot de Tareas -->
      <template v-slot:[`item.tareas`]="{ item }">
        <v-chip
          v-for="tarea in item.tareas"
          :key="tarea"
          color="blue-grey"
          small
          class="ma-1"
          dark
        >
          {{ tarea }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const props = defineProps({
  usuarios: {
    type: Array,
    required: true,
  },
});

defineEmits(["editar", "actualizar-lista"]);

const headers = ref([
  { title: "ID", key: "id" },
  { title: "Nombre", key: "nombre" },
  { title: "Correo", key: "correo" },
  { title: "Rol", key: "rol" },
  { title: "Tareas", key: "tareas", sortable: false },
  { title: "Acciones", key: "acciones", sortable: false },
]);

const eliminarUsuario = async (id) => {
  if (!confirm("¿Estás seguro de que quieres eliminar este usuario?")) {
    return;
  }
  try {
    await axios.delete(`http://localhost:8000/users/${id}`);
    alert(`Usuario eliminado correctamente`);
    emit("actualizar-lista");
  } catch (error) {
    alert("Error al eliminar usuario");
  }
};
</script>
