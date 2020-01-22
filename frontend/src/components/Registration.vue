<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ 'register' | translate }}</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <form id="registration-form" @submit="register">
        <div class="container">
          <b-field
            :label="'username' | translate"
            :type="usernameStyleType"
            :custom-class="usernameCustomClass"
            :message="usernameErrorMessage"
          >
            <b-input
              id="username"
              name="username"
              v-model.trim="$v.username.$model"
              @focus="$v.username.$touch"
              type="text"
            ></b-input>
          </b-field>
          <b-field
            :label="'email' | translate"
            :type="emailStyleType"
            :custom-class="emailCustomClass"
            :message="emailErrorMessage"
          >
            <b-input
              id="email"
              name="email"
              v-model.trim="$v.email.$model"
              @focus="$v.email.$touch"
              icon-pack="fas"
              icon="envelope"
            ></b-input>
          </b-field>
          <b-field
            :label="'phone_number' | translate"
            :type="phoneNumberStyleType"
            :custom-class="phoneNumberCustomClass"
            :message="phoneNumberErrorMessage"
          >
            <b-input
              id="phone-number"
              name="phone-number"
              v-model.trim="$v.phoneNumber.$model"
              @focus="$v.phoneNumber.$touch"
              type="phone-number"
              icon-pack="fas"
              icon="phone"
            ></b-input>
          </b-field>
          <b-field
            :label="'role' | translate"
            :type="roleStyleType"
            :custom-class="roleCustomClass"
            :message="roleErrorMessage"
          >
            <b-select
              :placeholder="'select_role' | translate"
              id="role"
              name="role"
              expanded
              v-model.trim="$v.role.$model"
              @focus="$v.role.$touch"
            >
              <option v-for="role in roles" :value="role.id" :key="role.id">
                <p v-if="currentLanguage == 'en'">{{ role.name_en }}</p>
                <p v-if="currentLanguage == 'kz'">{{ role.name_kz }}</p>
                <p v-if="currentLanguage == 'ru'">{{ role.name_ru }}</p>
              </option>
            </b-select>
          </b-field>
          <b-field
            :label="'password' | translate"
            :type="passwordStyleType"
            :custom-class="passwordCustomClass"
            :message="passwordErrorMessage"
          >
            <b-input
              id="password"
              name="password"
              type="password"
              v-model.trim="$v.password.$model"
              @focus="$v.password.$touch"
            ></b-input>
          </b-field>
          <b-field
            :label="'repeat_password' | translate"
            :type="repeatPasswordStyleType"
            :custom-class="repeatPasswordCustomClass"
            :message="repeatPasswordErrorMessage"
          >
            <b-input
              id="repeat-password"
              name="repeat-password"
              type="password"
              v-model.trim="$v.repeatPassword.$model"
              @focus="$v.password.$touch"
            ></b-input>
          </b-field>
          <b-button
            type="is-primary"
            id="submit-registration-button"
            :disabled="!formValid"
            @click.prevent="register()"
          >{{ 'register' | translate }}</b-button>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import Toasted from 'vue-toasted';
import Vue from 'vue';
import { mapState } from 'vuex';
import { required, minLength, sameAs } from 'vuelidate/lib/validators';
import { singleErrorExtractorMixin } from 'vuelidate-error-extractor';

Vue.use(Toasted);

