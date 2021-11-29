import { createRouter, createWebHashHistory } from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import About from '@/views/About'
import Playground from '@/views/Playground'
import Exams from '@/views/Exams'
import FinalGrades from '@/views/FinalGrades'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: About
  },
  {
    path: '/Overview',
    name: 'Overview',
    component: About
  },
  {
    path: '/Playground/BinarySearchTree',
    name: 'Playground',
    component: Playground
  },
  {
    path: '/Exams',
    name: 'Exams',
    component: Exams
  },
  {
    path: '/FinalGrades',
    name: 'FinalGrades',
    component: FinalGrades
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  linkExactActiveClass: 'is-active'
})

export default router