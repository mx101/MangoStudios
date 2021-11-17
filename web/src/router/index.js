import { createRouter, createWebHashHistory } from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/views/About'
import Playground from '@/views/Playground'
import Exams from '@/views/Exams'

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
  },
  {
    path: '/Exams',
    name: 'Exams',
    component: Exams
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router