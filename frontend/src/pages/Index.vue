<template>
  <q-page class="homePage column items-center justify-center">
    <p class="welcome text-h3 text-bold">Welcome, Rebeca!</p>
    <div class="column bttns-home-div">
      <q-btn
        no-caps
        flat
        color="black"
        label="design"
        class="no-border-radius buttonsBrdr q-my-sm q-py-sm text-bold text-h6"
        to="/design"
      />
      <q-btn
        no-caps
        flat
        color="black"
        label="shop"
        class="no-border-radius buttonsBrdr q-my-sm q-py-sm text-bold text-h6"
        to="/shop/1"
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageIndex",
  components: {},
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
.homePage {
  background-image: url("../assets/rbk-licenta2.png");
  background-position: center;
  background-size: cover;
  border-style: solid;
  border-width: 6px;
  margin-left: 7%;
  margin-right: 7%;
}
.buttonsBrdr {
  border-style: solid;
  border-width: 6px;
  background-color: $accent;
}
.bttns-home-div {
  max-width: 80vw;
  width: 25em;
  //margin-top: 20%;
  font-family: raleway;
}
.welcome {
  margin-top: 17%;
  margin-bottom: 7%;
  font-family: raleway;
}
</style>