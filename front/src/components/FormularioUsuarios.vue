<template>
  <v-card class="pa-4">
    <v-card-title>Agregar Usuario</v-card-title>
    <v-card-text>
      <v-form ref="form" @submit.prevent="submitForm">
        <v-text-field
          v-model="nombre"
          label="Nombre"
          required
        />
        <v-text-field
          v-model="email"
          label="Correo electrónico"
          required
        />
        <v-select
          v-model="rol"
          :items="roles"
          label="Rol"
          required
        />
        <v-btn type="submit" color="primary" class="mt-3">
          Agregar
        </v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const nombre = ref("");
const email = ref("");
const rol = ref("");

const roles = ["Admin", "User"]; // Roles de ejemplo

const submitForm = async () => {
  if (!nombre.value || !email.value || !rol.value) return;

  try {
    const response = await axios.post("http://localhost:8000/users", {
      nombre: nombre.value,
      email: email.value,
      rol: rol.value,
    });
    alert(`Usuario ${response.data.nombre} agregado correctamente`);
    
    // Limpiar formulario
    nombre.value = "";
    email.value = "";
    rol.value = "";

  } catch (error) {
    console.error("Error al agregar usuario:", error);
    alert("No se pudo agregar el usuario");
  }
};
</script>
