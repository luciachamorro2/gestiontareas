<template>
  <v-card>
    <v-card-title class="text-h6">
      Lista de Tareas
    </v-card-title>

    <v-data-table
      :headers="headers"
      :items="tasks"
      :items-per-page="5"
      class="elevation-1"
    >
      <!-- ✅ Slot de encabezados -->
      <template v-slot:headers="{ columns }">
        <tr>
          <th
            v-for="column in columns"
            :key="column.key"
            class="text-left font-weight-bold"
          >
            <!-- Icono opcional delante del título -->
            <v-icon v-if="column.key === 'estado'" size="small" class="me-1">
              mdi-flag
            </v-icon>
            {{ column.title }}
          </th>
        </tr>
      </template>

      <!-- Columna Estado -->
      <template v-slot:[`item.estado`]="{ item }">
        <v-chip :color="getEstadoColor(item.estado)" dark size="small">
          {{ item.estado }}
        </v-chip>
      </template>

      <!-- Columna Acciones -->
      <template v-slot:[`item.acciones`]="{ item }">
        <v-icon size="small" class="me-2" @click="$emit('editar', item)">
          mdi-pencil
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup>
import { useTareas } from "@/composables/useTareas";

const props = defineProps({
  tasks: {
    type: Array,
    required: true,
  },
});

defineEmits(["editar"]);

const { headers, getEstadoColor } = useTareas();
</script>
