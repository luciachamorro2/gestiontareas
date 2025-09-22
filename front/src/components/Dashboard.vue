<template>
  <div>
    <FormularioUsuario @usuario-agregado="cargarUsuarios" />
    <TablaUsuarios :usuarios="usuarios" @actualizar-lista="cargarUsuarios" />
    <TablaTareas :tasks="tareas" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import FormularioUsuario from './FormularioUsuario.vue'
import TablaUsuarios from './TablaUsuarios.vue'
import TablaTareas from './TablaTareas.vue'

const usuarios = ref([])
const tareas = ref([])

const cargarUsuarios = async () => {
  try {
    const res = await axios.get('http://localhost:8000/users')
    usuarios.value = res.data
  } catch (e) {
    console.error('Error cargando usuarios:', e)
  }
}

const cargarTareas = async () => {
  try {
    const res = await axios.get('http://localhost:8000/tasks')
