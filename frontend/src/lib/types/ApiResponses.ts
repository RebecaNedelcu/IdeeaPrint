import { Sex, Size } from "src/components/models";
import { Product } from "../models/Product";
import { ApiUser } from "../models/User";

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  user: ApiUser;
  access_token_lifetime: number;
}

export interface RegisterResponse {
  email: string;
  first_name: string;
  id: number;
  is_active: boolean;
  is_staff: boolean;
  last_name: string;
  username: string;
}

export interface ProductDetails {
  id: number;
  product: Product;
  price: number;
  color: string;
  size: Size;
  sex: Sex;
  quantity: number;
  product_images: string[];
}
