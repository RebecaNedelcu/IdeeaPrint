<template>
  <q-card flat square class="product-card q-ma-xl" q-hoverable>
    <div class="product-card-container">
      <q-img
        :src="illustration.image"
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
    />

    <q-card-section class="q-px-none">
      <div class="row">
        <div
          class="col-9 row card-text text-subtitle1 justify-start product-name"
        >
          {{ illustration.name }}
        </div>
        <div class="col-3 row card-text text-subtitle1 text-bold justify-end">
          <!-- {{ product.price.toString().split('.')[0] }} LEI -->
          de la 50LEI
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { ref, defineComponent, PropType } from "vue";
// import { useProducts } from "../lib/useProducts";
import { useUser } from "../lib/useUser";
import { Illustration } from "./models";

export default defineComponent({
  name: "ItemCard",
  props: {
    illustration: {
      type: Object as PropType<Illustration>,
      required: true,
    },
  },
  setup({ illustration }) {
    const { isProductFavorite } = useUser();
    // const favBtnIcon = ref(isProductFavorite(illustration.id));
     const favBtnIcon = ref(true);

    // const addToFav = () => {
    //   favBtnIcon.value = !favBtnIcon.value;
      //changePrice(illustration.id);
    // };
    //const { changePrice } = useProducts();
    return {
      //addToFav,
      favBtnIcon,
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
