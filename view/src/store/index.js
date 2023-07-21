import Vue from 'vue';
import Vuex from 'vuex';
import actions from './actions';
import mutations from './mutations';

Vue.use(Vuex);

const state = {
  events: [], // Initial state for events
};

export default new Vuex.Store({
  state,
  actions,
  mutations,
});
