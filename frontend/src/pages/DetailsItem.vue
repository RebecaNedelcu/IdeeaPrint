<template>
  <q-page class="column justify-end font-page" :style-fn="qpageMinHeight">
    <div class="row product-page-landing">
      <div class="col-12 col-md-5">
        <q-carousel
          animated
          v-model="slide"
          navigation
          infinite
          class="carusel"
          height="100%"
        >
          <q-carousel-slide
            :name="1"
            :img-src="selectedProductIllustration?.image"
          />
        </q-carousel>
      </div>
      <div class="col-12 col-md-7 column justify-center items-center">
        <div class="details-container q-ma-xl">
          <div class="text-h3 text-bold q-mb-md">
            {{ selectedProductIllustration?.product.name }}
          </div>
          <div class="text-body1 details-text">
            printed with love by Ideeaprint
          </div>
          <div class="text-bold text-h5 q-mb-xl q-mt-lg">
            {{ selectedProductIllustration?.product.price }} LEI
          </div>
          <div class="row text-h6">
            <div class="row items-center">
              <span class="q-mr-lg">Size: </span>
              <q-select
                borderless
                v-model="selectedSize"
                :options="sizes"
                dense
                color="secondary"
                class="q-mr-xl"
              />
            </div>
            <div class="row justify-center items-center">
              <span class="q-ml-xl q-mr-sm">Color: </span>
              <div class="row">
                <div
                  class="q-mr-xs items-center justify-center row"
                  v-for="product in productIllustrationsState.productIllustrations"
                  :key="product.id"
                  :style="{
                    background: product.product.color,
                    height: '1em',
                    width: '1em',
                    outline: '1px solid #000',
                  }"
                  @click="selectColor(product.product.color)"
                >
                  <q-icon
                    v-if="selectedColor === product.product.color"
                    name="done"
                    :color="
                      product.product.color === '#FFFFFF' ? 'black' : 'white'
                    "
                  >
                  </q-icon>
                </div>
              </div>
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
              @click="addProductToCart"
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
import { defineComponent, ref, onMounted, watch } from "vue";
import { useProductIllustration } from "../lib/useProductIllustration";
import { useProducts } from "../lib/useProducts";
import { useCart } from "../lib/useCart";
import { useRoute } from "vue-router";
import { ProductIllustration } from "../lib/models/ProductIllustration";
import { Size } from "../components/models";
import { showToast } from "../lib/useToast";

export default defineComponent({
  name: "DetailsItem",
  components: {},
  setup() {
    let route = useRoute();
    const selectedColor = ref("");
    const sizes = ref<Size[]>([]);
    const selectColor = (val: string) => {
      selectedColor.value = val;
    };
    const selectedProductIllustration = ref<ProductIllustration>();
    const updateSelectedProduct = async () => {
      productIllustrationsState.productIllustrations.forEach((element) => {
        if (element.product.color === selectedColor.value) {
          selectedProductIllustration.value =
            productIllustrationsState.productIllustrations[
              productIllustrationsState.productIllustrations.indexOf(element)
            ];
          retrieveProductDetails(
            productIllustrationsState.productIllustrations[
              productIllustrationsState.productIllustrations.indexOf(element)
            ].product.id
          );
        }
      });
    };
    watch(selectedColor, updateSelectedProduct);
    let qty = ref(1);
    function increment() {
      qty.value += 1;
    }
    function decrement() {
      if (qty.value > 1) qty.value -= 1;
    }
    const { state: productIllustrationsState, loadProductIllustrations } =
      useProductIllustration();

    const { getProductDetails } = useProducts();

    const retrieveProductDetails = async (productId: number) => {
      const data = await getProductDetails(productId);
      sizes.value = [];
      selectedSize.value = undefined;
      if (data)
        data.forEach((detail) => {
          if (!sizes.value.includes(detail.size)) {
            sizes.value.push(detail.size);
          }
        });
    };

    onMounted(async () => {
      await loadProductIllustrations(
        parseInt(route.params.productType.toString()),
        parseInt(route.params.illustrationId.toString())
      );
      selectedProductIllustration.value = {} as ProductIllustration;
      selectedColor.value =
        productIllustrationsState.productIllustrations[0]?.product.color;

      try {
        await retrieveProductDetails(
          productIllustrationsState.productIllustrations[0]?.product.id
        );
      } catch (error) {}
    });

    const selectedSize = ref<Size>();

    const { state: cartState, addCartProduct } = useCart();

    const addProductToCart = () => {
      if (selectedProductIllustration.value) {
        if (selectedSize.value) {
          addCartProduct(
            selectedProductIllustration.value.product.id,
            parseInt(route.params.illustrationId.toString()),
            "",
            qty.value,
            selectedProductIllustration.value.product.price,
            selectedProductIllustration.value.product.name,
            sizes.value,
            selectedSize.value,
            selectedProductIllustration.value.image
          );
        } else {
          showToast({ type: "negative", message: "Alege o mărime!" });
        }
      } else {
        showToast({ type: "negative", message: "Alege un produs!" });
      }
    };

    return {
      selected: ref("yellow"),
      slide: ref(1),
      text: ref(""),
      productIllustrationsState,
      selectColor,
      selectedColor,
      selectedProductIllustration,
      qty,
      increment,
      decrement, 
      selectedSize,
      sizes,
      options: ["XS", "S", "M", "L", "XL", "XXL"],
      qpageMinHeight() {
        return { minHeight: "1vh" };
      },
      addProductToCart,
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