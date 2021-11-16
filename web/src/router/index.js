import { createRouter, createWebHashHistory } from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/views/About'
import Playground from '@/views/Playground'

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/Overview',
    name: 'Overview',
    component: About
  },
  {
    path: '/Playground',
    name: 'Playground',
    component: Playground
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router