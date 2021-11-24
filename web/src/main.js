// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'mdbvue'
import 'd3'
import 'chart.js'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
// import {tree1} from "@benjaminadk/simple-binary-search-tree"

createApp(App).use(router).mount('#app')