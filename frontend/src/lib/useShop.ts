import { Illustration } from "src/lib/models/Illustration";
import { reactive } from "vue";
import { useApi } from "./useApi";

interface stateType {
  tshirts: Illustration[];
  hoodies: Illustration[];
  mugs: Illustration[];
  totebags: Illustration[];
}

const state = reactive<stateType>({
  tshirts: [],
  hoodies: [],
  mugs: [],
  totebags: [],
});

export const useShop = () => {
  const loadIllustrations = async (type: number) => {
    try {
      const { data, error, ok } = await useApi<Illustration[]>({
        url: "shop/illustrations/" + type + "/",
      });

      if (ok) {
        if (type === 1) state.tshirts = data;
        else if (type === 2) state.hoodies = data;
        else if (type === 3) state.mugs = data;
        else if (type === 4) state.totebags = data;
      } else {
        console.log(error);
      }
    } catch (err) {
      console.log(`api err: ${err}`);
    }
  };

  return { state, loadIllustrations };
};
