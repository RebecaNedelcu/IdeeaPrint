import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{
       path: '', component: () => import('pages/Index.vue')},
       {path: '/contact', component: () => import('pages/Contact.vue')},
       {path: '/design', component: () => import('pages/Design.vue')},
       {path: '/shop/:id', component: () => import('pages/Shop.vue')},
       {path: '/details/:productType/:illustrationId', component: () => import('pages/DetailsItem.vue')},
       {path: '/step2/:productType', component: () => import('pages/Step2.vue')},
       {path: '/step3/:productType/:idProduct/:price/:size/:name', component: () => import('pages/Step3.vue')},
       {path: '/favorite', component: () => import('pages/Favorite.vue')},
       {path: '/checkout', component: () => import('pages/Checkout.vue')},
       {path: '/profile', component: () => import('pages/Profile.vue')},
      ],
  },

  {
    path: '/signup',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/Signup.vue') }],
  },
  {
    path: '/signin',
    component: () => import('layouts/AuthLayout.vue'),
    children: [{ path: '', component: () => import('pages/Signin.vue') }],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
