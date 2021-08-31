<template>
  <q-page :style-fn="qpageMinHeight">
    <div class="row items-center justify-center">
      <item-card-component
        v-for="data in favoriteIllustrations"
        :illustration="data.illustration"
        :key="data.id"
        class="col-12 col-md-3"
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import ItemCardComponent from "../components/ItemCardComponent.vue";
import { FavoriteIllustrations } from "../lib/models/Illustration";
import { useUser } from "../lib/useUser";

export default defineComponent({
  name: "Shop",
  components: {
    ItemCardComponent,
  },
  setup() {
    const { getFavoriteIllustrationsWithData } = useUser();
    const favoriteIllustrations = ref<FavoriteIllustrations[]>();
    onMounted(async () => {
      try {
        const data = await getFavoriteIllustrationsWithData();
        favoriteIllustrations.value = data;
      } catch (error) {}
    });

    return {
      favoriteIllustrations,

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