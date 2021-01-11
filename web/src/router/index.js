import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Games from '@/components/games/Games';
import AddGame from '@/components/games/AddGame';
import EditGame from '@/components/games/EditGame'; import Users from '@/components/Users';
import Registration from '@/components/Registration';
import Login from '@/components/Login';
import PageNotFound from '@/components/PageNotFound';
import NotAuthorized from '@/components/NotAuthorized';
import store from '@/store';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/games',
      name: 'Games',
      component: Games,
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login');
        } else if (!store.getters.isStandardUser) {
          next('/401');
        } else {
          console.log('User token is fine');
          next();
        }
      }
    },
    {
      path: '/games/add',
      name: 'AddGame',
      component: AddGame,
      beforeEnter (to, from, next) {
        if (!store.getters.isStandardUser) {
          console.log('User is NOT authenticated');
          next('/login');
        } else if (!store.getters.isStandardUser) {
          next('/401');
        } else {
          console.log('User token is fine');
          next();
        }
      }
    },
    {
      path: '/games/edit',
      name: 'EditGame',
      component: EditGame,
      props: true,
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          console.log('User is NOT authenticated');
          next('/login');
        } else if (!store.getters.isStandardUser) {
          next('/401');
        } else {
          console.log('User token is fine');
          next();
        }
      }
    },
    {
      path: '/users',
      name: 'Users',
      component: Users,
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login');
        } else if (!store.getters.isAdmin) {
          next('/401');
        } else {
          next();
        }
      }
    },
    {
      path: '/register',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      beforeEnter (to, from, next) {
        store.dispatch('logout');
        next('/');
      }
    },
    {
      path: '/401',
      name: 'NotAuthorized',
      component: NotAuthorized
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    }
  ]
});
