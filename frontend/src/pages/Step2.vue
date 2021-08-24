<template>
  <q-page class="design-page column justify-center bg-warning">
    <div class="text-h3 text-bold q-mb-sm q-ml-xl">Design anything</div>
    <div class="text-body1 q-mb-md q-ml-xl">Step 2: Choose the details</div>
    <div class="chooseDesign self-center column text-h5 justify-between">
      <div class="col column justify-around q-ml-xl">
        <div class="q-gutter-sm">
          <div class="text-bold text-h4">Choose type:</div>
          <q-checkbox v-model="male" label="Male" color="accent" />
          <q-checkbox v-model="female" label="Female" color="accent" />
          <q-checkbox v-model="unisex" label="Unisex" color="accent" />

        </div>
        <div>
          <div  class="text-bold text-h4" >Choose size:</div>
          <div class="row items-center q-ma-sm">
            <span class="q-ma-md">XS:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
            <span class="q-ma-md">S:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
            <span class="q-ma-md">M:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
            <span class="q-ma-md">L:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
            <span class="q-ma-md">XL:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
            <span class="q-ma-md">XXL:</span>
            <q-input
              square
              dense
              standout="bg-grey-3"
              v-model="size"
              class="sizeInput"
              :input-style="{ color: '#000000' }"
            />
          </div>
        </div>
        <div>
          <div class="text-bold text-h4">Choose colour:</div>
          <q-btn-toggle
            class="time-btn-toggle justify-center no-border-radius"
            v-model="selected"
            color="primary"
            :toggle-color="selected"
            unelevated
            size="md"
            :options="[
              {
                class: 'q-ma-sm ',
                round: true,
                icon: selected === 'green' ? 'done' : '',
                color: 'green',
                value: 'green',
              },
              {
                class: 'q-ma-sm ',
                round: true,
                icon: selected === 'blue' ? 'done' : '',
                color: 'blue',
                value: 'blue',
              },
              {
                class: 'q-ma-sm ',
                round: true,
                icon: selected === 'yellow' ? 'done' : '',
                color: 'yellow',
                value: 'yellow',
              },
              {
                class: 'q-ma-sm ',
                round: true,
                icon: selected === 'purple' ? 'done' : '',
                color: 'purple',
                value: 'purple',
              },
              {
                class: 'q-ma-sm ',
                round: true,
                icon: selected === 'brown' ? 'done' : '',
                color: 'brown',
                value: 'brown',
              },
            ]"
          />
        </div>
      </div>
      <div class="column">
        <q-btn
          flat
          color="black"
          label="NEXT"
          push
          size="sm"
          v-close-popup
          class="
            no-border-radius
            nextButton
            text-bold
            q-pa-sm q-ma-lg
            col
            self-end
          "
        />
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "DesignStep2",
  components: {},
  setup() {
    return {
      male: ref(true),
      female: ref(false),
      unisex: ref(false),
      size: ref(""),
      selected: ref("yellow"),
    };
  },
});
</script>

<style lang="scss" scoped>
.design-page {
  font-family: raleway;
}
.chooseDesign {
  border-style: solid;
  background-color: white;
  border-width: 6px;
  height: 67vh;
  width: 70%;
}
.designCard {
  width: 100%;
  max-width: 150px;
  border-radius: 20%;
}
.sizeInput {
  border-style: solid;
  border-width: 2px;
  font-family: raleway;
  max-width: 3em;
}
.nextButton {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 3px;
  max-width: 80vw;
  width: 15em;
}
</style>