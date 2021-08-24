<template>
  <q-page class="profilePage row">
    <div
      class="col-12 col-md-auto column justify-center q-pa-xl"
      style="width: 25em"
    >
      <q-list bordered padding class="text-secondary text-bold profileMenu">
        <q-item
          clickable
          v-ripple
          :active="link === 'settings'"
          @click="link = 'settings'"
          active-class="my-menu-link"
        >
          <q-item-section>SETTINGS</q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="link === 'changePassword'"
          @click="link = 'changePassword'"
          active-class="my-menu-link"
        >
          <q-item-section>CHANGE PASSWORD</q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="link === 'history'"
          @click="link = 'history'"
          active-class="my-menu-link"
        >
          <q-item-section>ORDER HISTORY</q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="link === 'faq'"
          @click="link = 'faq'"
          active-class="my-menu-link"
        >
          <q-item-section>FAQ</q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="link === 'logout'"
          @click="link = 'logout'"
          active-class="my-menu-link"
        >
          <q-item-section>LOGOUT</q-item-section>
        </q-item>
      </q-list>
    </div>

    <div class="col column q-pa-xl">
      <div v-if="link === 'settings'" class="col">
        <div class="row bg-accent q-pa-md q-pl-xl text-bold text-body1">
          ACCOUNT SETTINGS
        </div>
        <div class="column q-my-lg divInputsContainer">
          <div class="row">
            <q-input
              square
              standout="bg-grey-3"
              v-model="firstname"
              placeholder="First name"
              class="borderLabel q-mt-sm q-mr-xs col"
              :input-style="{ color: '#000000' }"
            />
            <q-input
              square
              standout="bg-grey-3"
              v-model="firstnameCo"
              placeholder="Last name"
              class="borderLabel q-mt-sm q-ml-xs col"
              :input-style="{ color: '#000000' }"
            />
          </div>
          <div class="row">
            <q-input
              square
              standout="bg-grey-3"
              v-model="lastnameCo"
              placeholder="Telephone"
              class="borderLabel q-mt-sm q-mr-xs col"
              :input-style="{ color: '#000000' }"
            />
            <q-input
              square
              standout="bg-grey-3"
              v-model="companyCo"
              placeholder="Company"
              class="borderLabel q-mt-sm q-ml-xs col"
              :input-style="{ color: '#000000' }"
            />
          </div>
          <div class="col">
            <q-input
              square
              standout="bg-grey-3"
              v-model="streetCo"
              placeholder="Street adress"
              class="borderLabel q-mt-sm q-px-none streetInput"
              :input-style="{ color: '#000000' }"
            />
          </div>
          <div class="row">
            <q-input
              square
              standout="bg-grey-3"
              v-model="cityCo"
              placeholder="City"
              class="borderLabel q-mt-sm q-mr-xs col"
              :input-style="{ color: '#000000' }"
            />
            <q-input
              square
              standout="bg-grey-3"
              v-model="zipcodeCo"
              placeholder="Zip Code"
              class="borderLabel q-mt-sm q-ml-xs col"
              :input-style="{ color: '#000000' }"
            />
          </div>
          <div class="row">
            <q-input
              square
              standout="bg-grey-3"
              v-model="countyCo"
              placeholder="County"
              class="borderLabel q-mt-sm q-mr-xs col"
              :input-style="{ color: '#000000' }"
            />
            <q-input
              square
              standout="bg-grey-3"
              v-model="countryCo"
              placeholder="Country"
              class="borderLabel q-mt-sm q-ml-xs col"
              :input-style="{ color: '#000000' }"
            />
          </div>
        </div>
        <div class="row justify-center q-my-xl">
          <q-btn
            no-caps
            flat
            color="black"
            label="SAVE CHANGES"
            class="no-border-radius buttonsBrdr text-bold text-body1"
          />
        </div>
      </div>
      <div v-if="link === 'changePassword'" class="column">
        <div class="row bg-accent q-pa-md q-pl-xl text-bold text-body1">
          CHANGE PASSWORD
        </div>

        <div class="column q-my-lg divInputsContainer">
          <div class="column">
            <q-input
              standout="bg-grey-3 text-black"
              v-model="password"
              :type="isPwd ? 'password' : 'text'"
              placeholder="Old password"
              class="borderLabel"
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
              v-model="password"
              :type="isPwd ? 'password' : 'text'"
              placeholder="New password"
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
              v-model="password"
              :type="isPwd ? 'password' : 'text'"
              placeholder="Confirm new password"
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
          </div>
          <div class="column justify-center q-my-xl">
            <q-btn
              no-caps
              flat
              color="black"
              label="SAVE"
              class="
                no-border-radius
                buttonsBrdr
                text-bold text-body1
                col
                self-center
                q-mt-lg
              "
            />
          </div>
        </div>
      </div>

      <div v-if="link === 'history'" class="column">
        <div class="row bg-accent q-pa-md q-pl-xl text-bold text-body1">
          MY ORDERS
        </div>

        <q-expansion-item class="orderContainer q-mt-xl ">
            
          <template v-slot:header>
            <div class="row bg-primary items-center text-body1 orderContainerDetails ">
              <div class="column items-center q-mx-xl">
                <span class="text-bold">DELIVERD</span>
                <span class="text-body2"> 5 items </span>
              </div>

              <div class="column items-center q-mx-xl">
                <div class="text-bold">05/08/2021</div>
                <div class="text-body2">159 LEI</div>
              </div>
            </div>
          </template>
          
          <q-card>
            <q-card-section>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem,
              eius reprehenderit eos corrupti commodi magni quaerat ex numquam,
              dolorum officiis modi facere maiores architecto suscipit iste
              eveniet doloribus ullam aliquid.
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </div>
      <div v-if="link === 'changepassword'" class="column">changeplm</div>
      <div v-if="link === 'faq'" class="column">PAGINA DE FAQ</div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageIndex",
  components: {},
  setup() {
    return {
      link: ref("settings"),
      showpswd: ref(false),
      password: ref(""),
      isPwd: ref(true),
    };
  },
});
</script>

<style lang="scss" scoped>
.profilePage {
  font-family: raleway;
}

.my-menu-link {
  color: white;
  background: $info;
}
.profileMenu {
  border-style: solid;
  border-width: 6px;
  border-color: black;
}

.borderLabel {
  border-style: solid;
  border-width: 2px;
  font-family: raleway;
  // max-width: 40em;
}
.buttonsBrdr {
  border-style: solid;
  border-width: 4px;
  background-color: $accent;
}

.divInputsContainer {
  width: 50em;
  margin-left: auto;
  margin-right: auto;
}
.orderContainer {
  border-style: solid;
  border-width: 2px;
  border-color: black;
}

</style>