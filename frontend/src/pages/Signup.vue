<template>
  <q-page class="column items-center justify-center" :style-fn="qpageMinHeight">
    <div>
      <q-input
        square
        standout="bg-grey-3"
        v-model="firstName"
        placeholder="first name"
        class="borderLabel q-mt-sm"
        :input-style="{ color: '#000000' }"
      />
      <q-input
        square
        standout="bg-grey-3"
        v-model="lastName"
        placeholder="last name"
        class="borderLabel q-mt-sm"
        :input-style="{ color: '#000000' }"
      />
      <q-input
        square
        standout="bg-grey-3"
        v-model="email"
        placeholder="email"
        class="borderLabel q-mt-sm"
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
      <q-input
        standout="bg-grey-3 text-black"
        v-model="password2"
        :type="isPwd ? 'password' : 'text'"
        placeholder="confirm password"
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

      <q-btn
        no-caps
        flat
        @click="onRegisterClick"
        color="black"
        label="CREATE ACCOUNT"
        class="
          no-border-radius
          brdrButtons
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
          brdrButtons
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
import { showToast } from "../lib/useToast";
import { useUser } from "../lib/useUser";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "PageSignUp",
  components: {},
  setup() {
    const { register, login } = useUser();
    const router = useRouter();

    const firstName = ref("");
    const lastName = ref("");
    const email = ref("");
    const password = ref("");
    const password2 = ref("");

    const onRegisterClick = async () => {
      try {
        const { error } = await register(
          email.value,
          password.value,
          firstName.value,
          lastName.value
        );
        if (error) {
          showToast({ type: "negative", message: error });
          return;
        }
        await login(email.value, password.value)
        showToast({ type: "positive", message: "Logged in" });
        router.push("/");
      } catch (error) {}
    };

    return {
      onRegisterClick,
      firstName,
      lastName,
      email,
      password,
      password2,
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
.brdrButtons {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 6px;
  width: 20em;

  font-family: raleway;
}
.marginBtn {
  margin-top: 10%;
}
.marginRemember {
  margin-left: 60px;
  font-family: raleway;
}
</style>