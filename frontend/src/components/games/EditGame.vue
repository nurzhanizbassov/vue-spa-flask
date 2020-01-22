<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ 'add_game' | translate }}</h2>
        </div>
      </div>
    </section>

    <section class="section">
      <form id="edit-game-form" @submit="save">
        <div class="container">
          <b-field
            :label="'name_en' | translate"
            :type="nameEnStyleType"
            :custom-class="nameEnCustomClass"
            :message="nameEnErrorMessage"
          >
            <b-input
              id="name-en"
              name="name-en"
              v-model.trim="$v.nameEn.$model"
              @focus="$v.nameEn.$touch"
              type="text"
            ></b-input>
          </b-field>
          <b-field
            :label="'name_kz' | translate"
            :type="nameKzStyleType"
            :custom-class="nameKzCustomClass"
            :message="nameKzErrorMessage"
          >
            <b-input
              id="name-kz"
              name="name-kz"
              v-model.trim="$v.nameKz.$model"
              @focus="$v.nameKz.$touch"
              type="text"
            ></b-input>
          </b-field>
          <b-field
            :label="'name_ru' | translate"
            :type="nameRuStyleType"
            :custom-class="nameRuCustomClass"
            :message="nameRuErrorMessage"
          >
            <b-input
              id="name-ru"
              name="name-ru"
              v-model.trim="$v.nameRu.$model"
              @focus="$v.nameRu.$touch"
              type="text"
            ></b-input>
          </b-field>
          <b-field
            :label="'game_type' | translate"
            :type="gameTypeStyleType"
            :custom-class="gameTypeCustomClass"
            :message="gameTypeErrorMessage"
          >
            <b-select
              :placeholder="'select_game_type' | translate"
              id="game-type"
              name="game-type"
              expanded
              v-model.trim="$v.gameType.$model"
              @focus="$v.gameType.$touch"
            >
              <option v-for="gameType in gameTypes" :value="gameType.id" :key="gameType.id">
                <p v-if="currentLanguage == 'en'">{{ gameType.name_en }}</p>
                <p v-if="currentLanguage == 'kz'">{{ gameType.name_kz }}</p>
                <p v-if="currentLanguage == 'ru'">{{ gameType.name_ru }}</p>
              </option>
            </b-select>
          </b-field>
          <b-button
            type="is-primary"
            id="save-button"
            :disabled="!formValid"
            @click.prevent="save()"
          >{{ 'save' | translate }}</b-button>
          <b-button
            type="is-primary"
            id="back-button"
            @click.prevent="back()"
          >{{ 'back' | translate }}</b-button>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { required } from 'vuelidate/lib/validators';
import { singleErrorExtractorMixin } from 'vuelidate-error-extractor';

export default {
  props: {
    gameToEdit: Object
  },
  data() {
    return {
      id: this.$props.gameToEdit.id,
      nameKz: this.$props.gameToEdit.name_kz,
      nameRu: this.$props.gameToEdit.name_ru,
      nameEn: this.$props.gameToEdit.name_en,
      gameType: this.$props.gameToEdit.game_type_id,
      errorMsg: ''
    };
  },
  validations: {
    nameKz: {
      required
    },
    nameRu: {
      required
    },
    nameEn: {
      required
    },
    gameType: {
      required
    }
  },
  created() {
    this.fetchGameTypes();
  },
  extends: singleErrorExtractorMixin,
  computed: {
    ...mapState({
      gameTypes: state => state.gameTypes
    }),
    currentLanguage() {
      let l = this.$i18n.locale();
      return l;
    },
    nameKzStyleType() {
      return this.$v.nameKz.$error
        ? 'is-danger'
        : !this.$v.nameKz.$invalid && this.$v.nameKz.$dirty
        ? 'is-success'
        : null;
    },
    nameKzCustomClass() {
      return this.$v.nameKz.$error
        ? 'has-text-danger'
        : !this.$v.nameKz.$invalid && this.$v.nameKz.$dirty
        ? 'has-text-success'
        : null;
    },
    nameKzErrorMessage() {
      if (!this.$v.nameKz.required) {
        return !this.$v.nameKz.required && this.$v.nameKz.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    nameRuStyleType() {
      return this.$v.nameRu.$error
        ? 'is-danger'
        : !this.$v.nameRu.$invalid && this.$v.nameRu.$dirty
        ? 'is-success'
        : null;
    },
    nameRuCustomClass() {
      return this.$v.nameRu.$error
        ? 'has-text-danger'
        : !this.$v.nameRu.$invalid && this.$v.nameRu.$dirty
        ? 'has-text-success'
        : null;
    },
    nameRuErrorMessage() {
      if (!this.$v.nameRu.required) {
        return !this.$v.nameRu.required && this.$v.nameRu.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    nameEnStyleType() {
      return this.$v.nameEn.$error
        ? 'is-danger'
        : !this.$v.nameEn.$invalid && this.$v.nameEn.$dirty
        ? 'is-success'
        : null;
    },
    nameEnCustomClass() {
      return this.$v.nameEn.$error
        ? 'has-text-danger'
        : !this.$v.nameEn.$invalid && this.$v.nameEn.$dirty
        ? 'has-text-success'
        : null;
    },
    nameEnErrorMessage() {
      if (!this.$v.nameEn.required) {
        return !this.$v.nameEn.required && this.$v.nameEn.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    gameTypeStyleType() {
      return this.$v.gameType.$error
        ? 'is-danger'
        : !this.$v.gameType.$invalid && this.$v.gameType.$dirty
        ? 'is-success'
        : null;
    },
    gameTypeCustomClass() {
      return this.$v.gameType.$error
        ? 'has-text-danger'
        : !this.$v.gameType.$invalid && this.$v.gameType.$dirty
        ? 'has-text-success'
        : null;
    },
    gameTypeErrorMessage() {
      if (!this.$v.gameType.required) {
        return !this.$v.gameType.required && this.$v.gameType.$dirty
          ? this.$i18n.translate('field_required')
          : null;
      }
    },
    formValid() {
      return (
        !this.$v.nameEn.$invalid &&
        !this.$v.nameKz.$invalid &&
        !this.$v.nameRu.$invalid &&
        !this.$v.gameType.$invalid
      );
    }
  },
  methods: {
    save () {
      this.$store
        .dispatch('editGame', {
          gameId: this.id,
          nameEn: this.nameEn,
          nameKz: this.nameKz,
          nameRu: this.nameRu,
          gameTypeId: this.gameType
        })
        .then(response => {
          this.$toasted.global.toasted_success({
            message: this.$i18n.translate('record_updated')
          });
        });
    },
    back () {
      this.$router.push('/games');
    },
    fetchGameTypes () {
      this.$store.dispatch('loadGameTypes');
    },
    fetchGame () {
      this.$store.dispatch('fetchGame');
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
