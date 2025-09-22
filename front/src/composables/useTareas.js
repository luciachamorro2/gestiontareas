import { ref } from "vue";

export function useTareas() {
  const headers = ref([
    { title: "Tarea", key: "titulo" },
    { title: "Fecha", key: "fecha" },
    { title: "Destinatario", key: "destinatario" },
    { title: "Mensaje", key: "mensaje" },
    { title: "Notificaciones", key: "notificaciones" },
    { title: "Estado", key: "estado" },
    { title: "Acciones", key: "acciones", sortable: false },
  ]);

  const getEstadoColor = (estado) => {
    switch (estado) {
      case "Pendiente":
        return "orange";
      case "Completada":
        return "green";
      case "Vencida":
        return "red";
      case "Boceto":
        return "blue-grey";
      default:
        return "grey";
    }
  };

  return {
    headers,
    getEstadoColor,
  };
}

