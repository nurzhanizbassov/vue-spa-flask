<template>
  <div class="column is-4-tablet is-3-desktop is-2-widescreen">
    <aside class="menu">
      <p class="menu-label">{{ 'section' | translate }} 1</p>
      <ul class="menu-list">
        <li v-if="isAuthenticated && isAdmin">
          <a class="is-active" href="/users">
            <span class="icon">
              <i class="fa fa-user"></i>
            </span> &nbsp;
            {{ 'users' | translate }}
          </a>
        </li>
        <li v-if="isAuthenticated && isStandardUser">
          <a href="/games">
            <span class="icon">
              <i class="fa fa-user"></i>
            </span> &nbsp;
            {{ 'games' | translate }}
          </a>
        </li>
        <li>
          <a  href="#">
            <span class="icon">
                <i class="fas fa-chart-bar"></i>
            </span>
            {{ 'statistics' | translate }}
          </a>
        </li>
      </ul>
      <p class="menu-label">{{ 'section' | translate }} 2</p>
      <ul class="menu-list">
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
              <!--
              <i class="fa fa-file-text"></i>
              -->
            </span>
            {{ 'subsection' | translate }} 2.1
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
            </span>
            {{ 'subsection' | translate }} 2.2
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
            </span>
            {{ 'subsection' | translate }} 2.3
          </a>
        </li>
      </ul>
      <p class="menu-label">{{ 'section' | translate }} 3</p>
      <ul class="menu-list">
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
            </span>
            {{ 'subsection' | translate }} 3.1
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
            </span>
            {{ 'subsection' | translate }} 3.2
          </a>
        </li>
        <li>
          <a href="#">
            <span class="icon">
              <i class="fa fa-file"></i>
            </span>
            {{ 'subsection' | translate }} 3.3
          </a>
        </li>
      </ul>
    </aside>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      current: 'roles.index',
      user: {}
    };
  },
  methods: {
    route(item) {
      return item;
    },
    activeClass(route) {
      return this.route(route) === this.current ? 'is-active' : '';
    }
  }
};
</script>

<style>
</style>
