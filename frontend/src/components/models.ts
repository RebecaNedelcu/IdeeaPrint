import { deprecate } from "util";

enum ProductType {
  TShirt,
  Hoodie,
  Mug,
  Totebag,
}

enum Size {
  XS,
  S,
  M,
  L,
  XL,
  XXL,
}

enum Sex {
  Man,
  Woman,
  Unisex,
}

export interface Illustration {
  image: string;
  name: string;
}

export interface Product {
  id: number;
  product: {
    type: ProductType;
    illustration: Illustration;
  };
  price: number;
  color: string;
  size: Size;
  sex: Sex;
  cantity: number;
  product_images?: [{ image: string }];
}

export interface CartProduct {
  id: number;
  name: string;
  price: number;
  image: string;
  size: string;
  quantity: number;
}
