import { CartProduct } from "./models/CartProduct";
import { reactive } from "vue";
import { Size } from "src/components/models";

interface stateType {
  cartProducts: CartProduct[];
}

const state = reactive<stateType>({
  cartProducts: [],
});

let staticId = 1;

export const useCart = () => {
  const addCartProduct = (
    productId: number,
    illustrationId: number,
    editorIllustration: string,
    quantity: number,
    price: string,
    name: string,
    sizes: Size[],
    selectedSize: Size,
    image: string
  ) => {
    let newProd: CartProduct = {
      productId: productId,
      illustrationId: illustrationId,
      editorIllustration: editorIllustration,
      quantity: quantity,
      price: price,
      id: staticId,
      name: name,
      sizes: sizes,
      selectedSize: selectedSize,
      image: image,
    };
    state.cartProducts.push(newProd);
    staticId++;
  };
  const removeCartProduct = (index: number) => {
    state.cartProducts.splice(index, 1);
  };
    const incrementQuantity = (index: number) => {
      if (state.cartProducts[index].quantity)
        state.cartProducts[index].quantity += 1;
    };
    const decrementQuantity = (index: number) => {
      if (state.cartProducts[index].quantity > 1)
        state.cartProducts[index].quantity -= 1;
    };

  return { state, addCartProduct,removeCartProduct,incrementQuantity,decrementQuantity };
};
