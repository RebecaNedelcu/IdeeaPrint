<template>
  <q-page class="column justify-end font-page" :style-fn="qpageMinHeight">
    <div class="row product-page-landing">
      <div class="col-12 col-md-5">
        <q-carousel
          animated
          v-model="slide"
          arrows
          navigation
          infinite
          class="carusel"
          height="100%"
        >
          <q-carousel-slide :name="1" img-src="../assets/t-quarantini.png" />
          <q-carousel-slide :name="2" img-src="../assets/t-quarantini2.jpg" />
          <q-carousel-slide
            :name="3"
            img-src="https://cdn.quasar.dev/img/parallax2.jpg"
          />
          <q-carousel-slide
            :name="4"
            img-src="https://cdn.quasar.dev/img/quasar.jpg"
          />
        </q-carousel>
      </div>
      <div class="col-12 col-md-7 column justify-center items-center">
        <div class="details-container q-ma-xl">
          <div class="text-h3 text-bold q-mb-md">QUARANTINI T-SHIRT</div>
          <div class="text-body1 details-text">
            100% cotton, printed with love by Ideeaprint 
          </div>
          <div class="text-bold text-h5 q-mb-xl q-mt-lg">50 LEI</div>
          <div class="row text-h6">
            <div class="row items-center">
              <span class="q-mr-lg">Size: </span>
              <q-select
                borderless
                v-model="model"
                :options="options"
                dense
                color="secondary"
                class="q-mr-xl"
              />
            </div>
            <div>
              <span class="q-ml-xl">Colour: </span>
              <q-btn-toggle
                class=" justify-center no-border-radius"
                v-model="selected"
                color="primary"
                :toggle-color="selected"
                unelevated
                size="xs"
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
          <q-separator
            size="2px"
            color="secondary"
            class="q-my-none separator"
          />
          <div class="row items-center justify-between q-my-xs separator">
            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-minus"
              size="sm"
              @click="decrement"
            />
            <span class="text-h6 text-bold q-px-xl">{{ qty }}</span>

            <q-btn
              flat
              round
              color="secondary"
              icon="fas fa-plus"
              size="sm"
              @click="increment"
            />
          </div>
          <div class="column">
            <q-btn
              flat
              color="black"
              label="ADD TO CART"
              push
              size="lg"
              v-close-popup
              class="no-border-radius addToCartButton text-bold q-mt-md"
            />
            <q-btn
              flat
              color="black"
              label="ADD TO FAVORITES"
              push
              size="lg"
              v-close-popup
              class="no-border-radius addToFavoritesButton text-bold q-mt-md"
            />
          </div>
           <div class="column q-mt-xl items-start justify-end">
          <q-btn flat color="dark" label="FREE RETURN" icon="unarchive" />
          <q-btn
            flat
            color="dark"
            label="FREE DELIVERY OVER 299 LEI"
            icon="local_shipping"
          />
          <q-btn
            flat
            color="dark"
            label="PRODUCT MAINTENANCE"
            icon="local_laundry_service"
          />
        </div>
        </div>
       
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "DetailsItem",
  components: {},
  setup() {
    function useQtySelect() {
      let qty = ref(1);
      function increment() {
        qty.value += 1;
        return qty.value;
      }
      function decrement() {
        if (qty.value > 1) qty.value -= 1;
        return qty.value;
      }
      return { qty, increment, decrement };
    }
    return {
      selected: ref("yellow"),
      slide: ref(1),
      text: ref(""),
      ...useQtySelect(),
      model: ref(null),
      options: ["XS", "S", "M", "L", "XL", "XXL"],
      qpageMinHeight() {
        return { minHeight: "1vh" };
      },
    };
  },
});
</script>

<style lang="scss" scoped>
.product-page-landing {
  height: 85vh;
  width: 100%;
}
.font-page {
  font-family: raleway;
}
.details-text {
  word-wrap: break-word;
}
.addToCartButton {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 6px;
  max-width: 80vw;
  width: 23em;
}
.addToFavoritesButton {
  border-style: solid;
  background-color: white;
  border-width: 6px;
  max-width: 80vw;
  width: 23em;
}

.separator {
  max-width: 80vw;
  width: 33em;
}
</style>