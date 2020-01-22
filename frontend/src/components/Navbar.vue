<template>
  <nav class="navbar has-shadow is-fixed-top" id="main-navbar">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img
          src="/static/logo.png"
          :alt="'appTitle' | translate"
          width="28"
          height="28"
        />
      </a>
      <div
        class="navbar-burger burger"
        data-target="navMenu"
        @click="showNav = !showNav"
        :class="{ 'is-active': showNav }"
      >
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

    <div id="navMenu" class="navbar-menu" :class="{ 'is-active': showNav }">
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field is-grouped">
            <p class="control">
              <a class="button is-white" href="#">
                <b-select v-model="selectedLanguage">
                  <option v-for="(lang, index) in languages" :value="lang" :key="index">{{ lang.long }}</option>
                </b-select>
                <!--
                  {{ selectedLanguage }}
                -->
              </a>
            </p>
          </div>
        </div>

        <div class="navbar-item" v-if="!isAuthenticated">
          <a href="/login/">
            {{ 'sign_in' | translate }}
          </a>
        </div>

        <div class="navbar-item has-dropdown is-hoverable" v-if="isAuthenticated">
          <a class="navbar-link" href="#">
            <figure class="image is-24x24 is-rounded">
              <img
                src="static/portrait_placeholder.png"
              />
            </figure>
            <span>{{ 'hello' | translate }},</span>&nbsp;
            <span class="has-text-weight-bold"> {{ currentUser.email }} </span>
          </a>
          <div class="navbar-dropdown">
            <div class="navbar-item has-text-weight-bold">
              {{ 'app_title' | translate }}
            </div>
            <hr class="navbar-divider" />
            <a class="navbar-item is-leveled" href="# ">
              {{ 'account_settings' | translate }} &nbsp;
              <span class="icon">
                <i class="fa fa-cog"></i>
              </span>
            </a>
            <a class="navbar-item is-leveled" href="/logout">
              {{ 'sign_out' | translate }}
              <span class="icon">
                <i class="fa fa-sign-out"></i>
              </span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>

import { mapState } from 'vuex';
import Vue from 'vue';

export default {
  data() {
    return {
      selectedLanguage: this.$store.getters.getCurrentLanguage,
      showNav: false
    }
  },
  computed: {
    ...mapState(['languages'])
  },
  created() {
    Vue.i18n.set(this.$store.getters.getCurrentLanguage.short);
  },
  watch: {
    'selectedLanguage': function(newLang) {
      Vue.i18n.set(newLang.short);
      this.$store.dispatch('setLanguage', newLang.short);
    }
  }
};
</script>

<style>
</style>
