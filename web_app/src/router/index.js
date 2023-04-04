import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import FarmerPageView from '../views/FarmerPageView.vue'
import ConsumerPageView from '../views/ConsumerPageView.vue'
import FarmProductsView from '../views/FarmProductsView.vue'
// import FarmProductView from '../views/FarmProductView.vue'
import TrackingView from '../views/TrackingView.vue'
import FarmPageView from '../views/FarmPageView.vue'
import InputView from '../views/InputView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/farmers/:farmer_id',
      name: 'farmer',
      component: FarmerPageView
    },
    {
      path: '/farmpage/:farm_id',
      name: 'farm',
      component: FarmPageView
    },
    {
      path: '/consumerdash',
      name: 'consumerdash',
      component: ConsumerPageView
    },
    {
      path: '/farmproducts/:product_id',
      name: 'farmproducts',
      component: FarmProductsView
    },
    // {
    //   path: '/farmproducts/:farmproduct_id',
    //   name: 'farmproduct',
    //   component: FarmProductView
    // },
    {
      path: '/traking/:farmproduct_id',
      name: 'tracking',
      component: TrackingView
    },
    {
      path: '/inputs',
      name: 'inputs',
      component: InputView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
