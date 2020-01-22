import Vue from 'vue';
import Vuex from 'vuex';
import vuexI18n from 'vuex-i18n';
import translationsEn from '../../locale/en';
import translationsKz from '../../locale/kz';
import translationsRu from '../../locale/ru';

// Functions imported from src/api/index.js
import {
  fetchGames,
  fetchGameTypes,
  addGame,
  editGame,
  removeGame,
  fetchRoles,
  fetchUsers,
  editUsers,
  authenticate,
  register
} from '@/api';

import { isValidJwt, getUserDataFromJwt } from '@/utils';

Vue.use(Vuex);

const state = {
  // State is a single source of data in vuex
  games: [],
  gameTypes: [],
  roles: [],
  users: [],
  currentUser: {},
  jwt: '',
  languages: [
    {
      short: 'en',
      long: 'English'
    },
    {
      short: 'kz',
      long: 'Kazakh'
    },
    {
      short: 'ru',
      long: 'Русский'
    }
  ],
  currentLanguage: null
};

if (localStorage.getItem('currentLanguage')) {
  let language = localStorage.getItem('currentLanguage');
  state.languages.forEach(function(item) {
    if (item.short === language) {
      state.currentLanguage = item;
    }
  });
} else {
  state.currentLanguage = state.languages[0];
}

const actions = {
  // Asynchronous operations
  loadGames (context) {
    let securityToken = localStorage.getItem('securityToken');
    return fetchGames(securityToken).then(response => {
      context.commit('SET_GAMES', { games: response.data });
    });
  },
  loadGameTypes (context) {
    let securityToken = localStorage.getItem('securityToken');
    return fetchGameTypes(securityToken).then(response => {
      context.commit('SET_GAME_TYPES', { gameTypes: response.data });
    });
  },
  loadUsers (context) {
    let securityToken = localStorage.getItem('securityToken');
    return fetchUsers(securityToken).then(response => {
      context.commit('SET_USERS', {
        users: response.data
      });
    });
  },
  editUsers (context, payload) {
    let jwt = localStorage.getItem('securityToken');
    return editUsers(jwt, payload);
  },
  addGame (context, payload) {
    let jwt = localStorage.getItem('securityToken');
    return addGame(jwt, payload);
  },
  editGame (context, payload) {
    let jwt = localStorage.getItem('securityToken');
    return editGame(jwt, payload);
  },
  removeGame (context, payload) {
    let jwt = localStorage.getItem('securityToken');
    return removeGame(jwt, payload).then(() => {
      context.commit('REMOVE_GAME', payload)
    });
  },
  loadRoles (context) {
    return fetchRoles().then(response => {
      context.commit('SET_ROLES', { roles: response.data });
    });
  },
  login (context, userData) {
    context.commit('SET_USER_DATA', { userData });
    return authenticate(userData)
      .then(response => context.commit('SET_JWT_TOKEN', { jwt: response.data }))
  },
  logout (context) {
    context.commit('REMOVE_LOCAL_DATA');
  },
  register (context, userData) {
    context.commit('SET_USER_DATA', { userData });
    return register(userData);
  },
  setLanguage (context, language) {
    context.commit('SET_LANGUAGE', language);
  }
};

const mutations = {
  // Data mutations
  SET_GAMES (state, payload) {
    state.games = payload.games;
  },
  REMOVE_GAME (state, payload) {
    var gameId = payload.gameId;
    var newGames = [];
    for (var i = 0; i < state.games.length; i++) {
      if (state.games[i].id !== gameId) {
        newGames.push(state.games[i]);
      }
    }
    state.games = newGames;
  },
  SET_GAME_TYPES (state, payload) {
    state.gameTypes = payload.gameTypes;
  },
  SET_USERS (state, payload) {
    state.users = payload.users;
  },
  SET_USER_DATA (state, payload) {
    state.userData = payload.userData;
  },
  SET_JWT_TOKEN (state, payload) {
    state.jwt = payload.jwt;
    localStorage.setItem('securityToken', payload.jwt.token);
    state.currentUser = getUserDataFromJwt(state.jwt.token);
    localStorage.setItem('currentUser', JSON.stringify(state.currentUser));
  },
  REMOVE_JWT_TOKEN (state) {
    state.jwt = null;
    localStorage.removeItem('securityToken');
  },
  REMOVE_LOCAL_DATA (state) {
    if (state.jwt) {
      // state.jwt = null;
      state.jwt = '';
    }
    if (state.currentUser) {
      state.currentUser = {};
    }
    if (state.games) {
      state.games = [];
    }
    if (state.users) {
      state.users = [];
    }
    localStorage.removeItem('securityToken');
    localStorage.setItem('currentUser', JSON.stringify({}));
  },
  SET_LANGUAGE (state, lang) {
    state.currentLanguage = lang;
    localStorage.setItem('currentLanguage', lang);
  },
  SET_ROLES (state, payload) {
    state.roles = payload.roles;
  }
};

const getters = {
  // Getters for accessing data from the state or localStorage.
  isAuthenticated (state) {
    if (state.jwt) {
      return isValidJwt(state.jwt.token);
    } else {
      return isValidJwt(localStorage.getItem('securityToken'));
    }
  },
  isStandardUser (state) {
    if (state.currentUser.role) {
      return state.currentUser.role === 'Standard';
    } else if (JSON.parse(localStorage.getItem('currentUser'))) {
      return JSON.parse(localStorage.getItem('currentUser')).role === 'Standard';
    } else {
      return false;
    }
  },
  isAdmin (state) {
    if (state.currentUser.role) {
      return state.currentUser.role === 'Admin';
    } else if (JSON.parse(localStorage.getItem('currentUser'))) {
      return JSON.parse(localStorage.getItem('currentUser')).role === 'Admin';
    } else {
      return false;
    }
  },
  getCurrentUser (state) {
    if (state.currentUser.email) {
      return state.currentUser;
    } else {
      return JSON.parse(localStorage.getItem('currentUser'));
    }
  },
  getCurrentLanguage (state) {
    if (state.currentLanguage) {
      return state.currentLanguage;
    } else if (localStorage.getItem('currentLanguage')) {
      let language = localStorage.getItem('currentLanguage');
      state.languages.forEach(function(item) {
        if (item.short === language) {
          return item;
        }
      });
    } else {
      return state.languages[0];
    }
  }
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
});

Vue.use(vuexI18n.plugin, store);

Vue.i18n.add('en', translationsEn);
Vue.i18n.add('kz', translationsKz);
Vue.i18n.add('ru', translationsRu);

export default store;
