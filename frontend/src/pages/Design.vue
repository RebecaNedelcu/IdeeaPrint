<template>
  <q-page class="design-page column justify-center bg-warning">
    <div class="text-h3 text-bold q-mb-sm q-ml-xl">Design anything</div>
    <div class="text-body1  q-mb-md q-ml-xl">Step 1: Choose what would you like to personalize</div>
    <div class="chooseDesign self-center">
      <div class="row justify-center">
      <q-card class="designCard bg-accent column items-center q-ma-md">
        <img src="../assets/tshirt.png" class="q-px-lg q-py-sm" />

        <q-card-section class="q-py-sm">
          <div class="text-body2 text-bold">T-shirt</div>
        </q-card-section>
      </q-card>
      <q-card class="designCard bg-accent column items-center q-ma-md">
        <img src="../assets/hoodie.png" class="q-px-lg q-py-sm" />

        <q-card-section class="q-py-sm">
          <div class="text-body2 text-bold">Hoodie</div>
        </q-card-section>
      </q-card>
      <q-card class="designCard bg-accent column items-center q-ma-md">
        <img src="../assets/mug.png" class="q-px-lg q-py-sm" />

        <q-card-section class="q-py-sm">
          <div class="text-body2 text-bold">Mug</div>
        </q-card-section>
      </q-card>
      <q-card class="designCard bg-accent column items-center q-ma-md">
        <img src="../assets/totebag.png" class="q-px-lg q-py-sm" />

        <q-card-section class="q-py-sm">
          <div class="text-body2 text-bold">Totebag</div>
        </q-card-section>
      </q-card>
      
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
  name: "Design",
  components: {},
  setup() {
    return {};
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
.nextButton {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 3px;
  max-width: 80vw;
  width: 15em;
}
</style>