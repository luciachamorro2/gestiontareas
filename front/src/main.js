// main.js
import { createApp } from 'vue'
import App from './App.vue'
import '@mdi/font/css/materialdesignicons.css'  // Importar estilos fuentes iconos





// Importar estilos base de Vuetify
import 'vuetify/styles'

// Importar fuente de iconos Material Design
import '@mdi/font/css/materialdesignicons.css'

// Importar Vuetify y componentes/directivas
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'



// Crear instancia Vuetify con configuración para iconos mdi
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
})

const app = createApp(App)

// Usar Vuetify
app.use(vuetify)

// Montar app
app.mount('#app')
