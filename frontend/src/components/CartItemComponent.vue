<template>
  <q-slide-item @left="onLeft">
    <template v-slot:left>
      <q-icon name="done" />
    </template>
    <q-item class="item-design row q-pa-sm">
      <q-item-section class="col-5">
        <q-img :src="product.image" />
      </q-item-section>
      <q-item-section class="col-7">
        <div class="column">
          <span>{{product.name}}</span>
          <span class="text-bold q-mt-xs">{{product.price}} LEI</span>
          <div class="row items-center">
            <span class="text-subtitle2 q-mr-sm">Size: </span>
            <q-select
              borderless
              v-model="product.size"
              :options="options"
              dense
              color="secondary"
            />
          </div>
          <div class="row items-center">
            <span class="text-subtitle2  q-mr-sm">Qty: </span>
            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-minus"
              size="xs"
              @click=" if (product.quantity > 1) product.quantity -= 1;"
            />
            <span class="text-subtitle2 q-px-sm">{{ product.quantity }}</span>

            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-plus"
              size="xs"
              @click="product.quantity += 1"
            />
          </div>
          <div class="column items-end">
            <q-btn
              flat
              size="xs"
              class="deleteBtn q-mr-md"
              round
              color="secondary"
              icon="far fa-trash-alt"
            />
          </div>
        </div>
      </q-item-section>
    </q-item>
  </q-slide-item>
</template>

<script lang="ts">
import { ref, defineComponent, PropType } from "vue";
import { CartProduct } from "./models";

export default defineComponent({
  name: "CartItemComponent",
  props: {
    product: {
      type: Object as PropType<CartProduct>,
      required: true,
    },
  },
  setup() {
      function increment(product:CartProduct) {
        product.quantity += product.quantity+1;
      };
      function decrement(product:CartProduct) {
        if (product.quantity > 1) product.quantity -= 1;
      };
    return {
      onLeft() {},
      options: ["XS", "S", "M", "L", "XL", "XXL"],
    };
  },
});
</script>

<style lang="scss" scoped>
</style>