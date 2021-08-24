<template>
  <q-page class="column items-center" :style-fn="qpageMinHeight">
    <div>
      <q-input
        square
        standout="bg-grey-3"
        v-model="email"
        placeholder="email"
        class="borderLabel q-mt-xl"
        :input-style="{ color: '#000000' }"
      />
      <q-input
        standout="bg-grey-3 text-black"
        v-model="password"
        :type="isPwd ? 'password' : 'text'"
        placeholder="password"
        class="borderLabel q-mt-sm"
        :input-style="{ color: '#000000' }"
      >
        <template v-slot:append>
          <q-icon
            color="accent"
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>
      <q-checkbox
        size="xs"
        v-model="teal"
        label="Remember me"
        color="accent"
        class="marginRemember"
      />

      <q-btn
        no-caps
        flat
        color="black"
        label="LOG IN"
        class="
          no-border-radius
          borderButtons
          text-bold text-h6
          column
          bttns-home
          marginBtn
        "
      />
      <q-btn
        no-caps
        flat
        color="black"
        label="SIGN UP WITH GOOGLE"
        class="
          no-border-radius
          borderButtons
          text-bold text-h6
          column
          bttns-home
          q-mt-sm
        "
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageSignIn",
  components: {},
  setup() {
    return {
      email: ref(""),
      password: ref(""),
      isPwd: ref(true),
      teal: ref(true),
      qpageMinHeight() {
        return { minHeight: "1vh" };
      },
    };
  },
});
</script>

<style lang="scss" scoped>
.borderLabel {
  border-style: solid;
  border-width: 2px;
  font-family: raleway;
  max-width: 19em;
  margin-left: auto;
  margin-right: auto;
}
.borderButtons {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 6px;
  width: 20em;

  font-family: raleway;
}
.marginBtn {
  margin-top: 20%;
}
.marginRemember {
  margin-left: 60px;
  font-family: raleway;
}
</style>