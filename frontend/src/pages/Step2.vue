<template>
  <q-page class="design-page column justify-center bg-warning">
    <div class="text-h3 text-bold q-mb-sm q-ml-xl">Design anything</div>
    <div class="text-body1 q-mb-md q-ml-xl">Step 2: Choose the details</div>
    <div class="chooseDesign self-center column text-h5 justify-between">
      <div class="col column justify-around q-ml-xl">
        <div class="q-gutter-sm">
          <div class="text-bold text-h4">Choose type:</div>
          <q-checkbox disable v-model="male" label="Male" color="accent" />
          <q-checkbox disable v-model="female" label="Female" color="accent" />
          <q-checkbox disable v-model="unisex" label="Unisex" color="accent" />
        </div>
        <div>
          <div class="text-bold text-h4">Choose size:</div>
          <div class="row items-center q-ma-sm">
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="XS"
              label="XS:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('XS')"
            />
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="S"
              label="S:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('S')"
            />
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="M"
              label="M:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('M')"
            />
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="L"
              label="L:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('L')"
            />
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="XL"
              label="XL:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('XL')"
            />
            <q-radio
              v-model="selectedSize"
              size="xl"
              val="XXL"
              label="XXL:"
              left-label
              keep-color
              color="secondary"
              :disable="sizeIncluded('XXL')"
            />
          </div>
        </div>
        <div>
          <div class="text-bold text-h4">Choose color:</div>
          <div class="row">
            <div
              class="q-mr-xs items-center justify-center row"
              v-for="product in products"
              :key="product.id"
              :style="{
                background: product.color,
                height: '1em',
                width: '1em',
                outline: '1px solid #000',
              }"
              @click="selectColor(product.color)"
            >
              <q-icon
                v-if="selectedColor === product.color"
                name="done"
                :color="product.color === '#FFFFFF' ? 'black' : 'white'"
              >
              </q-icon>
            </div>
          </div>
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
import { defineComponent, ref, onMounted, watch, watchEffect } from "vue";
import { useProducts } from "../lib/useProducts";
import { Product } from "../lib/models/Product";
import { useRoute } from "vue-router";
import { Size } from "../components/models";

export default defineComponent({
  name: "DesignStep2",
  components: {},
  setup() {
    const route = useRoute();
    const { getProductsByType, getProductDetails } = useProducts();
    let products = ref<Product[]>();
    const sizes = ref<Size[]>([]);
    let stringSizes: String[] = [];
    let selectedSize = ref("");
    const selectedColor = ref("");
    const selectColor = (val: string) => {
      selectedColor.value = val;
    };

    const retrieveProductsByType = async (typeId: number) => {
      const data = await getProductsByType(typeId);
      if (data) {
        products.value = data;
      }
    };

    const updateSizes = async () => {
      let productId = ref();
      products.value?.forEach((product) => {
        if (product.color === selectedColor.value) {
          productId.value = product.id;
        }
      });
      const data = await getProductDetails(productId.value);
      sizes.value = [];
      stringSizes = [];

      data?.forEach((element) => {
        if (!sizes.value.includes(element.size)) {
          sizes.value.push(element.size);
        }
      });
      sizes.value.forEach((element) => {
        stringSizes.push(element.toString());
      });
    };

    watch(selectedColor, updateSizes);
    onMounted(async () => {
      try {
        await retrieveProductsByType(
          parseInt(route.params.productType.toString())
        );
      } catch (error) {}
    });

    const sizeIncluded = (size: string) => {
      return !sizes.value.toString().includes(size);
    };

    return {
      male: ref(false),
      female: ref(false),
      unisex: ref(true),
      size: ref(""),
      selectedColor,
      selectColor,
      products,
      sizes,
      Size,
      stringSizes,
      selectedSize,
      sizeIncluded,
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


        
