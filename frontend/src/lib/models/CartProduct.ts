import { Size } from "src/components/models";

export interface CartProduct {
    productId: number;
    illustrationId: number;
    editorIllustration: string;
    quantity: number;
    price: string;
    id: number;
    name: string;
    sizes: Size[];
    selectedSize: Size;
    image: string;
  }