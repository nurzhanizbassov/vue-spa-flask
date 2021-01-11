<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ 'my_games_library' | translate }}</h2>
        </div>
      </div>
    </section>

    <b-table :data="games">
      <template slot-scope="props">
        <b-table-column :label="'id' | translate" field='id'> {{ props.row.id }} </b-table-column>
        <b-table-column :label="'name_en' | translate" field='name_en'> {{ props.row.name_en }} </b-table-column>
        <b-table-column :label="'name_kz' | translate" field='name_kz'> {{ props.row.name_kz }} </b-table-column>
        <b-table-column :label="'name_ru' | translate" field='name_ru'> {{ props.row.name_ru }} </b-table-column>
        <b-table-column :label="'game_type' | translate" field='name_type'> {{
          props.row.game_type.name_en }} </b-table-column>
        <b-table-column :label="'edit' | translate">
          <button class="button is-small is-danger" @click="edit(props.row)">
            <i class="fas fa-pencil-alt"></i>
          </button>
        </b-table-column>
        <b-table-column :label="'remove' | translate">
          <button class="button is-small is-danger" @click="remove(props.row)">
            <i class="fas fa-trash-alt"></i>
          </button>
        </b-table-column>
      </template>
    </b-table>

    <b-button class="is-primary is-pulled-right" @click="add()">
      {{ 'add' | translate }}
    </b-button>
  </div>
</template>

<script>

import { mapState } from 'vuex'

export default {
  computed: mapState({
    games: state => state.games
  }),
  methods: {
    remove (game) {
      // console.log('UAC. Games. remove. game:', game);
      this.$buefy.dialog.confirm({
        title: this.$i18n.translate('remove_record'),
        message: this.$i18n.translate('confirm_removal'),
        confirmText: this.$i18n.translate('remove'),
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () =>
          this.$store.dispatch('removeGame', { gameId: game.id, userId:
            game.user_id })
            .then(response => this.$toasted.global.toasted_success({ message: this.$i18n.translate('record_removed') }))
            .catch(() => this.$toasted.global.toasted_error({ message: this.$i18n.translate('action_failed') }))
      })
    },
    edit (game) {
      this.$router.push({
        name: 'EditGame',
        params: {
          gameToEdit: game
        }
      });
    },
    add () {
      this.$router.push('/games/add');
    }
  },

  beforeMount () {
    this.$store.dispatch('loadGames')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
