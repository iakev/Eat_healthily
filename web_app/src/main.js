import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import '../node_modules/bulma/css/bulma.css'
import '../node_modules/bulma-calendar/dist/css/bulma-calendar.min.css'

// axios making request to flask REST API
axios.defaults.baseURL = 'http://127.0.0.1:5000'

const app = createApp(App) // Create the root store

app.use(createPinia())
app.use(router)

app.mount('#app')
