<template>
  <div id="somewebapp">
    <app-navbar></app-navbar>
    <section class="section sticky-footer-wrapper">
      <div class="columns">
        <app-sidebar></app-sidebar>
        <main class="column is-8-tablet is-9-desktop is-9-widescreen">
          <router-view />
        </main>
      </div>
    </section>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Vue from 'vue';
import AppNavbar from '@/components/Navbar';
import AppSidebar from '@/components/Sidebar';
import AppFooter from '@/components/Footer';
import Toasted from 'vue-toasted';

Vue.mixin({
  computed: {
    isAuthenticated () {
      return this.$store.getters.isAuthenticated;
    },
    currentUser () {
      return this.$store.getters.getCurrentUser;
    },
    isStandardUser () {
      return this.$store.getters.isStandardUser;
    },
    isAdmin () {
      return this.$store.getters.isAdmin;
    }
  }
});

// Define additional options for the vue-toasted
let toastedOptions = {
  'singleton': true
}

Vue.use(Toasted, toastedOptions);

// Error options to the toast
let errorOptions = {
    type: 'error',
    duration: '10000'
};

// Register the toast with the custom message
Vue.toasted.register('toasted_error',
    (payload) => {
        // If there is no message passed show default message
        if (!payload.message) {
          return 'Something Went Wrong...';
        }
        // If there is a message show it with the message
        return payload.message;
    },
    errorOptions
)

// Success options to the toast
let successOptions = {
    type: 'success',
    duration: '10000'
};

// Register the toast with the custom message
Vue.toasted.register('toasted_success',
    (payload) => {
        // If there is no message passed show default message
        if (!payload.message) {
          return 'Success!'
        }
        // If there is a message show it with the message
        return payload.message;
    },
    successOptions
)

// Warning options to the toast
let warningOptions = {
    type: 'warning',
    duration: '10000'
};

// Register the toast with the custom message
Vue.toasted.register('toasted_warning',
    (payload) => {
        // If there is no message passed show default message
        if (!payload.message) {
          return 'Warning!'
        }
        // If there is a message show it with the message
        return payload.message;
    },
    warningOptions
)

export default {
  name: 'App',
  components: { AppNavbar, AppSidebar, AppFooter }
};
</script>

<style lang="css">

  @import '../node_modules/@fortawesome/fontawesome-free/css/all.css';

</style>
