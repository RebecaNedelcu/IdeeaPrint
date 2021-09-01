<template>
  <q-page :style-fn="qpageMinHeight">
    <div class="row justify-between q-my-md">
      <q-input
        :input-style="{ color: '#000000' }"
        v-model="search"
        square
        dense
        standout="bg-grey-3"
        type="search"
        placeholder="Search"
        class="q-ml-xl searchDesign"
      >
        <template v-slot:append>
          <q-icon color="secondary" name="search" />
        </template>
      </q-input>

      <q-btn color="black" flat class="no-border-radius filterBtn q-mr-xl">
        <q-icon name="las la-sliders-h" color="secondary" />
        <q-menu class="meniu">
          <div class="no-wrap q-pa-md filters text-body2">
            <div class="column">
              <div class="text-h6 text-bold q-mb-md">Filters</div>
              <div class="q-mb-md">
                <span class="text-weight-medium">Product type:</span>
                <div>
                  <q-chip
                    v-model:selected="productType.Tshirt"
                    color="accent"
                    text-color="black"
                  >
                    T-shirts
                  </q-chip>
                  <q-chip
                    v-model:selected="productType.Mugs"
                    color="accent"
                    text-color="black"
                  >
                    Mugs
                  </q-chip>
                  <q-chip
                    v-model:selected="productType.Hoodies"
                    color="accent"
                    text-color="black"
                  >
                    Hoodies
                  </q-chip>
                  <q-chip
                    v-model:selected="productType.Totebags"
                    color="accent"
                    text-color="black"
                  >
                    Totebags
                  </q-chip>
                </div>
              </div>
              <div class="column q-mb-md">
                <span class="text-weight-medium">Sort by:</span>
                <q-radio
                  keep-color
                  v-model="color"
                  val="teal"
                  label="Price"
                  color="accent"
                />
                <q-radio
                  keep-color
                  v-model="color"
                  val="orange"
                  label="Name"
                  color="accent"
                />
                <q-radio
                  keep-color
                  v-model="color"
                  val="red"
                  label="Popularity"
                  color="accent"
                />
                <q-radio
                  keep-color
                  v-model="color"
                  val="cyan"
                  label="New"
                  color="accent"
                />
              </div>
              <div class="q-mb-md">
                <span class="text-weight-medium">Price:</span>
                <div class="q-px-xl q-pt-lg">
                  <q-range
                    v-model="label"
                    :min="1"
                    :max="500"
                    :step="1"
                    label-always
                    color="secondary"
                  />
                </div>
              </div>
            </div>

            <div class="row items-center justify-end">
              <q-btn
                flat
                color="black"
                label="Clear all"
                push
                size="sm"
                v-close-popup
                class="no-border-radius clearFilterButton text-bold"
              />
              <q-btn
                flat
                color="black"
                label="Apply filter"
                push
                size="sm"
                v-close-popup
                class="no-border-radius applyFilterButton text-bold q-ml-sm"
              />
            </div>
          </div>
        </q-menu>
      </q-btn>
    </div>
    <div class="row items-center justify-center">
      <item-card-component
        v-for="illustration in illustrations"
        :illustration="illustration"
        :key="illustration.id"
        class="col-12 col-md-3"
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import {
  computed,
  defineComponent,
  reactive,
  ref,
  onMounted,
  onBeforeUpdate,
} from "vue";
import ItemCardComponent from "../components/ItemCardComponent.vue";
import { useShop } from "../lib/useShop";
import { useRoute } from "vue-router";
import { Illustration } from "../lib/models/Illustration";

export default defineComponent({
  name: "Shop",
  components: {
    ItemCardComponent,
  },
  setup() {
    const route = useRoute();
    let illustrations = ref<Illustration[]>();
    type tproductType = {
      [key: string]: boolean;
    };
    const productType: tproductType = reactive({
      Tshirt: false,
      Mugs: false,
      Hoodies: false,
      Totebags: false,
    });
    type tproductSize = {
      [key: string]: boolean;
    };
    const productSize: tproductSize = reactive({
      XS: false,
      S: false,
      M: false,
      L: false,
      XL: false,
      XXL: false,
    });
    type tproductColour = {
      [key: string]: boolean;
    };
    const productColour: tproductColour = reactive({
      black: false,
      white: false,
      red: false,
      green: false,
      yellow: false,
      purple: false,
      blue: false,
    });

    const { state: illustrationsState, loadIllustrations } = useShop();

    onBeforeUpdate(async () => {
      await loadIllustrations(parseInt(route.params.id.toString()));
      if (parseInt(route.params.id.toString()) === 1)
        illustrations.value = illustrationsState.tshirts;
      else if (parseInt(route.params.id.toString()) === 2)
        illustrations.value = illustrationsState.hoodies;
      else if (parseInt(route.params.id.toString()) === 3)
        illustrations.value = illustrationsState.mugs;
      else if (parseInt(route.params.id.toString()) === 4)
        illustrations.value = illustrationsState.totebags;
    });
    onMounted(async () => {
      await loadIllustrations(parseInt(route.params.id.toString()));
      if (parseInt(route.params.id.toString()) === 1)
        illustrations.value = illustrationsState.tshirts;
      else if (parseInt(route.params.id.toString()) === 2)
        illustrations.value = illustrationsState.hoodies;
      else if (parseInt(route.params.id.toString()) === 3)
        illustrations.value = illustrationsState.mugs;
      else if (parseInt(route.params.id.toString()) === 4)
        illustrations.value = illustrationsState.totebags;
    });
    return {
      illustrations,
      ItemCardComponent,
      color: ref("cyan"),
      label: ref({
        min: 1,
        max: 500,
      }),
      search: ref(""),
      model: ref(null),
      productType,
      productSize,
      productColour,
      productTypeSelection: computed(() => {
        return Object.keys(productType)
          .filter((type) => productType[type] === true)
          .join(", ");
      }),
      productSizeSelection: computed(() => {
        return Object.keys(productSize)
          .filter((type) => productSize[type] === true)
          .join(", ");
      }),
      productColourSelection: computed(() => {
        return Object.keys(productColour)
          .filter((type) => productColour[type] === true)
          .join(", ");
      }),
      qpageMinHeight() {
        return { minHeight: "1vh" };
      },
    };
  },
});
</script>

<style lang="scss" scoped>
.searchDesign {
  border-style: solid;
  border-width: 2px;
}
.filterBtn {
  border-style: solid;
  background-color: white;
  border-width: 3px;
}

.filters {
  font-family: raleway;
  width: 500px;
  max-width: 85vw;
}
.applyFilterButton {
  border-style: solid;
  background-color: #c6b9ff;
  border-width: 3px;
}
.clearFilterButton {
  border-style: solid;
  background-color: white;
  border-width: 3px;
}
</style>
