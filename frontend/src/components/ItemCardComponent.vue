<template>
  <q-card flat square class="product-card q-ma-xl" q-hoverable>
    <div class="product-card-container">
      <q-img
        :src="product.product_images[0].image"
        class="product-img"
        ratio="1"
      >
      </q-img>

      <div class="card-overlay"></div>
    </div>
    <q-btn
      flat
      round
      class="fav-btn"
      color="secondary"
      size="md"
      :icon="favBtnIcon ? 'fas fa-heart' : 'far fa-heart'"
      @click="toggleFavoriteProduct"
    />

    <q-card-section class="q-px-none">
      <div class="row">
        <div
          class="col-9 row card-text text-subtitle1 justify-start product-name"
        >
          {{ product.product.illustration.name }}
        </div>
        <div class="col-3 row card-text text-subtitle1 text-bold justify-end">
          {{ product.price.toString().split('.')[0] }} LEI
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { ref, defineComponent, PropType } from "vue";
import { useProducts } from "../lib/useProducts";
import { useUser } from "../lib/useUser";
import { Product } from "./models";

export default defineComponent({
  name: "ItemCard",
  props: {
    product: {
      type: Object as PropType<Product>,
      required: true,
    },
  },
  setup({ product }) {
    const { isProductFavorite, toggleFavoriteProduct } = useUser();
    const favBtnIcon = ref(isProductFavorite(product.id));
    const addToFav = () => {
      favBtnIcon.value = !favBtnIcon.value;
      toggleFavoriteProduct
    };
    return {
      addToFav,
      favBtnIcon,
      toggleFavoriteProduct
    };
  },
});
</script>

<style lang="scss" scoped>
.product-card {
  max-width: 262px;
  height: 350px;
}
.product-card-container {
  position: relative;
}
.card-overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  background-color: $accent;
  transition: 0.2s ease;
}
.product-card-container:hover {
  color: $accent;
}
.product-card-container:hover .card-overlay {
  opacity: 0.6;
}
.product-img {
  border-style: solid;
  border-width: 6px;
  height: 335px;
}
.product-name {
  text-transform: uppercase;
}
.fav-btn {
  border-style: solid;
  border-width: 3px;
  background-color: white;
  position: absolute;
  bottom: 8%;
  right: 10%;
}
.card-text {
  font-family: raleway;
  word-wrap: break-word;
}
</style>
