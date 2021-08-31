import { Illustration } from "./Illustration";
import { Product } from "./Product";

export interface ProductIllustration {
    id: number;
    product: Product;
    illustration: Illustration;
    image: string;
}