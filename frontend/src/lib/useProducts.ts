import { Product } from "./models/Product";
import { reactive } from "vue";
import { ProductDetails } from "./types/ApiResponses";
import { useApi } from "./useApi";

interface stateType {
  products: Product[];
}

const state = reactive<stateType>({
  products: [],
});

export const useProducts = () => {
  // const changePrice = (id: number) => {
  //   const product = state.products.find((product) => product.id === id);
  //   if (product) {
  //     product.price = 100;
  //   }
  // };

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

  const getProductDetails = async (productId: number) => {
    try {
      const { data } = await useApi<ProductDetails[]>({
        url: `shop/get_product_details/${productId}`,
      });

      return data;
    } catch (error) {}
  };

  const getProductsByType = async (productsType: number) => {
    try {
      const { data } = await useApi<Product[]>({
        url: `shop/get_products_by_type/${productsType}`,
      });

      return data;
    } catch (error) {}
  };

  return { state, loadProducts, getProductDetails,getProductsByType };
};
