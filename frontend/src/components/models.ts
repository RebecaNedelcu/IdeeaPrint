import { deprecate } from "util";

enum ProductType {
  TShirt,
  Hoodie,
  Mug,
  Totebag,
}

export enum Size {
  XS,
  S,
  M,
  L,
  XL,
  XXL,
}

export enum Sex {
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


