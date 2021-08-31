import { ProductIllustration } from "./models/ProductIllustration";
import { reactive } from "vue";
import { useApi } from "./useApi";

interface stateType {
  productIllustrations: ProductIllustration[];
}

const state = reactive<stateType>({
  productIllustrations: [],
});

export const useProductIllustration = () => {
  const loadProductIllustrations = async (productType: number,illustrationId:number) => {
    try {
      const { data, error, ok } = await useApi<ProductIllustration[]>({
        url: "shop/productillustrationdetails/" + productType + "/" + illustrationId + "/",
      });

      if (ok) {
        state.productIllustrations = data;
      } else {
        console.log(error);
      }
    } catch (err) {
      console.log(`api err: ${err}`);
    }
  };

  return { state, loadProductIllustrations };
};
