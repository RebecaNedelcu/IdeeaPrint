<template>
  <q-card flat square class="product-card q-ma-xl" q-hoverable>
    <div class="product-card-container">
      <q-img :src="illustration.image" class="product-img" ratio="1"> </q-img>

      <div class="card-overlay"></div>
    </div>
    <q-btn
      flat
      round
      class="fav-btn"
      color="secondary"
      size="md"
      :icon="
        isIllustrationFavorite(illustration.id)
          ? 'fas fa-heart'
          : 'far fa-heart'
      "
      @click="onHeartClick"
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
import { ref, defineComponent, PropType, onMounted } from "vue";
import { Illustration } from "../lib/models/Illustration";
import { useUser } from "../lib/useUser";
import { showToast } from "../lib/useToast";

export default defineComponent({
  name: "ItemCard",
  props: {
    illustration: {
      type: Object as PropType<Illustration>,
      required: true,
    },
  },
  setup({ illustration }) {
    const {
      isIllustrationFavorite,
      toggleFavoriteIllustrations,
      state: userState,
    } = useUser();

    const onHeartClick = () => {
      if (!userState.user.isLoggedIn) {
        showToast({ type: "negative", message: "You are not logged in!" });
      } else {
        toggleFavoriteIllustrations(illustration.id);
      }
    };

    return {
      onHeartClick,
      isIllustrationFavorite,
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
