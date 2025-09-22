import { ref } from "vue";

export function useUsuarios() {
  const headers = ref([
    { title: "ID", key: "id" },
    { title: "Nombre", key: "nombre" },
    { title: "Correo", key: "correo" },
    { title: "Rol", key: "rol" },
    { title: "Tareas", key: "tareas" },
    { title: "Acciones", key: "acciones", sortable: false },
  ]);

  return {
    headers,
  };
}
