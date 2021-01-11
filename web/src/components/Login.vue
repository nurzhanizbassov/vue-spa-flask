<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ 'sign_in' | translate }} {{ 'or' | translate }} {{ 'register' | translate }}</h2>
          <!-- <p class="subtitle error-msg">{{ errorMsg }}</p> -->
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="field">
          <label class="label is-medium" for="email">{{ 'email' | translate }}</label>
          <div class="control">
            <input type="email" class="input is-medium" id="email" v-model="email" />
          </div>
        </div>
        <div class="field">
          <label class="label is-medium" for="password">{{ 'password' | translate }}</label>
          <div class="control">
            <input type="password" class="input is-medium" id="password" v-model="password" />
          </div>
        </div>

        <div class="control">
          <a class="button is-medium is-primary" @click="authenticate">{{ 'sign_in' | translate }}</a>
          <a class="button is-medium is-success" @click="register"> {{ 'register' | translate }}</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    authenticate () {
      this.$store
        .dispatch('login', { email: this.email, password: this.password })
        .then(
          () => (
            this.$router.push('/')
          )
        )
        .catch(
          () =>
          this.$toasted.global.toasted_error({ message: this.$i18n.translate('login_failed') })
        );
    },
    register () {
      this.$router.push('/register');
    }
  }
};
</script>