export default {
  data() {
    return {
      username: '',
      email: '',
      phoneNumber: '',
      role: '',
      password: '',
      repeatPassword: ''
    };
  },
  validations: {
    username: {
      required,
      minLength: minLength(6)
    },
    email: {
      required
    },
    phoneNumber: {
      required
    },
    role: {
      required
    },
    password: {
      required,
      minLength: minLength(6)
    },
    repeatPassword: {
      required,
      minLength: minLength(6),
      sameAsPassword: sameAs('password')
    }
  },
  created() {
    this.fetchRoles();
  },
  extends: singleErrorExtractorMixin,
  computed: {
    ...mapState({
      roles: state => state.roles
    }),
    currentLanguage() {
      let l = this.$i18n.locale();
      return l;
    },

    usernameStyleType() {
      return this.$v.username.$error
        ? 'is-danger'
        : !this.$v.username.$invalid
        ? 'is-success'
        : null;
    },
    usernameCustomClass() {
      return this.$v.username.$error
        ? 'has-text-danger'
        : !this.$v.username.$invalid
        ? 'has-text-success'
        : null;
    },
    usernameErrorMessage() {
      if (!this.$v.username.required) {
        return !this.$v.username.required && this.$v.username.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      } else if (!this.$v.username.minLength) {
        return (
          this.$v.username.$params.minLength.min +
          ' ' +
          this.$i18n.translate('characters_minimum')
        );
      }
    },

    phoneNumberStyleType() {
      return this.$v.phoneNumber.$error
        ? 'is-danger'
        : !this.$v.phoneNumber.$invalid
        ? 'is-success'
        : null;
    },
    phoneNumberCustomClass() {
      return this.$v.phoneNumber.$error
        ? 'has-text-danger'
        : !this.$v.phoneNumber.$invalid
        ? 'has-text-success'
        : null;
    },
    phoneNumberErrorMessage() {
      if (!this.$v.phoneNumber.required) {
        return !this.$v.phoneNumber.required && this.$v.phoneNumber.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    emailStyleType() {
      return this.$v.email.$error
        ? 'is-danger'
        : !this.$v.email.$invalid
        ? 'is-success'
        : null;
    },
    emailCustomClass() {
      return this.$v.email.$error
        ? 'has-text-danger'
        : !this.$v.email.$invalid
        ? 'has-text-success'
        : null;
    },
    emailErrorMessage() {
      if (!this.$v.email.required) {
        return !this.$v.email.required && this.$v.email.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    passwordStyleType() {
      return this.$v.password.$error
        ? 'is-danger'
        : !this.$v.password.$invalid
        ? 'is-success'
        : null;
    },
    passwordCustomClass() {
      return this.$v.password.$error
        ? 'has-text-danger'
        : !this.$v.password.$invalid
        ? 'has-text-success'
        : null;
    },
    passwordErrorMessage() {
      if (!this.$v.password.required) {
        return !this.$v.password.required && this.$v.password.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      } else if (!this.$v.password.minLength) {
        return this.$v.password.$params.minLength.min + ' characters minimum!';
      }
    },
    roleStyleType() {
      return this.$v.role.$error
        ? 'is-danger'
        : !this.$v.role.$invalid
        ? 'is-success'
        : null;
    },
    roleCustomClass() {
      return this.$v.role.$error
        ? 'has-text-danger'
        : !this.$v.role.$invalid
        ? 'has-text-success'
        : null;
    },
    roleErrorMessage() {
      if (!this.$v.role.required) {
        return !this.$v.role.required && this.$v.role.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    repeatPasswordStyleType() {
      return this.$v.repeatPassword.$error
        ? 'is-danger'
        : !this.$v.repeatPassword.$invalid
        ? 'is-success'
        : null;
    },
    repeatPasswordCustomClass() {
      return this.$v.repeatPassword.$error && this.$v.repeatPassword.minLength
        ? 'has-text-danger'
        : !this.$v.repeatPassword.$invalid
        ? 'has-text-success'
        : null;
    },
    repeatPasswordErrorMessage() {
      if (
        this.$v.repeatPassword.$model !== '' &&
        !this.$v.repeatPassword.sameAsPassword
      ) {
        return this.$i18n.translate('passwords_not_identical');
      } else if (!this.$v.repeatPassword.minLength) {
        return (
          this.$v.repeatPassword.$params.minLength.min +
          ' ' +
          this.$i18n.translate('characters_minimum')
        );
      } else {
        return null;
      }
    },
    formValid() {
      return (
        !this.$v.username.$invalid &&
        !this.$v.phoneNumber.$invalid &&
        !this.$v.email.$invalid
      );
    }
  },
  methods: {
    register() {
      this.$store
        .dispatch('register', {
          username: this.username,
          email: this.email,
          phoneNumber: this.phoneNumber,
          roleId: this.role,
          password: this.password,
          repeatPassword: this.repeatPassword
        })
        .then(response => {
          if (response.data === 'email_already_exists') {
            this.$toasted.global.toasted_error({
              message: this.$i18n.translate('email_already_exists')
            });
          } else if (response.data === 'phone_number_already_exists') {
            console.log('this.$toasted:', this.$toasted);
            this.$toasted.global.toasted_error({
              message: this.$i18n.translate('phone_number_already_exists')
            });
          } else if (response.data === 'username_not_valid') {
            this.$toasted.global.toasted_error({
              message: this.$i18n.translate('usernameNotValid')
            });
          } else if (response.data === 'password_not_valid') {
            this.$toasted.global.toasted_error({
              message: this.$i18n.translate('passwordNotValid')
            });
          } else if (response.data === 'role_not_valid') {
            this.$toasted.global.toasted_error({
              message: this.$i18n.translate('roleNotValid')
            });
          }
          this.$toasted.global.toasted_success({
            message: this.$i18n.translate('registration_complete')
          });
        });
    },
    fetchRoles() {
      this.$store.dispatch('loadRoles');
    }
  }
};
</script>
<style></style>
