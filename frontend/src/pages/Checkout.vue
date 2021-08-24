<template>
  <div class="q-pa-md fontAll">
    <q-stepper
      v-model="step"
      header-nav
      ref="stepper"
      color="secondary"
      animated
      done-color="info"
      active-color="accent"
      inactive-color="secondary"
    >
      <q-step :name="1" title="DELIVERY" icon="local_shipping" :done="done1">
        <div class="text-h3 column items-center text-bold">
          Shipping information
        </div>
        <div class="column allInput q-my-xl">
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

        <q-stepper-navigation class="row justify-between q-mx-xl">
          <q-btn
            flat
            @click="step = 1"
            color="secondary"
            label="Back to Shopping"
          />
          <q-btn
            @click="
              () => {
                done1 = true;
                step = 2;
              }
            "
            label="Proceed to Payment"
            class="continueBtn no-border-radius"
          />
        </q-stepper-navigation>
      </q-step>

      <q-step :name="2" title="PAYMENT" icon="savings" :done="done2">
        <div class="text-h3 column items-center text-bold">Payment details</div>
        <div class="text-bold text-h4 column items-center q-mt-md">
          <q-option-group
            v-model="group"
            :options="options"
            color="accent"
            inline
            size="140px"
          />
          <div class="text-body1">Delivery between 2-5 work days.</div>
        </div>
        <div v-if="group==='op-card'" class="column allInput q-my-lg">
          <q-input
            square
            standout="bg-grey-3"
            v-model="cardholderCo"
            placeholder="Cardholder Name"
            class="borderLabel q-mt-sm q-ml-xs col"
            :input-style="{ color: '#000000' }"
          />
          <q-input
            mask="#### #### #### ####"
            square
            standout="bg-grey-3"
            v-model="cardnumberCo"
            placeholder="Card Number"
            class="borderLabel q-mt-sm q-ml-xs col"
            :input-style="{ color: '#000000' }"
          />
          <div class="row justify-between">
            <div class="row items-center col-7">
              <span class="text-bold q-mr-xl text-h6"> EXPIRATION DATE</span>
              <q-input
                square
                mask="##/##"
                placeholder="MM/YY"
                standout="bg-grey-3"
                v-model="dateCo"
                class="borderLabel q-mt-sm col"
                :input-style="{ color: '#000000' }"
              />
            </div>
            <q-input
              mask="###"
              square
              standout="bg-grey-3"
              v-model="cvvCo"
              placeholder="CVV"
              class="borderLabel q-mt-sm col-2"
              :input-style="{ color: '#000000' }"
            />
          </div>
        </div>
        <q-stepper-navigation class="row justify-between q-mx-xl">
          <q-btn
            flat
            @click="step = 1"
            color="secondary"
            label="Back"
            class="q-ml-sm"
          />
          <q-btn
            @click="
              () => {
                done2 = true;
                step = 3;
              }
            "
            label="Finish"
            class="continueBtn no-border-radius"
          />
        </q-stepper-navigation>
      </q-step>
      <q-step :name="3" title="STATUS" icon="pending" :done="done3">
          <div class="column items-center text-h3 text-bold">THANK YOU FOR YOUR ORDER!</div>
          <div class="column items-center text-bold text-h4 q-mt-xl">STATUS:</div>
          <div class="column items-center text-bold text-h3 q-mb-xl q-mt-sm">DELIVERD</div>
        <q-stepper-navigation class="row justify-end q-mx-xl">
          <q-btn  @click="done3 = true" label="Done" class="continueBtn no-border-radius " />
          
        </q-stepper-navigation>
      </q-step>
    </q-stepper>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "PageCheckout",
  components: {},
  setup() {
    const step = ref(1);
    const done1 = ref(false);
    const done2 = ref(false);
    const done3 = ref(false);
    return {
      step,
      done1,
      done2,
      done3,

      reset() {
        done1.value = false;
        done2.value = false;
        done3.value = false;
        step.value = 1;
      },
      firstnameCo: ref(""),
      lastnameCo: ref(""),
      telephonenameCo: ref(""),
      companyCo: ref(""),
      streetCo: ref(""),
      cityCo: ref(""),
      zipcodeCo: ref(""),
      countyCo: ref(""),
      countryCo: ref(""),

      group: ref("op-card"),

      options: [
        {
          label: "Cash",
          value: "op-cash",
        },
        {
          label: "Credit Card ",
          value: "op-card",
        },
      ],
    };
  },
});
</script>

<style lang="scss" scoped>
.fontAll {
  font-family: raleway;
}
.borderLabel {
  border-style: solid;
  border-width: 2px;
  font-family: raleway;
  // max-width: 40em;
}
.allInput {
  max-width: 70em;
  margin-left: auto;
  margin-right: auto;
}
.continueBtn {
  border-style: solid;
  border-width: 4px;
  background-color: $accent;
}
</style>