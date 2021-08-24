import { Product } from "src/components/models";
import { reactive } from "vue";
import { useApi } from "./useApi";

interface stateType {
  products: Product[];
}

const state = reactive<stateType>({
  products: [],
});

export const useProducts = () => {
  const changePrice = (id: number) => {
    const product = state.products.find((product) => product.id === id);
    if (product) {
      product.price = 100;
    }
  };

  const loadProducts = async () => {
    try {
      const { data, error, ok } = await useApi<Product[]>({
        url: "shop/products/details/",
      });

      if (ok) {
        state.products = data;
      } else {
        console.log(error);
      }
    } catch (err) {
      console.log(`api err: ${err}`);
    }
  };

  return { state, changePrice, loadProducts };
};
