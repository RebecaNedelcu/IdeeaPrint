<template>
  <q-slide-item @left="onLeft">
    <template v-slot:left>
      <q-icon name="done" />
    </template>
    <q-item class="item-design row q-pa-sm">
      <q-item-section class="col-5">
        <q-img :src="cartProduct.image" />
      </q-item-section>
      <q-item-section class="col-7">
        <div class="column">
          <span>{{ cartProduct.name }}</span>
          <span class="text-bold q-mt-xs">{{ cartProduct.price }} LEI</span>
          <div class="row items-center">
            <span class="text-subtitle2 q-mr-sm">Size: </span>
            <q-select
              borderless
              v-model="cartProduct.selectedSize"
              :options="options"
              dense
              color="secondary"
            />
          </div>
          <div class="row items-center">
            <span class="text-subtitle2 q-mr-sm">Qty: </span>
            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-minus"
              size="xs"
              @click="decrement"
            />
            <span class="text-subtitle2 q-px-sm">{{
              cartProduct.quantity
            }}</span>

            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-plus"
              size="xs"
              @click="increment"
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
              @click="removeFromCart"
            />
          </div>
        </div>
      </q-item-section>
    </q-item>
  </q-slide-item>
</template>

<script lang="ts">
import { ref, defineComponent, PropType } from "vue";
import { CartProduct } from "../lib/models/CartProduct";
import { useCart } from "../lib/useCart";
export default defineComponent({
  name: "CartItemComponent",
  props: {
    cartProduct: {
      type: Object as PropType<CartProduct>,
      required: true,
    },
  },
  setup(props) {
    const {
      state: cartState,
      removeCartProduct,
      incrementQuantity,
      decrementQuantity,
    } = useCart();
    let removeFromCart = () => {
      removeCartProduct(cartState.cartProducts.indexOf(props.cartProduct));
    };
    let increment = () => {
      incrementQuantity(cartState.cartProducts.indexOf(props.cartProduct));
    };
    let decrement = () => {
      decrementQuantity(cartState.cartProducts.indexOf(props.cartProduct));
    };

    let onLeft = ({ reset }: any) => {
      removeFromCart();
    };
    return {
      removeFromCart,
      increment,
      decrement,
      onLeft,
      options: props.cartProduct.sizes,
    };
  },
});
</script>

<style lang="scss" scoped>
</style>