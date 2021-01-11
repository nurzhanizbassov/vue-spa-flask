<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Users</h2>
        </div>
      </div>
    </section>
    <b-table :data="users">
      <template slot-scope="props">
        <b-table-column :label="'id' | translate" field='id'> {{ props.row.id }} </b-table-column>
        <b-table-column :label="'email' | translate" field='email'> {{ props.row.email }} </b-table-column>
        <b-table-column :label="'username' | translate" field='username'> {{ props.row.username }} </b-table-column>
        <b-table-column :label="'phone_number' | translate" field='phone_number'> {{ props.row.phone_number }} </b-table-column>
        <b-table-column :label="'enabled' | translate" field="enabled" centered>
          <b-checkbox v-model="props.row.enabled" @input="addToEdit(props.row)">
          </b-checkbox>
        </b-table-column>
      </template>
    </b-table>

    <b-button type="is-primary is-pulled-right" @click="save" >
      {{ 'save' | translate }}
    </b-button>
  </div>
</template>

<script>

import { mapState } from 'vuex';

export default {
  data () {
    console.log('Users Component loaded');
    return {
      usersToEdit: []
    }
  },
  methods: {
    addToEdit (user) {
      if (!this.usersToEdit.some(item => item.id === user.id)) {
        this.usersToEdit.push(user);
      }
    },
    remove (user) {
      this.$store.dispatch('removeUser', {userId: user.id})
      .then(response => this.$toasted.global.toasted_success({ message: this.$i18n.translate('record_removed') }))
      .catch(() => this.$toasted.global.toasted_error({ message: this.$i18n.translate('action_failed') }));
    },
    save () {
      if (this.usersToEdit.length !== 0) {
        this.$store.dispatch('editUsers', this.usersToEdit)
        .then(response => this.$toasted.global.toasted_success({ message: this.$i18n.translate('records_updated') }));
      } else {
        this.$toasted.global.toasted_warning({ message: this.$i18n.translate('nothing_to_update') });
      }
    }
  },
  computed: {
    ...mapState({
      users: state => state.users
    })
  },
  beforeMount () {
    this.$store.dispatch('loadUsers');
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
