import { createRouter, createWebHashHistory } from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import About from '@/views/About'
import Playground from '@/views/Playground'
import Exams from '@/views/Exams'
import FinalGrades from '@/views/FinalGrades'
import ResourcesMpLists from '@/views/ResourcesMpLists'
import PreorderPlayground from '@/views/PreorderPlayground'
import MPs from '@/views/MPs'

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
    path: '/Playground/mp_lists',
    name: 'ResourcesMpLists',
    component: ResourcesMpLists
  },
  {
    path: '/Playground/PreorderPlayground',
    name: 'PreorderPlayground',
    component: PreorderPlayground
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
  },
  {
    path:'/MPs',
    name: 'MPs',
    component: MPs
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  linkExactActiveClass: 'is-active'
})

export default router