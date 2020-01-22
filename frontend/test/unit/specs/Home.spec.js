import Vue from 'vue'
import Home from '@/components/Home'

// TODO: Need to fix this test. A key 'app_title'
// gets returend instead of text 'Some Web App'.
describe('Home.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Home)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.title').textContent)
      .toEqual('Some Web App')
  })
})
