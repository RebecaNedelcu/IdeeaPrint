<template>
  <q-layout>
    <q-btn dense flat round icon="close" @click="hasHistory() ? $router.go(-1) : $router.push('/')" class="x" size="30px" />

    <div class="auth-buttons-container">
      <div class="auth-each-btn-container">
        <router-link
          to="/signup"
          class="btn-auth"
          exact-active-class="btn-auth-active"
        >
          sign up
        </router-link>
      </div>
      <div class="auth-each-btn-container">
        <router-link
          to="/signin"
          class="btn-auth"
          exact-active-class="btn-auth-active"
        >
          sign in
        </router-link>
      </div>
    </div>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "AuthLayout",

  components: {},

  setup() {
    return {hasHistory() {
        return window.history.length > 2;
      },};
  },
});
</script>

<style lang="scss" scoped>
.x {
  position: absolute;
  right: 80px;
  top: 45px;
}
a {
  color: #000000;
  text-decoration: none;
}
.auth-buttons-container {
  font-family: raleway;
  font-style: normal;
  font-weight: bold;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  text-transform: lowercase;
  color: #000000;

  display: block;
  margin-left: auto;
  margin-right: auto;
}
.auth-each-btn-container {
  display: inline-flex;
}
.btn-auth {
  background: #ffffff;
  border: 5px solid #000000;
  box-sizing: border-box;
  border-radius: 14px;
  margin: 2em 1em 0.5em 1em;
  padding: 10px 50px;
  transition: all 0.1s ease;
  transition-property: color, border-color;
}
.btn-auth:hover {
  color: #c6b9ff;
  border-color: #c6b9ff;
}
.btn-auth-active {
  background: #ffffff;
  border-style: solid;
  border-color: #000000;
  border-width: 5px 5px 10px 5px;
  box-sizing: border-box;
  border-radius: 14px;
}
</style>
