import Vue from 'vue';
import App from './App';
import router from './router';
import store from './store';

import Buefy from 'buefy';
import 'buefy/dist/buefy.css';

import Vuelidate from 'vuelidate';
import VueI18n from 'vue-i18n'

Vue.use(Buefy);
Vue.use(Vuelidate);
Vue.use(VueI18n);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
